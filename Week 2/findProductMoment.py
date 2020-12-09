import math, io


user_input = input("Name of file with two columns of numbers: ") 
file_thing = open(user_input, "r")

both_columns = file_thing.read()
file_thing.close()

both_columns_split = both_columns.split()
columna = [] #first column
columnb = [] #second column
for i in range(len(both_columns_split)):
    if i % 2 == 0: #first column (even, list starts at 0)
        columna.append(float(both_columns_split[i]))
    if i % 2 == 1: #second column (odd)
        columnb.append(float(both_columns_split[i]))

def findMean(x): #finding the mean
    s = math.fsum(x)
    return s/(len(x))

def findStandardDeviation(x): #finding the standard deviation
    s = findMean(x)
    s2 = 0
    for i in x: #for every float in x
        s2 += pow((i - s), 2) #add it to s2
    return math.sqrt((s2/(len(x) - 1)))

def findProductMoment(x, y): #getting the product moment
    mx = findMean(x)
    my = findMean(y)
    sdx = findStandardDeviation(x)
    sdy = findStandardDeviation(y)
    psd = sdx * sdy
    n_sum_xy = 0
    for i in range(len(x)): #for i in length of the list (both lists should be the same size)
        n_sum_xy += (x[i] - mx)*(y[i] - my)
    return (((1/(len(x) - 1))*n_sum_xy)/psd)

file_thing = open("pmc_calc.txt", "w+")
file_thing.write(str(findProductMoment(columna, columnb)))
file_thing.close()