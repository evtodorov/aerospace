"""
Created on Tue Apr 29 09:49:26 2014

Obtain CL(alpha) data from a dat file and plot it
@author: etodorov
"""
cL = []
alpha = []
f = open("D:/Dropbox/Aerospace/Python/29-04-14/clalpha.dat", "r")
txt = f.readlines()
for line in txt:
    if(line[0].isupper()):
        continue
    else: 
        alpha.append(float(line.split(",")[0]))
        cL.append(float(line.split(",")[1]))
table="alpha \t \t \t cL"
for i in range(len(cL)):
    table = table+"\n"+str(alpha[i])+"\t"+"\t"+"\t"+str(cL[i])
print table
f.close()
    