r = range(101)
s=0
sq=0
for i in r:
    s += i
    sq += i*i
    print i, s, sq
print s*s - sq