#implement the Island model of migration
def askForInputs():
    """asks for inputs."""
    P = input("This program implements the Island model of migration.\nInput the frequency of an allele on mainland (P): ")
    p0 = input("Input the frequency of that allele on the island in generation 0 (starting frequency) (p0): ")
    m = input("Input the fraction of all the genes on the island that come from the mainland each generation (m): ")
    g = input("Input the number of generations to pass for the calculation for the next allele frequency (g): ")
    return [P, p0, m, g]

inputs = askForInputs()

while True:
    try: #if the inputs are wrong
        P = float(inputs[0])
        p0 = float(inputs[1])
        m = float(inputs[2])
        g = int(inputs[3])
        break
    except: #ask again
        print("\nError: An input was not of the correct type... Make sure to enter numbers for P, p0, m, and an integer for g.\n")
        inputs = askForInputs()

pt = p0
print("Generation 0 allele frequency: %.6f" %pt)

for i in range(int(g)):
    pt = m*(P-pt)+pt
    print("Generation", i + 1, "allele frequency: %.6f" % pt)