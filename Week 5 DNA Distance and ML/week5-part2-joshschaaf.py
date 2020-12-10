import re, math
from scipy.optimize import minimize_scalar

def fixString(string):
    """
        uses regex to remove anything but ATCGN-
    """
    string = re.sub(r"[^A-Z-]", "", string)
    return string

def fixName(string):
    string = re.sub(r"[^A-z_.0-9-]", "", string[12::1])
    return string

def getFastaData2D(fileName):
    """
        returns a list of a text file's contents
    """
    fileThing = open(fileName, "r")
    data = fileThing.readlines()
    fileThing.close()
    retlist = []
    for i in range(len(data)):
        if data[i][0] == ">":
            retlist.append([fixName(data[i]), fixString(data[i+1])])
    return retlist

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
        returns the number of bases that don't match between strings, avoiding '-' and 'N'
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

def calculateP(SD, numDiff):
    """
        returns p of SD and numDiff
    """
    return numDiff/SD

def estimateMutationsPerSite(p):
    """
        estimates mutations per site with K'=(-3/4)Log(1-4p/3)
    """
    return (-3/4)*math.log(1-((4*p)/3))

data = getFastaData2D("Myotis_aligned.fa")
length = len(data[0][1])

def fillMatrix(twoDList, length):
    matrix = []
    for i in range(len(twoDList)):
        temp = []
        for j in range(len(twoDList)):
            SD = determineIdenticalBases(data[i][1], data[j][1])
            if SD[1] == 0:
                temp.append(0)
            else:
                p = calculateP(SD[0]+SD[1], SD[1])
                temp.append(estimateMutationsPerSite(p))
        matrix.append(temp)
    return matrix

def makeLen(string, desiredLength):
    strlen = len(string)
    if strlen >= desiredLength:
        return string[0:desiredLength-1:1] + "|"
    elif strlen == desiredLength:
        return string
    else:
        temp = ""
        for _ in range(desiredLength-strlen):
            temp += " "
        return string + temp

listOfNames = []
for i in range(len(data)):
    listOfNames.append(makeLen(data[i][0], 12))

matrix = fillMatrix(data, length)

def makeMatrix(listOfNames):
    returnMatrix = []
    for i in range(len(matrix)):
        if i == 0:
            returnMatrix.append(" ")
            for k in range(len(listOfNames)):
                returnMatrix.append(listOfNames[k])
        for j in range(len(matrix[i])):
            if j == 0:
                returnMatrix.append(listOfNames[i])
            if matrix[i][j] == 0:
                returnMatrix.append(0)
            else:
                returnMatrix.append(matrix[i][j])
    return returnMatrix
        

fileThing = open("matrix.txt", "w")
for i in range(len(matrix)):
    if i == 0:
        for l in range(12):
            fileThing.write(" ")
        for k in range(len(listOfNames)):
            fileThing.write(listOfNames[k])
            if k == len(listOfNames)-1:
                fileThing.write("\n")
    for j in range(len(matrix[i])):
        if j == 0:
            fileThing.write(listOfNames[i])
        if matrix[i][j] == 0:
            fileThing.write(makeLen("0", 12))
        else:
            fileThing.write(makeLen(str(round(matrix[i][j], 8)), 12))
        if j == len(matrix[i])-1:
            fileThing.write("\n")
fileThing.close()