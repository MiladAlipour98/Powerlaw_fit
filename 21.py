import numpy as np
import matplotlib.pyplot as plt

def gamma_ds(ds,kmin): #step 1
    N = len(ds)
    return 1 + (N / np.log(ds/(kmin - 1/2)).sum())

def zeta(gamma, ds, kmin):
    index_of_kmin = np.where(ds == kmin)[0][0]
    return (ds[index_of_kmin:] ** (-gamma)).sum()


def Pk(gamma, ds, kmin):
    ps = []
    for k in ds:
        p = 1 - (zeta(gamma, ds, k) / zeta(gamma, x, kmin))
        ps.append(p)
    return np.array(ps)

def D(P_k,S_k,kmin,x):
    index_of_kmin = np.where(x == kmin)[0][0]
    print(len(S_k), len(P_k))
    print(P_k)

    result = np.abs(S_k[index_of_kmin:]-P_k[index_of_kmin:])
    print("result =" ,result)
    return result.max() if len(result) > 0 else 1

file = open("terrorism.txt", "r")
lines = file.read().strip().split()
d = [int(float(i)) for i in lines]
print(d)
ds = np.array(d)
lmn= 10
print(ds[-1])
m = max(ds)
print(m)
n = len(ds)
print(n)
ds_dict = dict((i, d.count(i)) for i in set(ds))
print(ds_dict)
x = list(ds_dict.keys())
y =list(ds_dict.values())
x.sort()
x = np.array(x)
print(x)
#print(z)
y = [element / n for element in y]
#print(y)

S_k =[]
for i in range(len(y)):
     S_k.append(sum(y[i:]))
S_k = np.array(S_k)
print(S_k)
Ds = []

for kmin in x:
    gamma = gamma_ds(ds,kmin)
    P_k = Pk(gamma,x,kmin)
    Di = D(P_k,S_k,kmin,x)
    Ds.append(Di)
Ds = np.array(Ds)
print(Ds)


plt.plot(x, Ds, 'r.', markersize=4)
plt.xlabel("$Kmin$")
plt.ylabel("$D$")
plt.title("D-Kmin")
plt.show()


