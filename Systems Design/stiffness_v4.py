#with changing thickness NB
#!!!!!!!! thickness change is turned off, since the results are not consitstent;
#to turn on, delete line 37 ("ratio_hv = 1" in fitness())
#TODO: 
#TODO:  stress calculations? for torsion.
#TODO: built in torsion (not really necessary); 
import numpy as np
from random import random, randint, choice


Li = 2.86


# #Al
#G = 26e+9
E = 72e+9
density = 2700.
sigma_yield = 300e+6

#toff
#E = 68e+9
#density = 2350.
#sigma_yield = 490e+6


#Foam
#E = 4e+4
#sigma_yield = .005e+6
#density = 150.

#CFRP
#E= 135e+9
#density = 1600.
#sigma_yield = 600e+10

#Titanim
#E = 116e+9
#density = 4500. 
#sigma_yield = 

#Steel
#E = 200e+9
#density = 7800.
#sigma_yield = 

Mi = [88.3e+3,401.6e+3,967.3e+3,1.7e+6,2.6e+6,3.6e+6,4.7e+6,5.8e+6,7e+6,7.9e+6]
Vi = np.array([61.7,157,238,297,335,357,365,449,349,331])*1000. #asssume no stress due to shear force at crit point
Mi = np.array(Mi)
Ti = np.array([])
ci = [3.2,3.9,4.61,5.31,6.01,6.72,7.42,8.12,8.83,9.53]
ci = np.array(ci)
#distribution on t(y)
#fitness function: don't breed if too high displacement, more fit if lighter
def thickness(t_min,t_max, length,max_ratio_hv=10):
    #top thickness/side thickness ratio_hv (0-1)
    mag = 10**(-int(np.log10(t_min))+1) #scale t so that t_min is integer
    t_min = t_min*mag
    t_max = t_max*mag
    #print mag, t_min, t_max
    t = [ (randint(t_min,t_max-1)+randint(0,9)*.1)/mag for i in xrange(length) ]
    ratio_hv = random()*max_ratio_hv
    while (np.any(t<t_min)): 
        ratio_hv = 10*random()*max_ratio_hv+0.1 #makes sure no thickness smaller than the minimum even with the ratio_hv 
        #print "while thickness"
    return np.array(t),ratio_hv

def max_arr(arr1,arr2):
    out = arr2
    for i in xrange(len(arr1)):
        if arr1[i] >= arr2[i]:
            out[i] = arr1[i]
    return out
            
def fitness((t,ratio_hv),delta_max):
    #retruns the mass for every thickness distribution that work, increases the thickness*(1+random) if delta is too high
    t = np.array(t)
    
    ratio_hv = 1
    ratio_tb = 1
    
    t_side = t*ratio_hv
    t_top = t
    t_bot = t*ratio_tb
    h_na = (t_top-t_bot)/(t_bot+t_top)
    h_top = 0.05*ci-h_na
    h_bot = 0.05*ci+h_na
    
    Ii_t = inertia(t,ratio_hv)
      # side \ top \bottom

    if(np.any(t==0)): return float('inf'), t
    
    #displacement    
    deltai_t = Mi*Li**2/2./E/Ii_t
    phii_t = Mi*Li/E/Ii_t
    delta_t = 0.
    for i in xrange(len(deltai_t)):
        delta_t += deltai_t[i]+sum(phii_t[i:])*Li
    
    #yield stress: all beam elements
    M_internal = [sum(Mi[:i+1]) for i in xrange(len(Mi))]
    sigma = M_internal*max_arr(h_top,h_bot)/Ii_t
    #print "fitness"
    
    #rotation
    #theta = 
    
    #mass
    mi = (0.45*(t_top+t_bot)+0.1*t_side)*ci*density*Li
    m = sum(mi)
    
    check_delta = delta_t < delta_max
    check_sigma = sigma_yield > sigma
    #goodenough = check_delta and check_sigma
    #print goodenough, (sigma_yield > sigma).any(), sigma    
    if not check_delta: 
        return fitness((t*(1.+random()),ratio_hv),delta_max)
    elif not check_sigma.all():
        return fitness((t*(1.+random()*(check_sigma==False)),ratio_hv),delta_max)
    else:
        return m, (t, ratio_hv)
def inertia(t,ratio_hv,ratio_tb=1):
    t_side = t*ratio_hv
    t_top = t
    t_bot = t*ratio_tb
    h_na = (t_top-t_bot)/(t_bot+t_top)
    h_top = 0.05*ci-h_na
    h_bot = 0.05*ci+h_na
    
    Ii_t = 2*(1/12*t_side*(.1*ci)**3+.1*ci*t_side*h_na**2) + 0.45*ci*t_top*h_top**2 +  0.45*ci*t_bot*h_bot**2 
    return Ii_t
