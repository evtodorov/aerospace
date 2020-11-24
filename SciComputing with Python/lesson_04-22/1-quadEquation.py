import math

print "To solve ax2+bx+c=0: "
a = input("Enter a value for a: ")
b = input("Enter a value for b: ")
c = input("Enter a value for c: ")

D = b**2-4.0*a*c

if(D>=0):
    x1=(-b-math.sqrt(D))/(2.0*a)
    x2=(-b+math.sqrt(D))/(2.0*a)
    print "x1= ",x1
    print "x2= ",x2
else:
    print "No real solutions"

exit = input("Press Ctrl+F6")

