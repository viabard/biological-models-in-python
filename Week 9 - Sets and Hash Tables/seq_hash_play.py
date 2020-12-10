"""
    seq_hash_play.py
        a progam to demonstrate the difference between looking things up using a hash function (as used by python dictionaries)
        and looking things up by going through the data one by one.

        works on a file of fasta records

        this program does not do much that is useful

        it is just for demonstrating the value of hash functions for speeding lookups
"""

import random
import time
from Bio import SeqIO   ## frmo BioPython import the SeqIO module. Used to import sequence data into a BioPython class called a SeqRecord


srdic = {}  ## a dictionary to hold SeqRecords made from fasta file
srlist = []  ## a list to hold SeqRecords made from fasta file
srnamelist = []  ## a list to hold seq ids
for record in SeqIO.parse("transcripts_n1000_568.fa.transdecoder.mRNA", "fasta"):
    srname = record.id
    srnamelist.append(srname)
    srlist.append(record)
    srdic[srname] = record ## srname is the key,  record is the value

print("{} records".format(len(srdic))) ## print the number of SeqRecords

## we use the strings in srnamelist to do lookup operations on both srlist  and srdic
## to make the demonstration more realistic, we shuffle the strings in srnamelist
random.shuffle(srnamelist)

## we will time how long the dictionary lookup operations take
numfound_dic = 0
dictimestart = time.clock()
for srname in srnamelist:    ## do a lookup for each name in srnamelist
    srfoundfromdic = srdic[srname]  ## just do a simple assignement on the SeqRecord found using srname
    numfound_dic += 1
dictimestop = time.clock()
dictimespan = dictimestop - dictimestart
print ( "dictionary:  # found, time", numfound_dic,dictimespan)

##now time how long the list lookup operations take
numfound_list = 0
listtimestart = time.clock()
for srname in srnamelist:
    for sr in srlist:
        if sr.id == srname:
            srfoundfromlist = sr
            numfound_list += 1
            ## if found, step out of this inner loop
            break
listtimestop = time.clock()
listtimespan = listtimestop - listtimestart
print ("list:  # found, lookup time", numfound_list,listtimespan)

print ("relative time:  list time / dictionary time  ",listtimespan/dictimespan)



