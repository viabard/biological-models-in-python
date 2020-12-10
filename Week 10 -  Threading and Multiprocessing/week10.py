import sys, argparse, time, threading
from Bio import SeqIO
from multiprocessing import Process

parser = argparse.ArgumentParser(description='Run week10 Project - Joshua Schaaf') #parsing arguments from command line
parser.add_argument('-t', '--type', type=int, help='1 for threading and 0 for multiprocessing', default=0) #default is multiprocessing
parser.add_argument('-j', '--join',  type=int, help='1 for join() after each job, 0 for join() after all jobs have started', default =0) #default is joining after all the jobs have started
args = parser.parse_args()

isThreading = bool(args.type)
isJoiningAfter = bool(args.join)
fileNames = ["Myotis_aligned_small.fasta", "opuntia.fasta", "porcelaincrab_aligned.fasta", "pyrus.fasta"] #file names


def makeSeqRecords(fileName): 
    """
        Makes seqIO records with SeqIO.parse
    """
    retval = list(SeqIO.parse(fileName, "fasta"))
    return retval

def numberOfRecords(seqRecords):
    """
        Just returns the length of the object passed, wich should be the number of seqRecords (number of sequences)
    """
    return len(seqRecords)

def totalSeqLength(seqRecords):
    """
        Returns the total lengths of all the sequences combined, removes '-' before counting
    """
    retval = 0
    for record in seqRecords:
        retval += len(str(record.seq).replace("-", ""))
    return retval
    

def getNORandTSL(fileName):
    """
        Takes in a file's name, uses seqIO to make seqrecords, gets the number of records and the total sequence length

        Prints the file name, the number of seq records, and the total sequence length to a file (output.txt), as well as to the console
    """
    fileThing = open("output.txt", 'a')
    seqRecords = makeSeqRecords(fileName)
    NOR = str(numberOfRecords(seqRecords))
    TSL = str(totalSeqLength(seqRecords))
    information = "\n\nFile Name: " + fileName + "\nNumber of seq records: " + NOR + ".\nTotal sequence lengths: " + TSL + "."
    print(information)
    fileThing.write(information + "\n")
    fileThing.close()

startTime = time.time() #start time
if __name__ == '__main__':
    """
        Using a list of file names, take in the sequences using seqIO, print the number of sequences in each file, and then print the length of all the sequences combined for each file.
        Uses threading or multiprocessing, depending on what was chosen at command line
        Joins each process after each process starts, or after they all started, depending on what was chosen at command line
    """
    print("Is Threading:", isThreading, "\nIs Joining After:", isJoiningAfter)
    fileThing = open("output.txt", 'w')
    fileThing.write("\nIs Threading:" + str(isThreading) + "\nIs Joining After:" + str(isJoiningAfter))
    fileThing.close()
    fileThing = open("output.txt", 'a')
    if(isThreading):
        t = [] #list of threads
        if isJoiningAfter:
            i = 0
            for f in fileNames:
                t.append(threading.Thread(name="file: " + f, target=getNORandTSL, args = (f,)))
                t[i].start()
                i += 1
            for i in range(len(t)):
                t[i].join()
            print("Time taken: " + str(time.time()-startTime))
            fileThing.write("\nTime taken: " + str(time.time()-startTime))
        else:
            i = 0
            for f in fileNames:
                t.append(threading.Thread(name="file: " + f, target=getNORandTSL, args = (f,)))
                t[i].start()
                t[i].join()
                i += 1
            print("Time taken: " + str(time.time()-startTime))
            fileThing.write("\nTime taken: " + str(time.time()-startTime))
    else:
        procs = []
        if isJoiningAfter:
            for i in range(len(fileNames)):
                proc = Process(target=getNORandTSL, args=(fileNames[i],))
                procs.append(proc)
                proc.start()
            for i in range(len(procs)):
                procs[i].join()
            print("Time taken: " + str(time.time()-startTime))
            fileThing.write("\nTime taken: " + str(time.time()-startTime))
        else:
            for i in range(len(fileNames)):
                proc = Process(target=getNORandTSL, args=(fileNames[i],))
                procs.append(proc)
                proc.start()
                procs[i].join()
            print("Time taken: " + str(time.time()-startTime))
            fileThing.write("\nTime taken: " + str(time.time()-startTime))
