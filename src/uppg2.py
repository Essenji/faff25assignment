import matplotlib as mp
import numpy as n
import matplotlib.pyplot as plt


def main():
    #plotDistanceInLens(1.5)
    #plotDistanceInLensApprox(1.5)
    #plt.ylim(0.430,0.460)
    #plt.show()
    plotDistanceInLensbk7(plotbk7())
    plt.show()


def plotDistanceInLens(n2):
    n1 = 1
    R = 0.15
    h = n.linspace(0, 0.05 , 1000)
    a1 = n.sin(h/R) #Trig ger infallande vinkel
    a2=n.arcsin(n1/n2*n.sin(a1))
    gamma = a1-a2 #gamma = 180 - (180 - a1) - a2
    f2=R*n.sin(a2)/n.sin(gamma)
    #plt.figure()
    plt.plot(h, f2+R)

def plotDistanceInLensbk7(n2):
    n1 = 1
    R = 0.15
    h = 0.025
    a1 = n.sin(h/R)
    a2=n.arcsin(n1/n2*n.sin(a1))
    gamma = a1-a2
    f2=R*n.sin(a2)/n.sin(gamma)
    plt.figure()
    plt.plot(n2, f2+R)

def plotDistanceInLensApprox(n2):
    n1 = 1
    R = 0.15
    h = n.linspace(0, 0.05 , 1000)
    a1 = h/R
    a2=n1/n2*a1
    gamma = a1-a2
    f2=R*a2/gamma
    #plt.figure()
    plt.plot(h, f2+R)


def plotbk7():
    wl = n.linspace(0.4, 0.7 , 1000)
    plt.figure()
    bk7 = calcbk7(wl)
    plt.plot(wl, bk7)
    plt.show()
    return bk7


def calcbk7(wl):
    a1 = 2.271176
    a2 = -9.700709*10**(-3)
    a3 = 0.0110971
    a4 = 4.622809 * 10**(-5)
    a5 = 1.616105 * 10**(-5)
    a6 = -8.285043 * 10**(-7)
    q=a1 + a2 * wl ** 2 + a3 * wl ** (-2) + a4 * wl ** (-4) + a5 * wl ** (-6) + a6 * wl ** (-8)
    return n.sqrt(q)

main()