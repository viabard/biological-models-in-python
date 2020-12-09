import numpy as np
import random as rand

fileThing = open("11.1-output.txt", 'w')


#creates 2D array with random floating point values between 0 and 10 and prints the integer parts of the array
rowSize = 7
columnSize = 10
zeroToTenNumpyMatrix = np.random.rand(rowSize, columnSize)*10
integerParts = zeroToTenNumpyMatrix.astype(int)
fileThing.write("Integer Matrix: \n" + str(integerParts))
fileThing.write("\n\n")
#use np.arange() to make a 1D array with 12 elements, then use in place conditions to change the array so that all elements greater than 3 and less than 9 aree replaced by their negative values
secondPart = np.arange(12)
i = (secondPart>3)&(secondPart<9)
secondPart[i] *= -1
fileThing.write("Replaced: " + str(secondPart))

fileThing.close()