import random
import matplotlib.pyplot as plt
import math

def newr(n):
    """
        n is the number of random values to sum
        return the sum
    """
    sumv = 0.0
    for i in range(n):
        sumv += random.random()
    return sumv

def newrp(n):
    """
        n is the number of random values to sum
        return the sum
    """
    prodv = 1.0
    for i in range(n):
        prodv *= random.random()
    return prodv

seed = 11
random.seed(seed)
numvals = 100000
numtosum = 5
sumvals = 0.0
nlist = []
for i in range(numvals):
##    sumvals += random.random()
    x = newr(numtosum)
##    x = newrp(numtosum)
    nlist.append(x)
##    nlist.append(math.log(x))
    sumvals += x

print(sumvals)
print(sumvals/numvals)

n, bins, patches = plt.hist(nlist, 100, density=True, facecolor='green', alpha=0.75)
plt.show()



