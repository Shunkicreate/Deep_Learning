import numpy as np
import matplotlib.pylab as plt

#Rectified Linear Unit

def relu(x):
    return np.maximum(0,x)
x=np.arange(-5.0,5.0,0.1)
print(x)
y=relu(x)
plt.plot(x,y)
plt.ylim(-1,6)
plt.show()