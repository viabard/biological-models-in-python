def makeLen(string, desiredLength): #formatting
    """
        Makes a string a desired length by adding speces to the end, or cutting it off and replacing the last with a '|'

        string: string that will be changed
        desiredLength: the desired length of the string
    """
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

data = [] 
with open("genelist.txt", 'r') as x: #read in all the lines into a list
    data = x.readlines()
    x.close()

twoDArray = [] #2Darray
temp = [] 
for i in range(len(data)):
    if ("Species" in data[i]) and i != 0: #if it is the species line (and not the first line)
        twoDArray.append(temp.copy()) #append a copy of temp to 2Darray
        temp.clear() #clear temp
    elif i == len(data)-1: #if it is the last line
        temp.append(data[i].strip("\n")) #append to temp (strip newline)
        twoDArray.append(temp.copy()) #append to 2Darray
    temp.append(data[i].strip("\n")) #basically else, append to temp (strip newline)

fileThing = open("week9part1output.txt", 'w')
speciesList = []
fileThing.writelines("Species | Genes | Unique Genes" + "\n") #header
print("Species | Genes | Unique Genes")
for species in twoDArray: #print to a file, as well as to the screen
    print(species[0], end = ": | ")
    fileThing.writelines(species[0] + ": | ")
    speciesList.append(species.pop(0)) #make a species list while removing them from 2Darray
    print(len(species), "|", len(set(species))) #popped species name so just genes
    fileThing.writelines(str(len(species)) + " | " + str(len(set(species))) + "\n")


"""
    Making a matrix that compares each species to every species, finding the gene names they have in common
"""
matrix = []
length = 11
matrix.append([makeLen("", length)])
for i in range(len(twoDArray)):
    matrix[0].append(makeLen(speciesList[i], length))

for i in range(len(twoDArray)):
    temp2 = []
    temp2.append(makeLen(speciesList[i], length))
    for j in range(len(twoDArray)):
        temp = set(twoDArray[i])
        intersect = temp.intersection(set(twoDArray[j]))
        if j != len(twoDArray)-1:
            temp2.append(makeLen(str(len(intersect)), length))
        else: 
            temp2.append(makeLen(str(len(intersect)), length))
        if j == len(twoDArray)-1:
            matrix.append(temp2)

matrixStart = "\nNumber of gene names that are unique for species i that are also among the unique names for species j...\n"
print(matrixStart, end="")
fileThing.write(matrixStart)

for i in range(len(matrix)): #formatting! (printing matrix to file)
    for j in range(len(matrix[i])):
        if j == len(matrix[i])-1:
            print(matrix[i][j])
            fileThing.write(matrix[i][j] + "\n")
        else:
            print(matrix[i][j], end = "")
            fileThing.write(matrix[i][j])
fileThing.close()