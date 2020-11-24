#Largest palyndrome product of 3-digit numbers
#unfinished
check = True
r = range(1000,100,-1)
pal = []
for i in r:
    for j in r:
        n = i*j     #get a product
        nstr = []   
        #product to list
        for k in range(len(str(n))):
            nstr.append(str(n)[k])
        #invert the list
        #not using reverse because BECAUSE
        inv = range(len(nstr))
        for l in inv:
            inv[l]=nstr[-(l+1)]
        if(inv==nstr):
            print "The largest palyndrome product is",j,"x",i,"=",inv
            break
            break
            break