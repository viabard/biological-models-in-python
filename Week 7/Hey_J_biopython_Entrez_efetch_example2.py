## Download DNA sequence records from NCBI using Entrez module of BioPython
## This program makes just one call to NCBI and saves the result as a SeqRecord

from Bio import Entrez
from Bio import SeqIO

## should provide NCBI with my email with making a request
myemail = "hey@temple.edu"     # used to tell NCBI who is inquiring

## accession number for record to get (example is for for Orangutan xq13 locus )
acnumber = "AJ312520"

## make a call to NCBI for a record in genbank format (include retmode in function call)
myhandle = Entrez.efetch(db="nucleotide", id=acnumber, rettype="gb",retmode="text", email=myemail)

## read into a SeqRecord
myseqrec  = SeqIO.read(myhandle,"genbank")

## close the handle
myhandle.close()

## open file handle where retrieved records will be saved
mygbfile = open("xq13_sequence_a.gb","w")
SeqIO.write(myseqrec,mygbfile,"genbank")
mygbfile.close()


## open file handle where retrieved records will be saved
mygbfile = open("xq13_sequence_a.fas","w")
SeqIO.write(myseqrec,mygbfile,"fasta")
mygbfile.close()




