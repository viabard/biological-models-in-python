## Download DNA sequence records from NCBI using Entrez module of BioPython
## This program makes two calls to NCBI and writes each result to a file

from Bio import Entrez
from Bio import SeqIO

## should provide NCBI with my email with making a request
myemail = "hey@temple.edu"     # used to tell NCBI who is inquiring

## accession number for record to get (example is for for Orangutan xq13 locus )
acnumber = "AJ312520"

## file handle where retrieved records will be saved
mygbfile = open("xq13_sequence.fasta","w")

## make a call to NCBI for a record in fasta format
myhandle = Entrez.efetch(db="nucleotide", id=acnumber, rettype="fasta", email=myemail)

## write to the file and close the file
mygbfile.write(myhandle.read())
mygbfile.close()

## close the handle
myhandle.close()

## open file handle where retrieved records will be saved
mygbfile = open("xq13_sequence.gb","w")

## make another call to NCBI for a record in genbank format (include retmode in function call)
myhandle = Entrez.efetch(db="nucleotide", id=acnumber, rettype="gb",retmode="text", email=myemail)
## write to the file and close the file
mygbfile.write(myhandle.read())
mygbfile.close()

## close the handle
myhandle.close()


