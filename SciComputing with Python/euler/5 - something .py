#Smallest evenly divisible number
n=10
res = 1
for i in range(n,1,-1):
    if(res%i!=0): res=res*i
print res