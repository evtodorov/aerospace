import math
n=2
primes = []
while len(primes)<10001:
    i = 2
    check = True
    while (i<=math.sqrt(n)):
        if(n%i==0): 
            check = False
            
            break
        i +=1
    if(check): primes.append(n)
    n+=1
print primes[-1]
print primes[10002]

#Put a number to check if it is prime: 
#65845484531
#65845484531 is a prime
#Press enter to try again