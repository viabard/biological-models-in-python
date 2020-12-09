import re, math
from scipy.optimize import minimize_scalar

def getFastaData(fileName):
    """
        returns a list of a text file's contents
    """
    fileThing = open(fileName, "r")
    data = fileThing.readlines()
    fileThing.close()
    return data

def checkForNOrGap(character):
    """
        returns True if the character it not '-' or 'N'
        returns False if they are
    """
    if character == "-" or character == "N":
        return False
    else:
        return True

def determineIdenticalBases(string1, string2):
    """
        returns the number of bases that match between strings, avoiding '-' and 'N'
    """
    S = 0
    D = 0
    if len(string1) != len(string2):
        return -1
    for i in range(len(string1)):
        if checkForNOrGap(string1[i]) and checkForNOrGap(string2[i]) :
            if string1[i] == string2[i]:
                S += 1
            else:
                D += 1
    return S, D

def fixString(string):
    """
        uses regex to remove anything but ATCGN-
    """
    string = re.sub(r"[^ATCGN-]", "", string)
    return string

def calculateP(SD, numDiff):
    """
        returns p of length and numDiff
    """
    return numDiff/SD

def estimateMutationsPerSite(p):
    """
        estimates mutations per site with K'=(-3/4)Log(1-4p/3)
    """
    return (-3/4)*math.log(1-(4*p/3))

def probabilityDifferent(K):
    """
        returns the probability that two bases are different
    """
    return (3/4)*(1-math.exp(-4*K/3))


def makeListK(maximum, step, minimum = 0):
    """
        returns a list inclusive between minimum and maximum, by interval step
    """
    retlist = []
    for i in range(1+(int((maximum-minimum)/step)//1)):
        retlist.append(minimum + i*step)
    return retlist

data = getFastaData("data_for_jukes_cantor_exercise.fa")
fileThing = open("S, D, p, K'.txt", "w")
SD = determineIdenticalBases(fixString(data[1]), fixString(data[3]))

def logLikelihood(K, S = SD[0], D = SD[1]):
    """
        K = K
        S = number same
        D = number different

        returns the neagative of log likelihood
    """
    return -1*(D*math.log(probabilityDifferent(K))+S*math.log(1-probabilityDifferent(K)))

def getMultipleLogLikelihood(listK, S = SD[0], D = SD[1]):
    """
        listK = a list of K
        S = number same
        D = number different

        returns a list of all the values of the log likelihood
    """
    retlist = []
    for i in range(len(listK)):
        retlist.append(-1*logLikelihood(listK[i], S, D))
    return retlist

def findHighest(numList, listK):
    """
        numList = list of numbers
        listK = list of K

        returns a tuple of the highest number and its K value
    """
    temp = -10000000000
    K = -1
    for i in range(len(numList)):
        if numList[i] >= temp:
            temp = numList[i]
            K = listK[i]
    return temp, K

fileThing.writelines(["S = " + str(SD[0]) + "\n", "D = " + str(SD[1]) + "\n", "p = " + str(calculateP(SD[0]+SD[1], SD[1])) + "\n", "K' = " + str(estimateMutationsPerSite(calculateP(SD[0]+SD[1], SD[1]))) + "\n" + "\n"])

ListK = makeListK(1, 0.000001, minimum=0.000001)

highest = findHighest(getMultipleLogLikelihood(ListK),ListK)
fileThing.writelines(["Brute Force: Largest Log-Likelihood = " + str(highest[0]) + " || ", "K = " + str(highest[1]) + "\n\n"])
fileThing.write("Scipy minimize_scalar Output for Negative Log-Likelihood: \n" + str(minimize_scalar(logLikelihood, bounds = ([0.00001, 1]), method='bounded')))
