"""
Project euler problem #2 and 25

"""

fib = []
tot = 0
fib.append(1)
fib.append(2)
i=2
run = True
#while(fib[i-1]<4000000):
while run:
    fib.append(fib[i-2]+fib[i-1])
    i+=1
    if(fib[-1]>10**999):
        run = False
print len(fib)+1
#for i in fib:
#    if(i%2==0): tot+=i
#if(fib[-1]%2==0): tot = tot - fib[-1]
#print "fib",fib
#print 'tot',tot



    