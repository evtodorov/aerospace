a = 0
b = 0
i = 0
for a in xrange(1000):
    for b in xrange(1000):
        c = 1000 - (a+b)
        if(a*a+b*b==c*c):
            print a,b,c, a*b*c
