import random
print("This program simulates an 'evolution' of sorts. It will create a random string and replace each letter at a frequency you choose. It will try and get the string as close to \"methinks it is like a weasel\" as it can (Idea of Richard Dawkins): ")

def getParams():
    """
        Get the parameters from the user:
        Probability, # of offspring, random number seed, and generation 'cap'
    """
    while True:
        retval = []
        retval.append(input("Enter the probability of making a mistake for each character: "))
        retval.append(input("Enter the number of 'offspring' made each generation: "))
        retval.append(input("Enter a seed for random: "))
        retval.append(input("Enter how many generations you are willing to go through: "))
        try:
            retval[0] = float(retval[0])
            retval[1] = int(retval[1])
            retval[3] = int(retval[3])
            break
        except:
            print("\nPlease enter a decimal value for probablity, and an integer value for number of offspring...\n")
    return retval

inputs = getParams()
random.seed(inputs[2])
stringThing = "methinks it is like a weasel"

def convertToSpaces(string):
    """
        Converts '{' to ' ' in a given string and returns the new string
    """
    retval = ""
    for i in range(len(string)):
        if string[i] == "{":
            retval += " "
        else:
            retval += string[i]
    return retval

def getRandomString(length):
    """
        Creates a random string that is 'length' long
    """
    retval = ""
    for i in range(length):
        retval += chr(random.randint(97,123))
    retval = convertToSpaces(retval)
    return retval

def mutate(original, probability):
    """
        Mutates the given string by looping over the characters in the string, and replacing with a random character based on the given probability.
    """
    retval = ""
    for i in range(len(original)):
        thisRandom = random.random()
        while thisRandom == probability:
            thisRandom = random.random()
        if thisRandom < probability:
            retval += convertToSpaces(chr(random.randint(97,123)))
        else:
            retval += original[i]
    return retval

def gettingCloseness(string):
    """
        Returns a value that increases with how many characters match between the given string and the 'target' string.
    """
    retval = 0
    for i in range(len(stringThing)):
        if stringThing[i] == string[i]:
            retval += 1
    return retval

def createGenerationAndChooseBest(original, offspring, probability):
    """
        Uses a string, the number of offspring per generation, and the probability of mutation:
            Stores mutated children in a 2D array, next to their compared scores...
            Then takes the best child based off the compared score.
            Compares that best child's score to the original string.
            Returns the highest scoring string.
    """
    di = []
    for i in range(offspring):
        temp = mutate(original, probability)
        tempnum = gettingCloseness(temp)
        di.append([tempnum, temp])
    bestString = ""
    bestNum = 0
    for i in range(len(di)):
        if bestNum <= di[i][0]:
            bestNum = di[i][0]
            bestString = di[i][1]
    original_num = gettingCloseness(original)
    if bestNum >= original_num:
        return bestString
    else:
        return original

random_string = getRandomString(len(stringThing)) #creating the original random string
generationsAllowed = inputs[3]
gen = 0

#main loop
for i in range(generationsAllowed): #until the chosen generation
    if gen == 0: #the first generation
        print("Generation: ", gen, "| ", random_string)
    random_string = createGenerationAndChooseBest(random_string, inputs[1], inputs[0])
    gen += 1
    if random_string == stringThing: #checks to see if the best mutated string is the target sequence
        print("Generation: ", gen, "| ", random_string)
        break
    if gen % (generationsAllowed/50) == 0: #prints 20 times, no matter how large the generations
        print("Generation: ", gen, "| ", random_string)

input("") #doesn't close a cmd when done