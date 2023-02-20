from matplotlib import pyplot as plt 
import numpy as np

def convex_set():
    plt.axis("off")

    x = np.linspace(-np.pi,np.pi,100)
    plt.plot(np.cos(x),np.sin(x),"b")
    plt.show()
    

def non_convex_set():
    plt.axis("off")

    x = np.linspace(-1,1,100)
    plt.plot(x,x**3,"b")
    plt.plot(100*[1],np.linspace(-1,1,100),"b")
    plt.plot(x,[-1]*100,"b")
    plt.show()
    
non_convex_set()