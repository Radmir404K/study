import numpy as np
import statistics
import matplotlib.pyplot as plt
import sys

def conjGrad(A,x,b,tol,r0):
    r = b - A.dot(x)
    p = r.copy()
    res3 = []
    for i in range(300):
        Ap = A.dot(p)
        if i == 0:
            alpha = 0.1
        elif i != 0:
            alpha = np.dot(p,r)/np.dot(p,Ap)
        x = x + alpha*p
        r = b - A.dot(x)
        if float(np.sqrt(r.dot(r)))/r0 < tol:
            res3.append(float(np.sqrt(r.dot(r)))/r0)
            break
        else:
            beta = -np.dot(r,Ap)/np.dot(p,Ap)
            p = r + beta*p
            res3.append(float(np.sqrt(r.dot(r)))/r0)
    return [res3, x] 

def iter2(u, k, f, A, r0, rkv, tau, res2, P):
    k += 1
    u1 = u + P.dot(rkv)
    rkv = f - A.dot(u1)
    rk = float(np.sqrt(rkv.dot(rkv)))
    res2.append(rk/r0)
    if rk/r0 <= 0.0001:
        return [res2, u1]
    
    else:
        iter2(u1, k, f, A, r0, rkv, tau, res2, P)
        return [res2, u1]

def iter(u, k, f, A, r0, rkv, tau, res1):
    k += 1
    u1 = u + tau * rkv
    rkv = f - A.dot(u1)
    rk = float(np.sqrt(rkv.dot(rkv)))
    res1.append(rk/r0)
    if rk/r0 <= 0.0001:
        return [res1, u1]
    
    else:
        iter(u1, k, f, A, r0, rkv, tau, res1)
        return [res1, u1]



sys.setrecursionlimit(10000)
f = np.array([0.] * 495 + [1.] * 11 + [0.] * 494)

A = np.array([[0.] * 1000] * 1000)

Beta = 10

tau = 0.0826

Alpha = 0.01

P = np.array([[0.] * 1000] * 1000)

for i in range(len(A)):
    if i == 0:
        A[i][i] = 2 + Beta
        A[i][i + 1] = -1

    elif i == len(A) - 1:
        A[i][i] = 2 + Alpha
        A[i][i - 1] = -1

    else:
        A[i][i] = 2 + Alpha
        A[i][i + 1] = -1
        A[i][i - 1] = -1
    
    P[i][i] = A[i][i]

u = np.array([0.] * 1000)

k = 0

u0 = np.array([0] * 1000)

r0v = f - A.dot(u0)

r0 =float(np.sqrt(r0v.dot(r0v)))

P = np.linalg.inv(P)

#res = np.linalg.eig(A)
#print(max(res[0]), min(res[0]))

res1 = []
res2 = []

res1 = iter(u0, k, f, A, r0, r0v, tau, res1)

res2 = iter2(u, k, f, A, r0, r0v, tau, res2, P)

res3 = conjGrad(A,u0,f,10**(-4),r0)

#print(x)

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

#fig1, ax1 = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = list(range(0, 13000))


#plt.ylim(0, 1)
ax.semilogy(x[:len(res1[0])], res1[0], linestyle="None", marker='o', color="g", label = "простая итерация") #график
ax.semilogy(x[:len(res2[0])], res2[0], linestyle="None", marker='o', color="b", label = "без параметра") #график
ax.semilogy(x[:len(res3[0])], res3[0], linestyle="None", marker='o', color="r", label = "градиент") #график

ax.legend()


#ax1.plot(x[:len(res1[1])], res1[1], markersize = 15, linestyle="None", marker='^', color="g", label = "эксперименты") #график
#ax1.plot(x[:len(res1[1])], res1[1], markersize = 12, linestyle="None", marker='s', color="b", label = "эксперименты") #график
#ax1.plot(x[:len(res1[1])], res1[1], linestyle="None", marker='o', color="r", label = "эксперименты") #график

fig.savefig("graph.png") #сохранение
#fig1.savefig("sol.png") #сохранение
