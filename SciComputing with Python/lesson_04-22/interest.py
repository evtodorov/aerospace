print "    *** Interest calculator  **** "
print

x0    = input("Enter the begin value of savings (or debt):")
perc  = input("Enter yearly interest rate in percent:")
years = input("Enter number of years:")

x1 = x0*((1.0 + perc/100.0)**years)

print
print " End amount after",years,"years is",int(x1*100)/100.
print
