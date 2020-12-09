import re, math

def fixString(string):
    """
        uses regex to remove anything but ATCGN-
    """
    string = re.sub(r"[^A-Z-]", "", string)
    string = string.strip("\n")
    return string

def fixName(string):
    string = re.sub(r"[^A-z_.0-9-]", "", string)
    string = string.strip("\n")
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


def getDistancesWithNames(twoDList):
    """
    Returns a 'matrix', or a 2Dlist of [name1, name2, k value]
    """
    matrix = []
    for i in range(0,len(twoDList)):
        for j in range(len(twoDList) - len(twoDList) + i):
            SD = determineIdenticalBases(data[i][1], data[j][1])
            temp = []
            if SD[1] != 0:
                p = calculateP(SD[0]+SD[1], SD[1])
                temp.append(data[i][0])
                temp.append(data[j][0])                
                temp.append(estimateMutationsPerSite(p))
                matrix.append(temp)
    return matrix

def findSmallest(distancesWithNames):
    """
    Takes a 'matrix' of distances with names and returns the index of the smallest k value
    """
    smallest = distancesWithNames[0][2]
    smallestIndex = -1
    for i in range(len(distancesWithNames)):
        if smallest >= distancesWithNames[i][2]:
            smallest = distancesWithNames[i][2]
            smallestIndex = i
    return smallestIndex

def newMatrixWithSmallest(distancesWithNames, smallestIndex, beforeDistance = 0):
    """
    distancesWithNames: a 2Dlist comprised of [name1, name2, k value]
    smallestIndex: the index of the distancesWithNames that has the smallest k value
    CURRENTLY UNUSED -- beforeDistance: the distance of the previous
    """
    smallestName1 = distancesWithNames[smallestIndex][0]
    smallestName2 = distancesWithNames[smallestIndex][1]
    temp = []
    newMatrix = []
    #oldDistance = distancesWithNames[smallestIndex][2]
    distancesWithNames.pop(smallestIndex)
    i = 0
    while i < len(distancesWithNames):
        if smallestName1 in distancesWithNames[i]:
            temp.append(distancesWithNames.pop(i))
            i -= 1
        elif smallestName2 in distancesWithNames[i]:
            temp.append(distancesWithNames.pop(i))
            i -= 1
        if i == len(distancesWithNames)-1:
            break
        i += 1
    i = 0
    while i < len(temp):
        if smallestName1 in temp[i]:
            distance1 = -1
            distance2 = -1
            searching = ""
            if smallestName1 == temp[i][0]:
                searching += temp[i][1]
            else:
                searching += temp[i][0]
            distance1 = temp[i][2]
            temp.pop(i)
            i -= 1
            for j in range(len(temp)):
                if smallestName2 and searching in temp[j]:
                    distance2 = temp[j][2]
                    temp.pop(j)
                    if j <= i:
                        i -= 1
                    break
            extraTemp = []
            extraTemp.append("(" + smallestName1 + "," + smallestName2 + ")")
            #extraTemp.append("(" + smallestName1 + ":" + str((oldDistance/2) - beforeDistance) + "," + smallestName2 + ":" + str((oldDistance/2) - beforeDistance) + ")")
            extraTemp.append(searching)
            extraTemp.append((distance1+distance2)/2)
            newMatrix.append(extraTemp)
        i += 1
    while len(distancesWithNames) != 0:
        newMatrix.append(distancesWithNames.pop(0))
    return newMatrix, beforeDistance

def makeNewickList(distancesWithNames):
    """
    Returns a Newick-string using UPGMA
    """
    i = 0
    oldDistance = 0
    while len(distancesWithNames) > 1:
        smallestindex = findSmallest(distancesWithNames)
        distancesWithNames, oldDistance = newMatrixWithSmallest(distancesWithNames, smallestindex, beforeDistance=oldDistance)
        i+=1
    retString = "(" + distancesWithNames[0][0] + "," + distancesWithNames[0][1] + ");"
    return retString

data = getFastaData2D("Myotis_aligned.fa") #Currently uses Myotis_aligned.fa, but takes in any fasta file that **DOESN'T HAVE EXACT DUPLICATE SEQUENCES**
matrix = getDistancesWithNames(data)
#tester = [["A", "B", 20], ["A", "C", 60], ["A", "D", 100], ["A", "E", 90], ["B", "C", 50], ["B", "D", 90], ["B", "E", 80], ["C", "D", 40], ["C", "E", 50], ["D", "E", 30]] #a test distancesWithNames


filething = open("newick_string_output.txt", "w")
final = makeNewickList(matrix)
filething.writelines(final)
filething.close()
print(final)