import numpy as np
M1 = np.random.randn(1000,1000)
M2 = np.random.randn(1000,1000)
for x in range(0, 1000):
    M1 = M2 + M1
print(M1)
