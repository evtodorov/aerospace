hours = input("Hours: ")
minutes = input("Minutes: ")

if(hours>=12):
    hours = hours - 12
elif(hours>=24):
    print "Give me hours and minutes"
    
if(minutes>=60):
    print "Give me hours and minutes"
    
hoursAngle = hours*(360.0/12.0)+minutes*(360.0/12.0/60.0)
minutesAngle= minutes*(360.0/60)

betweenAngle = hoursAngle - minutesAngle
if(betweenAngle<0):
    betweenAngle = -betweenAngle
if(0<=betweenAngle<=180):
    print betweenAngle
#elif(-180<=betweenAngle<=0):
#   print (-betweenAngle)
elif(180<=betweenAngle<=360):
    print (360-betweenAngle)
#elif(-360<=betweenAngle<=180):
#    print (360+betweenAngle)
