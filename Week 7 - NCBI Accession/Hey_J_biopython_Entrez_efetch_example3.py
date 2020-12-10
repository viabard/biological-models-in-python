## download a list of nucleotide records from NCBI
## make a list of SeqRecord
## This example uses sequences reported in publication with PMID 22802635
## to see this go to pubmed and search in pubmed for 22802635
## this is an article: Martin et al., 2012. Diversification of complex butterfly wing patterns by repeated regulatory evolution of a Wnt ligand. Proceedings of the National Academy of Sciences 109:12632-12637.
## then display in medline format
## scroll down and find genbank record numbers


from Bio import Entrez
from Bio import SeqIO

## should provide NCBI with my email with making a request
myemail = "hey@temple.edu"     # used to tell NCBI who is inquiring

## list of accession numbers

idlist = ["HE668478 ","HE669520 ","JN944582 ","JN944583 ","JN944584 ","JN944585 ","JN944586 ","JN944587 ","JN944588 ","JN944589"]

## make a call to NCBI for all the  records,  return in genbank format with return mode "text"
myhandle = Entrez.efetch(db="nucleotide", id=idlist,rettype="gb",retmode = "text",email=myemail)

## make a list of SeqRecords using SeqIO.parse
srlist = []
for sr in SeqIO.parse(myhandle, "genbank"):
    srlist.append(sr)
myhandle.close()

print (srlist)
