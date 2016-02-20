import matplotlib as mp
import numpy as n
import matplotlib.pyplot as plt


def main():
    plotReflection(1, 1.75)
    plotReflection(1.75, 1)
    plt.show()


def plotReflection(n1, n2):
    a1 = n.array(n.linspace(0.1, n.pi / 2, 1000))
    a2 = n.arcsin(n1 * (n.sin(a1)) / n2)
    diffs = a1 - a2
    sums = a1 + a2
    Rs = n.abs(n.sin(diffs) / n.sin(sums)) ** 2
    Rp = n.abs(n.tan(diffs) / n.tan(sums)) ** 2
    plt.figure()
    plt.plot(a1, Rs)
    plt.plot(a1, Rp)



if __name__ == "__main__":
    main()


