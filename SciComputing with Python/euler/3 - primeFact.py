from math import sqrt
n = 600851475143
fact = []
primeFact = []
for i in range(2,int(sqrt(n))):
    #check if a factor
    if(n%i==0): 
        #check if factor is prime
        prime = True
        j=2
        while(j<=sqrt(i)):
            if(i%j==0): 
                print "Not a prime",i
                prime = False                
                break
            j+=1
        fact.append(i)
        if(prime): 
            primeFact.append(i)
            prime = False
print fact
print primeFact[-1]