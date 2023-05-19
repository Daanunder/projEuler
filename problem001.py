import numpy as np
import math

n = 1000
d = [3,5]
totalset = []
for i in d:
    toplim = math.floor((n-1)/i)
    t = [i*m for m in range(1,toplim+1)]
    totalset += t

s = np.unique(totalset)
print(s)
print(sum(s))

