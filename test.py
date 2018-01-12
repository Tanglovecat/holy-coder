import matplotlib.pyplot as plt
import math
x = [ 0.01*i for i in range(3140)]
y = [math.sin(i) for i in x]
y = [i**2 for i in y]
plt.plot(x,y,'r')
plt.show()
 
