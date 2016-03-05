import matplotlib as mp
import numpy as n
import matplotlib.pyplot as plt


def main():
    """
    This program calculates the Fraunhofer and Fresnel graphs given different distances L. Fresnel uses N as number of slits.
    :return:
    """
    L = n.array([1, 0.1, 0.01, 0.001]) # Distance from screen to slit
    N = 20 # Number of slits (only used in Fresnel)
    x = [n.linspace(-0.02*i, 0.02*i, 1000) for i in L]
    for index, i in enumerate(L):
        plt.subplot(2,2,1+index)
        plt.plot(x[index], fraunhofer(x[index], i), label="Fraunhofer")
        plt.plot(x[index], fresnel(x[index], i, N), label="Fresnel")
        plt.xlabel("x")
        plt.ylabel("Intensity")
        plt.axis([-0.02*i,0.02*i, 0, 1])
        plt.legend()
    plt.show()


def fraunhofer(x, L):
    """
    :param x: Point on screen
    :param L: Distance between slit and screen
    :return: Returns the intenstiy function computed with Fraunhofer approximation
    """
    hypot = n.sqrt(x**2+L**2)
    beta = n.pi*100e-6/632e-9*x/hypot
    return (n.sin(beta)/beta)**2


def fresnel(x, L, N):
    """
    :param x: Point on screen
    :param L: Distance between slits and screen
    :param N: Number of slits
    :return: Returns the intensity function
    For every point on the screen and for every slit the complex contribution is added.
    """
    d = 100e-6/N
    wl = 632e-9
    total = n.zeros_like(x, dtype=n.complex64)
    for index, Point in enumerate(x):
        for i in range(-N // 2, N//2):
            hypot = n.sqrt(L**2+(abs(Point)+i*d)**2)
            phase = 2*n.pi*(hypot % wl)/wl
            total[index] += n.exp(phase * 1j)/N
    return n.abs(total)



main()