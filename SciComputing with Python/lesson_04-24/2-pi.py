choice = input("Calculate pi using \n \
1) Leibniz's formula \n \
2) The inverse sin fucntion \n")
s=0

acc = input("Number of decimal places accuracy in the calculation of pi: \n" )
if(choice==1):
    i=0
    while (1/(i*2.+3.)>(1./(10**(acc+1)))):
        s += ((-1.0)**i)/(2.0*i+1.0)
        i+=1
    pi = 4.*s
if(choice==2):
    i = 1
    ls = []
    llodd = []
    lleven=[]
    while(1/(3.*2**(2.*i+2.))>(1./(10**(acc+1)))):
    #while(i<10):
        #print 1/(3.*2**(2.*i+2.))
        #print (1./(10**(acc+1)))

        odd = 1
        even = 1
        lodd = []
        leven = []
        for j in range(0,i): 
            odd = odd*(2.*(j+1)-1)
            even = even*(2.*(j+1))
        s += odd/even/(2.**(2.*(i)+1.))/(2.*(i)+1.)
        i+=1
    i = i-1
    pi = 6.*(.5+s)
print "Pi is approximately",pi
print "This calculation required n of minimum "+str(i)

hold = raw_input("Press enter to continue")
