import numpy as np
def step_function(x):
    y=x>0
    y = y.astype(np.int)
    return y

print(step_function(np.array([-1,4,3,-23])))
    