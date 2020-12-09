file_thing = open("Dromel_Adh.fasta", "r") #opens the fasta file
header = file_thing.readline() #stores the single line header
file_read_lines = file_thing.readlines() #stores the rest of the file with readlines()
file_thing.close() #closes file pointer

file_string = ""
for i in file_read_lines: #for each item (line) in file_read_lines...
    file_string += str(i).strip("\n") #...store add the stripped version of the line to a string
gcaa_count = 0

def findSeqCount(file_string, sequence_to_search): #function to find how many times the sequence appears
    retval = 0
    for i in range(len(file_string) - len(sequence_to_search) + 1): #for i in range of the length of the string, minus the sequence to search length to avoid looking past the list
        count = 0
        for j in range(len(sequence_to_search)): #for i in range length of sequence that is being searched for...
            if(sequence_to_search[j] == file_string[i + j]): #compare the sequence, and the sequence being searched for
                count += 1
                if count == 4:
                    retval += 1
            else: #if its not, just move to the next nucleotide
                break
    return retval

def reverseCompliment(sequence_to_search): #function to make the reverse compliment of a sequence
    reverse = sequence_to_search[::-1] #reverses the string given
    retval = "" #new string instead of modifying original string

    for i in range(len(reverse)):
        if reverse[i] == "G":
            retval += "C"
        elif reverse[i] == "C":
            retval += "G"
        elif reverse[i] == "A":
            retval += "T"
        elif reverse[i] == "T":
            retval += "A"
    return retval

reverse_compliment = reverseCompliment(file_string) #calling reverse compliment function

gcaa_count = findSeqCount(file_string, "GCAA") #calling seq count on original sequence
rc_gcaa_count = findSeqCount(reverse_compliment, "GCAA") #calling seq count on reverse compliment
print("Regular Count: ", gcaa_count, "\nReverse-Compliment Count: ", rc_gcaa_count) #printing to the screen

file_thing = open("reverse_compliment.txt", "w") #writing the reverse compliment to a file
file_thing.write(reverse_compliment)
file_thing.close()