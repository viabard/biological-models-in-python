import numpy as np
import random as rand
import math

seed = input("Input a seed for the random numbers (blank is a random seed): ") 
if seed != "":
    np.random.seed(int(seed))
    rand.seed(int(seed))

def findMean(x): #finding the mean
    s = math.fsum(x)
    return s/(len(x))

def findVariance(x): #finding the variance
    s = findMean(x)
    s2 = 0
    for i in x: #for every float in x
        s2 += pow((i - s), 2) #add it to s2
    return (s2/(len(x) - 1))

def listToString(list):
    retval = ""
    for i in range(len(list)):
        retval += str(list[i])
    return retval

poisson = np.random.poisson(lam=5, size=1000)
exponential = [rand.expovariate(0.5) for i in range (1000)]
normal = [rand.gauss(10, 5) for i in range(1000)]

poisson_mean = findMean(poisson)
exponential_mean = findMean(exponential)
normal_mean = findMean(normal)

poisson_variance = findVariance(poisson)
exponential_variance = findVariance(exponential)
normal_variance = findVariance(normal)

poisson_list = ["Poisson -- Expected Mean: ", 5, " | Actual Mean: ", poisson_mean, " | Expected Variance: ", 5, " | Actual Variance: ", poisson_variance]
exponential_list = ["\nExponential -- Expected Mean: ", 1/0.5, "  | Actual Mean: ", exponential_mean, " | Expected Variance: ", 1/(0.5**2), "| Actual Variance: ", exponential_variance]
normal_list = ["\nNormal -- Expected Mean: ", 10, " | Actual Mean: ", normal_mean, " | Expected Variance: ", 5**2, " | Actual Variance: ", normal_variance]

file_thing = open("distribution_expected_and_actual.txt", "w")
file_thing.write(listToString(poisson_list))
file_thing.write(listToString(exponential_list))
file_thing.write(listToString(normal_list))
file_thing.close()

print(listToString(poisson_list))
print(listToString(exponential_list))
print(listToString(normal_list))

file_thing