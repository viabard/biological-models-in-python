# playing with numpy
import time
import random
import numpy as np

def dotproduct(a,b):
    """
        regular python implementation of dotproduct of two matrices
        each a list of lists.
        a, b are each rectangular lists of lists
        if a has shape x,y and b has shape y,z
        new matrix has shape x,z
    """
    anumrows = len(a)
    anumcols = len(a[0])
    bnumrows = len(b)
    bnumcols = len(b[0])
    assert anumcols == bnumrows
    newm = [[0 for i in range(anumrows)] for j in range(bnumcols)]
    for i in range(anumrows):
        for j in range(bnumcols):
            tempsum = 0.0
            for k in range(anumcols):
                tempsum += a[i][k] * b[k][j]
            newm[i][j] = tempsum
    return newm


# make a stochastic matrix,  each value in each row is non-negative, and all values in each row sum to 1
# compare numpy with regular python for matrix dot product

numtrials = 50
matrixsize = 10

# regular python
starttime = time.time()

nrows = ncols = matrixsize
for trial in range(numtrials):
    mp = []
    for i in range(nrows):
        # build a list of random numbers
        temprow = [random.random() for j in range(ncols)]
        # normalize so the values in the row sum to 1
        mp.append([temprow[j]/sum(temprow) for j in range(ncols)])
        # normalize so the values in the row sum to 1
    mpdotmp = dotproduct(mp,mp)
stoptime = time.time()
print("regular python time: {:.3}".format(stoptime-starttime))




# do it in numpy
starttime = time.time()
for trial in range(numtrials):
    mnp = np.random.rand(matrixsize,matrixsize)
    mnp = mnp/mnp.sum(axis=1,keepdims=1)
    mnp = np.dot(mnp,mnp)
stoptime = time.time()
print("numpy time: {:.3}".format(stoptime-starttime))



mnp = np.array(mp)

# check column and row sums
# to sum 'over' the first axis  (i.e. sum columns)
colsums = mnp.sum(axis=0)
# to sum 'over' the 2nd axis  (i.e. sum rows)
rowsums = mnp.sum(axis=1)


mnpcopy = mnp.copy()
# find the dominant eigenvector by raising the matrix to high powers
for k in range(3):
    mnp = np.dot(mnp,mnp)
    print("power:",2**(k+1),"row 0:",mnp[0])

# now try the linear algebra
from numpy import linalg

print("use matrix_power():",linalg.matrix_power(mnpcopy,8)[0])