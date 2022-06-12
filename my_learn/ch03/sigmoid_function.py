import matplotlib.pylab as plt
import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))

x=np.arange(-5.0,5.0,0.1)
# print(x)
y=sigmoid(x)
# plt.plot(x,y)
# plt.ylim(-0.1,1.1)
# plt.show()
print(sigmoid(10000000),sigmoid(-10000000))