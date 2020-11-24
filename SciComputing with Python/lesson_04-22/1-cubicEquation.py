import math
def cubRoot(x):
    y = (abs(x))**(1.0/3.0)
    if(x<0): y = -y
    return y
print "To solve x3+ax2+bx+c=0: "
p = float(input("Enter a value for a: "))
q = float(input("Enter a value for b: "))
r = float(input("Enter a value for c: "))

A = (3.0*q-p*p)/3.0
B = (2.0*p*p*p-9.0*p*q+27.0*r)/27.0
D = A*A*A/27.0+B*B/4.0

    
if(D>=0):
    M = cubRoot(-B/2.0+(D**0.5))
    N = cubRoot(-B/2.0-(D**0.5))
    
    x1 = M + N
    x2 = complex(-(M+N)/2.0,math.sqrt(3)*(M-N)/2)
    x3 = complex(-(M+N)/2.0,-math.sqrt(3)*(M-N)/2)
elif(D<0):
    if(B>=0):
        phi = math.acos(-math.sqrt((B*B/4.0)/(-A*A*A/27)))
    elif(B<0):
        phi = math.acos(math.sqrt((B*B/4.0)/(-A*A*A/27.0)))
    else:
         print "You fucked something"        
         
    x1 = 2*math.sqrt(-A/3)*math.cos(phi)
    x2 = 2*math.sqrt(-A/3)*math.cos(phi+2*math.pi/3)
    x3 = 2*math.sqrt(-A/3)*math.cos(phi+4*math.pi/3)
else:
    print "You fucked something"

print "x1= ",x1-p/3.0
print "x2= ",x2-p/3.0
print "x3= ",x3-p/3.0
exit = input("Press Ctrl+F6")
