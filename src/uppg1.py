import numpy as n
import matplotlib.pyplot as plt

#Code by Jonas Danebjer (kin13jda) and Simon Johansson (tna11sjo)

def main():
    plotReflection(1, 1.75)
    plotReflection(1.75, 1)

    plt.show()


def plotReflection(n1, n2):

    a1 = n.array(n.linspace(0.1, n.pi / 2, 1000))
    a2 = n.arcsin(n1 * (n.sin(a1)) / n2)
    print(a2)
    diffs = a1 - a2
    sums = a1 + a2
    Rs = n.abs(n.sin(diffs) / n.sin(sums)) ** 2
    Rp = n.abs(n.tan(diffs) / n.tan(sums)) ** 2
    plt.figure()
    brewster = n.arctan(n2/n1)

    # plt.subplot(2,1,1)
    plt.plot((brewster, brewster), (-100, 100), "y", label='Brewster')
    if n2 < n1:
        totalRef = n.arcsin(n2/n1)
        plt.plot((totalRef, totalRef), (-100, 100),"r" ,label='Total Reflection')

    # plt.xlabel("?")
    # plt.ylabel("Intensity")
    plt.legend(loc=2)
    # plt.subplot(2,1,2)
    plt.plot(a1, Rs, "b" ,label='Rs')
    plt.plot(a1, Rp, "g" ,label='Rp')
    plt.xlabel("Radians")
    plt.ylabel("Reflection")
    plt.legend(loc=2)
    plt.ylim(0,1)



if __name__ == "__main__":
    main()


