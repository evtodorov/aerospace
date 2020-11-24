from math import sqrt,atan2

# Problem 4: Gravity forces

def gravforce(m,x,y):

    G = 6.674e-11
    fx = []
    fy = []
    n = len(m)
    
    for i in range(n):
        sfx = 0
        sfy = 0

        for j in range(n):

            if not i==j:
                r2 = (x[i]-x[j])**2 + (y[i]-y[j])**2
                F = G*m[i]*m[j]/r2
                r = sqrt(r2)

                angle = atan2(y[j]-y[i]),[xj]-x[i])
                sfx = sfx + F*cos(angle)
                sfy = sfy + F*sin(angle)
                
                sfx = sfx + F*(x[j]-x[i])/r
                sfy = sfy + F*(y[j]-y[i])/r

        fx.append(sfx)
        fy.append(sfy)

    return fx,fy
