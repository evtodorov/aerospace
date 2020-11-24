from math import sqrt
m = 2000000
nums = range(2,m)
primes = [2]
s = 2
for n in nums:
    prime = True
    for j in primes:
        if(n%j==0):
            prime = False
            break
    if(prime):
        i = 2
        while (i*n < m and i*n in nums):
            nums.remove(nums.index(i*n))
            i+=1
        primes.append(n)
        s += n
print s
