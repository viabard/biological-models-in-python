
def hashCode(string):
    """
        takes in a string and creates a hashcode using the ord() of each character and some simple arithmetic. hashnumber is an integer
    """
    retstring = 0
    i = 0
    for char in string:
        i += 1
        c = 31
        retstring += (ord(char)*ord(char))**c*i
    return int(retstring)%1000000

data = [] #holds the data from the file
with open("Myotis_aligned.fa", 'r') as x: #read in all the lines into a list
    data = x.readlines()

names = [] #a list of all the names of species
accessionNumbers = [] #a list of all the accession numbers

for line in data: #getting the names and accession numbers
    count = 0
    if line[0] == '>':
        tempLine = ""
        name = ""
        for char in line:
            if char != '\n':
                if count <= 0 and char != '_' and char != '>':
                    tempLine += char
                if count > 0:
                    name += char
                if char == '_':
                    count += 1
        names.append(name)
        accessionNumbers.append(tempLine)

myotisseqs = {} #a dictionary that will have the hash numbers of accession numbers as keys, and the species names as values
keys = [] #a list of the keys
for i in range(len(accessionNumbers)): #gets a list of the keys, as well as adds to the dictionary
    myotisseqs[hashCode(accessionNumbers[i])] = names[i]
    keys.append(hashCode(accessionNumbers[i])) 

fileThing = open("week9part2output.txt", 'w')

for number in accessionNumbers: #prints to the screen and to a file: the accession numbers followed by the species names (retrived from the dictionary)
    print("Accession Number: " + number + "\t\tSpecies: " + myotisseqs[hashCode(number)])
    fileThing.write("Accession Number: " + number + "\t\tSpecies: " + myotisseqs[hashCode(number)] + '\n')

fileThing.close()