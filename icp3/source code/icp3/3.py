import numpy as np
v = np.random.randint(1,20,15)
print(v)
v[np.where(v==np.amax(v))]=0
print(v)