def evolve (pop, delta_max, retain=.25, random_select=0.1, mutate = 0.5, diverge=0.5, threshold = 1.,max_gen=1e+6):
    #grade all thicknesses and choose retain% that have lowest mass=fitness
    
    graded = [ fitness(x,delta_max) for x in pop]
    graded_sorted = sorted(graded, key= lambda x: x[0])
    average = 0
    for i in graded_sorted:
        average += i[0]
    average = average/len(graded_sorted)
    best = graded_sorted[0][0]
    print "Best: %s kg \t Average: %s kg" % (str(best), str(average))
    graded = [ x[1] for x in graded_sorted]

    ret_len = int(len(graded)*retain)
    parents = graded[:ret_len]


        
    # randomly add other individuals to promote genetic diversity
    for individual in graded[ret_len:]:
        if random_select > random():
            parents.append(individual)

    # mutate some individuals
    #requires reentering of the min values (for now)
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
            individual[0][pos_to_mutate] = thickness(t_min,t_max,10)[0][randint(0, len(individual)-1)]
        #ratio_hv mutation
        #individual[0] is thickness distribution, individual[1] is ratio_hv
        if mutate > random() and False: #mutation ratio_hv turned off
            mut_ratio_hv = individual[1]*choice([randint(1,10),1./float(randint(1,10))])
            while(np.any(individual[1]*mut_ratio_hv<0.0005)): #makes sure no thickness smaller than the minimum even with the ratio_hv 
                mut_ratio_hv = individual[1]*randint(1,10)
                #print "while mutation"
                #print mut_ratio_hv
                #print mut_ratio_hv*individual[1]
            individual = (individual[0],mut_ratio_hv)
        
        if diverge > random():
            pos_to_mutate = randint(0, len(individual)-1)
            individual[0][pos_to_mutate] *= 1.- random()
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    
    while len(children) < desired_length:
        #print "while sex"
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female and (parents[male][0]!=parents[female][0]).any():
            if (male<female): ratio_hv = parents[male][1]
            else: ratio_hv = parents[female][1]
            male = parents[male][0]
            female = parents[female][0]
            child = ([ choice([male[i],female[i]]) for i in xrange(len(male))],ratio_hv)
            children.append(child)
#    if (max_gen-1)%50==0:
#        print "PURGE", max_gen, "left"
#        parents = parents[:1]
#        children = [thickness(t_min,t_max,t_len) for i in xrange(p_length-1)]
    parents.extend(children)
    
        #stop if the parents have the same mass
    if(abs(graded_sorted[0][0]-graded_sorted[ret_len][0])< threshold):
        print "Converged: \n Mass1: %d \n distribution1: %s \n Thickness ratio_hv (v/h)1: %s" % (graded_sorted[0][0],str(graded_sorted[0][1][0]),str(graded_sorted[0][1][1]))
        print "\n Mass2: \t %d \n distribution2: \t %s \n Thickness ratio_hv (v/h)2: \t %s" % (graded_sorted[1][0],str(graded_sorted[1][1][0]),str(graded_sorted[1][1][1]))
        print "\n Mass3: %d \n distribution3: %s \n Thickness ratio_hv (v/h)3: %s" % (graded_sorted[2][0],str(graded_sorted[2][1][0]),str(graded_sorted[2][1][1]))
        return graded_sorted[0][1][0] 
    elif(max_gen<=0):
        print "Not converged before max" , graded_sorted[0]
        return parents
    elif(abs(graded_sorted[0][0]-graded_sorted[ret_len][0])< threshold*10):
        return evolve(parents,delta_max,mutate=0.2,max_gen=max_gen-1)
    else:
        #print "recursion evolve"
        return evolve(parents,delta_max,max_gen=max_gen-1)

    
p_length = 1500
evolutions = 1000
t_min = 0.0005
t_max = 0.002
t_len = 10
delta_max = 9.4
from time import time
t0 = time()
import sys
sys.setrecursionlimit(10*evolutions)
population = [thickness(t_min,t_max,t_len) for i in xrange(p_length)]
#the_best = evolve(population,delta_max,max_gen=evolutions)
print "IN", -t0 + time()
#for p=1000, retain=.25 and convergence threshold=1.0 typical runtime is around 10 seconds.
