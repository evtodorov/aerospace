from math import pi

# Find pi according to Leibniz formula
#
# pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - ...


# Number of iterations
N = 1000000

# Starting values
estpi  = 0.
sign   = 1.

# Serie
for i in xrange(1,N*2,2):
    estpi = estpi + 4.*sign/float(i)
    sign  = -sign

print "Estimated pi =",estpi
print "Real pi      =",pi


    
