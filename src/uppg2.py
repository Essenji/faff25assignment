import matplotlib as mp
import numpy as n
import matplotlib.pyplot as plt


def main():
    plotDistanceInLens(1.5)



def plotDistanceInLens(n2):
    n1 = 1
    R = 0.15
    h = n.array(n.linspace(0, 0.05 , 1000))
    a1 = n.sin(h/R)
    a2=n.arcsin(n1/n2*n.sin(a1))
    gamma = a1-a2 #gamma = 180 - (180 - a1) - a2
    f2=R*n.sin(a2)/n.sin(gamma)
    plt.plot(h, f2+R)
    plt.show()


main()