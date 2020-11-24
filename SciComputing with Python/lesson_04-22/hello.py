import os

print 'T converter F and C'

scale = raw_input ("Enter F to convert  F  to C or C  to convert C to F: ")

if(scale=='f' or scale=='F'):
    tempIn = raw_input("Enter temperature in degrees F: ")
    scaleIn = 'Fahrenheit'
    tempOut = (float(tempIn)-32)*5/9
    scaleOut = 'Celsius'
elif(scale=='c' or scale=='C'):
    tempIn = raw_input("Enter temperature in degrees C: ")
    scaleIn = 'Celsius'
    tempOut = float(tempIn)*9/5+32
    scaleOut = 'Fahrenheit'
else:
    print 'Fuck you bitch'


print tempIn," degrees ",scaleIn," is ",tempOut," degrees ",scaleOut
print 'Now fuck off'

