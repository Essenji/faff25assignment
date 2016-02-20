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

def plotLensDistance(h):
    r = 0.15
    n1 = 1
    n2 = 1.5
    # h =  np.linspace(0, 0.05, 2000)
    a2= asin(n1/n2 * h/r)
    a1= asin(h/r)
    df = r*sin(a2)/sin(a1-a2)

    dx = r+df
    plt.plot(h,dx, "b")


def plotChromaticAbb(h, n2):
    r = 0.15
    n1 = 1
    # n2 = 1.5
    # h =  np.linspace(0, 0.05, 2000)
    a2= asin(n1/n2 * h/r)
    a1= asin(h/r)
    df = r*sin(a2)/sin(a1-a2)

    dx = r+df
    # plt.plot(n2,dx, "b")
    return dx

def plotParaxialDistance():
    # Approximating sinus x = x
    # H becomes a constant factor in the end.
    r = 0.15
    n1 = 1
    n2 = 1.5
    h =  np.linspace(0, 0.05, 2000)
    a2= n1/n2 * h/r
    a1= h/r
    df = r*a2/(a1-a2)

    dx = r+df
    plt.plot(h,dx, "g")



def plotBK7(wl):
    a1 = 2.271176
    a2 = -9.700709e-3
    a3 = 0.0110971
    a4 = 4.622809e-5
    a5 = 1.616105e-5
    a6 = -8.285043e-7

    nsq = a1+ a2*wl**2+a3*wl**-2+a4*wl**-4+a5*wl**-6+a6*wl**-8
    # print(nsq)
    n = np.sqrt(nsq)
    # plt.plot(wl, n)
    return n

def intensity(x, l):
    b = 100e-6
    lmbd = 632e-9
    sintheta = x / np.sqrt(x**2 + l**2)
    beta = pi*b/lmbd *sintheta
    intens = (sin(beta)/beta)**2
    return intens



def intensitySlits(x, l, n):

    b = 100e-6
    d = b/n
    lmbd = 632e-9
    sintheta = x / np.sqrt(x**2 + l**2)
    gamma = pi*d/lmbd *sintheta
    intens = (sin(n*gamma)/sin(gamma))**2
    return intens

def main():
    # plt.subplot(2, 1, 1)
    # plotReflection(1, 1.75)
    # plt.subplot(2, 1, 2)
    # plt.subplot(2,1,1)
    #    plt.show()


    ##Upg2
    # plotLensDistance(np.linspace(0, 0.05, 2000))
    # plotParaxialDistance()
    # plt.show()

    #Upg3
    # plotBK7(np.linspace(0.4,0.7,300))
    # plt.show()

    #Upg 4
    # wl = np.linspace(0.4, 0.7, 300)
    # n = plotBK7(wl)
    # # print(n)
    # f = plotChromaticAbb(0.025, n)
    # plt.plot(wl,f, "g")
    # plt.show()
    nbrslits = 10;
    points = np.linspace(-0.02, 0.02, 20000)
    plt.subplot(4, 1, 1)
    plt.plot(points, intensity(points, 1), label="1m")
    plt.plot(points, intensitySlits(points, 1,nbrslits), label="1m")

    plt.subplot(4, 1, 2)
    points = np.linspace(-0.002, 0.002, 20000)

    plt.plot(points, intensity(points, 0.1), label="0.1m")
    plt.plot(points, intensitySlits(points, 0.1,nbrslits), label="0.1m")

    plt.subplot(4, 1, 3)
    points = np.linspace(-0.0002, 0.0002, 20000)

    plt.plot(points, intensity(points, 0.01), label="0.01m")
    plt.plot(points, intensitySlits(points, 0.01,nbrslits), label="0.01m")

    plt.subplot(4, 1, 4)
    points = np.linspace(-0.00002, 0.00002, 20000)

    plt.plot(points, intensity(points, 0.001), label="0.001m")
    plt.plot(points, intensitySlits(points, 0.001,nbrslits), label="0.001m")



    plt.show()



if __name__ == "__main__":
    main()

