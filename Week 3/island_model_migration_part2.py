#implement the Island model of migration
import random
def askForInputs(): #function for getting input
    P = input("This program implements the Island model of migration. It also randomly changes the frequency which the allele is added to the deterministic value.\nInput the frequency of an allele on mainland (P): ")
    p0 = input("Input the frequency of that allele on the island in generation 0 (starting frequency) (p0): ")
    m = input("Input the fraction of all the genes on the island that come from the mainland each generation (m). Maximum value of 0.01: ")
    s = input("Input a random seed number (a positive integer): ")
    return [P, p0, m, s]

inputs = askForInputs()
while True: #casting to correct datatypes, and if it throws an exception, ask for input again
    try:
        s = int(inputs[3])
        P = float(inputs[0]) 
        p0 = float(inputs[1])
        m = float(inputs[2])
        break
    except:
        print("\nError: An input was incorrect.\n")
        inputs = askForInputs()
while True: #making sure that m is between 0.01 and 0
    if type(m) != float:
        try:
            m = float(m)
        except:
            m = input("Error: Input an m value from 0 up to an including 0.01: ")
    elif type(m) == float and m > 0.01 or m <= 0:
        m = input("Error: Input an m value from 0 up to an including 0.01: ")
    elif type(m) == float and m <= 0.01 and m > 0:
        break

    
random.seed(s) #implementing the random number seed

gen = 1 #generation 0 nothing happens
pt = p0

while (pt <= 1.0 and pt >= 0.0 and gen < 10000):
    gen += 1
    pt = m*(P-pt)+pt
    pt += random.uniform(-0.05, 0.05) #adds a uniformly distributed value between -0.05 and 0.05

if gen != 10000:
    if pt >= 1.0:
        print("Allele frequency: ", pt, " --- Allele fixed after", gen, "generations.")
    if pt <= 0.0:
        print("Allele frequency: ", pt, " --- Allele was lost after", gen, "generations.")
else:
    print("After 10000 generations, the allele frequency is: ", pt)