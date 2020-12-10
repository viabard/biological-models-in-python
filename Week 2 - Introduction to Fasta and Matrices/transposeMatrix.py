file_name = input("Text file name with rows and columns of numbers: ") #asks user for input
file_thing = open(file_name, "r") #opens the file with the name provided

large_file_string = file_thing.read() #stores the whole file as a string
file_thing.close() #closes the file pointer

large_file_list = large_file_string.splitlines() #a list of split lines
for i in range(len(large_file_list)):
    large_file_list[i] = large_file_list[i].split() #splitting, but now by spaces, making it a 2D list

def transposeMatrix(x): #function that transposes the matrix
    retval = []
    for i in range(len(x[0])): #for each column the 2D list...
        retval.append([]) #...append an empty list
        for j in range(len(x)): #for each row in the 2D list...
            retval[i].append(x[j][i]) #...append the values to the newest empty list created
    return retval

file_thing = open("matrix_transpose.txt", "w") #file pointer
file_thing.write(str(transposeMatrix(large_file_list))) #writes to the file (must be a string)
file_thing.close() #closes file pointer