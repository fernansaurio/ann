from math import *
#from numpy import *
import numpy as np
import pylab as plt
import matplotlib
matplotlib.use('qt5agg') 

def f(c):
    m = 68.1
    v=40
    t = 10
    g=9.8

    return ( ((g*m) /c) * (1-(e** -( (c*t) /m) ) )-v )

x=np.linspace(0.1,20,100)
plt.plot(x,f(x))
plt.show()

