__author__ = 'tank'
import matplotlib.pyplot as plt
import numpy as np

from numpy import arcsin  as  asin , sin,  tan

from math import pow
from math import pi

def plotReflection(n1, n2):
    a1 = np.linspace(0, pi/2, 590)
    a2 = np.arcsin(sin(a1) * n1/n2)
    print(a2)
    rs = abs(sin(a1-a2)/sin(a1+a2))**2
    rp = abs(tan(a1-a2)/tan(a1+a2))**2

    plt.plot(np.rad2deg(a1),rs, "b")
    plt.plot(np.rad2deg(a1),rp, "r")



def main():
    plt.subplot(2, 1, 1)
    plotReflection(1, 1.75)
    plt.subplot(2, 1, 2)

    plotReflection(1.75, 1)
    plt.show()
if __name__ == "__main__":
    main()