import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

def plot_data1(start, stop, x):
    c = np.arange(start, stop, 1)
    # Func 1
    y = c**3 + 1000*c**2 - 500000*c + x
    plt.plot(c,y)
    plt.grid(True)
    plt.show()
    return c, y

def func1(a,b):
    A = (1/2*10**6 - (a**2+b**2) - (a*b))/(a+b)
    #return np.clip(a, 0, 998)
    return A

def func2(a,b):
    A = (-(a+b)+np.sqrt(a**2+b**2-6*a*b+2*10**6))/2
    #return np.clip(a, 0, 998)
    return A

def func3(a,b):
    A = (-(a+b)-np.sqrt(a**2+b**2-6*a*b+2*10**6))/2
    #return np.clip(a, 0, 998)
    return A

def plot_data2():
    a = np.arange(1,1001)
    b = np.arange(1,1001)
    aa, bb = np.meshgrid(a,b)

    z1 = func1(aa, bb)
    z2 = func2(aa, bb)

    z3 = z1 + aa + bb - 1000
    z4 = z2 + aa + bb - 1000
    
    C = []
    total = []
    for i in range(1000):
        for j in range(1000):
            if z3[i,j] == 0.0:
                print(f'z3 {i,j}')
            if z4[i,j] == 0.0:
                pass
            #c = np.sqrt(a**2 + b**2)
            #C.append(c)
            #total.append(a+b+c)


            

    #fig, ax = plt.subplots(1,2, figsize=(15,15))
    #a1 = ax[0].contourf(a,b,z1, np.arange(0,1001,100))
    #ax[0].axis('equal')
    #a2 = ax[1].contourf(a,b,z2, np.arange(0,1001,100))
    #ax[1].axis('equal')
    #a3 = ax[0].plot(z3[0], z3[1], 'r*')
#
    #fig.colorbar(a1, ax=ax[0])
    #fig.colorbar(a2, ax=ax[1])
    #fig.colorbar(a3, ax=ax[2])
    #fig.colorbar(a4, ax=ax[1][1])

    #plt.show()



