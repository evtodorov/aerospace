import math

print "To solve for the hipotnuse: "
a = input("Enter a value for a: ")
b = input("Enter a value for b: ")

if(a>=0, b>=0):
    c = math.sqrt(a*a+b*b)
    print "c= ",c
else:
    print "No such triangle"


