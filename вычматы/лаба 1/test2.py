import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.sparse import coo_array
from scipy.sparse.linalg import splu
from scipy.sparse import csc_matrix, linalg as sla

x = []

a = 10000
h=1/math.sqrt(a)
c=0.1





for i in range(a):
    x.append([0] * a)
    x[i][i] = 4+c* h **2
    if i-math.sqrt(a)>=0:
        x[i][i-int(math.sqrt(a))]=-1
    if i+math.sqrt(a)<a:
        x[i][i+int(math.sqrt(a))]=-1
    if i%math.sqrt(a) == 0:
        x[i][i+1]=-1
    elif (i+1)%math.sqrt(a) == 0:
        x[i][i-1]=-1
    else:
        x[i][i+1]=-1
        x[i][i-1]=-1
        
k=np.array([1] * a, dtype=float)


p = splu(x)
z2=p.solve(k)

g = [0] * int(math.sqrt(a))
y = [0] * int(math.sqrt(a))
for i in range(int(math.sqrt(a))):
    g[i] = h * i
    y[i] = h * i

fig, ax = plt.subplots(1, 1)

x1 = np.array(g)
y1= np.array(y)

x1, y1 = np.meshgrid(x1, y1)


c1 = ax.tricontourf(x1.flatten(),y1.flatten(),z2, cmap="plasma")

fig.savefig("sol.png")

        


