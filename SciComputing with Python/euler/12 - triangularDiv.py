triangle = 3.
i = 3.
divisors = []
while len(divisors) < 500:
    divisors = [1,triangle]
    divisor = 2.
    while divisor < triangle**.5:
        if(triangle%divisor==0):
            divisors.append(divisor)
            divisors.append(triangle/divisor)
        divisor +=1
    triangle += i
    i += 1
print divisors
print triangle-i+1
