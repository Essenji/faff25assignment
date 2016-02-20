import matplotlib as mp
import numpy as n
import matplotlib.pyplot as plt


def main():
    L = n.array([1, 0.1, 0.01, 0.001])
    x = [n.linspace(-0.02*i, 0.02*i, 1000) for i in L]
    N = 2
    for index, i in enumerate(L):
        plt.subplot(2,2,1+index)
        plt.plot(x[index], fraunhofer(x[index], i))
        plt.plot(x[index], fresnel(x[index], i, N))

    plt.show()
    # plt.subplot(2,2,1)
    # plt.plot(x, fraunhofer(x, 1), label="Distance 1m")
    # plt.plot(x, fresnel(x, 1, N), label="Distance 1m")
    # x = n.linspace(-0.001, 0.001, 1000)
    # plt.subplot(2,2,2)
    # plt.plot(x, fraunhofer(x, 0.1))
    # plt.plot(x, fresnel(x, 0.1, N))
    # x = n.linspace(-0.0001, 0.0001, 1000)
    # plt.subplot(2,2,3)
    # plt.plot(x, fraunhofer(x, 0.01))
    # plt.plot(x, fresnel(x, 0.01, N))
    # x = n.linspace(-0.00001, 0.00001, 1000)
    # plt.subplot(2,2,4)
    # plt.plot(x, fraunhofer(x, 0.001))
    # plt.plot(x, fresnel(x, 0.001, N))
    # plt.show()


def fraunhofer(x, L):
    hypot = n.sqrt(x**2+L**2)
    beta = n.pi*100e-6/632e-9*x/hypot
    return (n.sin(beta)/beta)**2


def fresnel(x, L, N):
    d = 100e-6/N
    hypot = n.sqrt(x**2+L**2)
    gamma = n.pi*d/632e-9*x/hypot
    print((n.sin(N*gamma)/n.sin(gamma))**2)
    return (n.sin(N*gamma)/n.sin(gamma))**2


main()