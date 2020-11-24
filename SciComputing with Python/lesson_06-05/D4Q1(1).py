import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,9,901)   # or:
x = np.arange(0,9.01,0.01)

y2 = x*x  
y3 = x*x*x

#or:

y2 = x**2
y3 = x**3 

plt.plot(x,y2,'r.')
plt.plot(x,y3,'b+')
plt.show()

