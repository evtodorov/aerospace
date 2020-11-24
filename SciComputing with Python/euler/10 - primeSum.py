from math import sqrt
m = 2000000
nums = range(2,m)
primes = []
s = 0
for n in nums:
    prime = True
    for j in primes:
        if(n%j==0):
            prime = False
            break
    if(prime):
        primes.append(n)
        s += n
print s
