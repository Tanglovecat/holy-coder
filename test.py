import matplotlib.pyplot as plt
import math
x = [ 0.01*i for i in range(3140)]
y = [math.sin(i) for i in x]
plt.plot(x,y,'r')
plt.show() 
