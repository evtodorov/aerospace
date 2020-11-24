# Program to calculate angle between clock hands
# as function of time entered by the user

print "Time at hand: calculates angle betweesn clock hands"
print
print "I need the time in  hours (0-23) and minutes (0-59)."
print

# Input values

hr = int(input("Enter the hours of the time first(0-23): "))
mn = int(input("Now enter the minutes of the time(0-59): "))

# Check validity of entered values
if hr>=0 and hr<24 and mn>=0 and mn<60:

# Calculate angle
    
    angle_hr = (float(hr%12)+float(mn)/60.)*30 # every hour is 30 degrees as 12*30=360
    angle_mn = float(mn)*6.    # every hour is  6 degrees as 60*6=360

    diffangle = abs(angle_hr - angle_mn)

    if diffangle>180:
        diffangle  = 360-diffangle

# Show result, e.g. for 6:30 answer is 15 degrees

    print
    print "Angle between clock hands is:",diffangle," degrees"


# Invalid entry

else:

    print "Invalid inpout values!"
    print "Hours should be 0-23"
    print "Minutes should be 0-59"
    
