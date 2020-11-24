i = 1
more = 1
points = []
while(more==1):
    points.append([])
    pointX = input("enter X coordinate for "+str(i)+" point")
    pointY = input("enter Y coordinate for "+str(i)+" point")
    points[i-1].append(pointX)
    points[i-1].append(pointY)
    i+=1
    more = input("Press 1 to add more points or 0 to stop adding points")
hold = raw_input("Press enter")
s = 0
sigma = 0

n = len(points)
# from i = 1 to i = n-1
for j in range(1,n):
    # y_i+1              y_i           x_i+1       x_i
    s = (points[j][1]+points[j-1][1])*(points[j][0]-points[j-1][0])/2
    print s
    sigma += s
    # y1            yn              x1          xn
A0 = (points[0][1]+points[-1][1])*(points[0][0]-points[-1][0])/2.
A = A0 + sigma
print "The area is "+str(abs(A))
