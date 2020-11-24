import time

startCPU = time.clock()
startCAL = time.time()



for i in xrange(0,10000000):
    if(False):break
    

elapsedCPU = time.clock()-startCPU
elapsedCAL = time.time()-startCAL
print "CPU time", elapsedCPU
print "Clock time", elapsedCAL
