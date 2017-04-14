
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
from matplotlib import cm

def ackley(x, y):
    a = 20
    b = 0.2
    c = 2*np.pi
    print "X: ", x
    print "Y: ",y
    #z = -a*np.exp(-b*np.sqrt((1/y)*x**2))-np.exp((1/y)*np.cos(c*x))+a+np.exp(1)

    A = x**2 + y**2
    B = np.cos(c*x) + np.cos(c*y)
    t1 = - a * np.exp(-b * ((1/2.) * A**(0.5)))
    t2 =  - np.exp((1/2.)*B)
    z = - a * np.exp(-b * ((1/2.) * A**(0.5))) + (- np.exp((1/2.)*B)) + a + np.exp(1)
    #z = a + np.exp(1) + (-a)*np.exp(-b*np.sqrt(x**2+y**2))-np.exp(np.cos(c*x)-y**2-np.sin(c*x))
    print "Z", z
    return z#(-a)*np.exp(-b*np.sqrt((1/y)*x**2))#-np.exp((1/y)*np.cos(c*x))#x**2 + y

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = y = np.arange(-10.0, 10.0, 0.06)
    X, Y = np.meshgrid(x, y)
    zs = np.array([ackley(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.jet,linewidth=0.0055, antialiased=False)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    fig.colorbar(surf, shrink=0.5, aspect=7)
    plt.show()

main()
