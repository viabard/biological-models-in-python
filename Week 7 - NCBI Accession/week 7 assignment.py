import os
from Bio import AlignIO
from Bio import Entrez
from Bio import SeqIO
from Bio import Phylo
from Bio.Align.Applications import ClustalwCommandline
from Bio.Phylo.Applications import PhymlCommandline



## should provide NCBI with my email with making a request
myemail = "joshuaschaaf@gmail.com"     # used to tell NCBI who is inquiring

## list of accession numbers

#idlist = ["P10360.1","NP_001122370.1","NP_001071796.1","AEW46988.1","AEW46989.1","AEW46990.1", "P04637.4", "O15350.1", "Q9H3D4.1", "P02340.4", "O88898.1", "Q9JJP2.1", "P79734.1"]
idlist = ["AB082923", "M13874", "U50395.1", "AF475081.1", "AB020761.1", "KU159768.1", "JF792632.2", "AB559569.1", "KX018989.1", "U48957.1", "U48956.1", "U57306.1", "NM_206545.2", "NM_001271820.1", "HM773025.1"]

## make a call to NCBI for all the  records,  return in genbank format with return mode "text"
myhandle = Entrez.efetch(db="nucleotide", id=idlist,rettype="gb",retmode = "text",email=myemail)

## make a list of SeqRecords using SeqIO.parse
srlist = []
for sr in SeqIO.parse(myhandle, "genbank"):
    srlist.append(sr)
myhandle.close()

myfile = open("p53_homologous_unedited.fa", "w+")
SeqIO.write(srlist, "p53_homologous_unedited.fa", "fasta")
copy = myfile.readlines()
myfile.close()

fixedCopy = []
for line in copy:
    if line[0] == ">":
        tempString = ""
        tempString += ">"
        numSpaces = 0
        for i in range(len(line)):
            if numSpaces > 0 and numSpaces < 3:
                if line[i] == " " and numSpaces < 2:
                    tempString += "_"
                else:
                    tempString += line[i]
            if numSpaces > 1 and numSpaces >= 3: 
                tempString += line[i]
            if line[i] == " ":
                numSpaces += 1
            
        fixedCopy.append(tempString)
    else:
        fixedCopy.append(line)
myfile = open("p53_homologous.fa", "w")
myfile.writelines(fixedCopy)
myfile.close()


## make a list of lengths of sequences
lenlist = []
for seq in srlist:
    lenlist.append(len(seq))

print("Lengths:", lenlist)

##see clustalw http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc81
# specify the location of the clustalw executable (this depends on your machine)
which = input("Clustal X or Clustal W? (X shows, W doesn't): ")
if which == 'X':
    clustalw_exe_path = r"C:\Program Files (x86)\ClustalX2\clustalx2.exe"
else:    
    clustalw_exe_path = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"

#optional check to see if that path exists
assert os.path.isfile(clustalw_exe_path), "Clustal W/X executable missing"

# create an instance of a Bio.AlignApplication that can be called like a function and runs clustalw
clustalw_cline = ClustalwCommandline(clustalw_exe_path, infile="p53_homologous.fa")

clustaltextout, clustaltexterr = clustalw_cline()

if len(clustaltexterr) > 0:
    print("error:\n%s"%(clustaltexterr))
    exit()

print ("clustalw output:\n %s"%(clustaltextout))

# read in the alignment file   and create a MultipleSeqAlignment object
clustalalignment = AlignIO.read("p53_homologous.aln", "clustal")

#write the alignment to a format that can be read by PhyML

alignout_filename = "p53_homologous.out"
AlignIO.write(clustalalignment,alignout_filename,"phylip-relaxed")

print("Making tree (takes around 75 seconds): ")

# specify the location of the phyml executable (this depends on your machine)
phyml_exe_path = r"D:\SCHOOL\fall 2020\Biological Models in Python\Week 7\PhyML-3.1_win32.exe"

#optional check to see if that path exists
assert os.path.isfile(phyml_exe_path), "PhyML executable missing"

# create an instance of a Bio.AlignApplication that can be called like a function and runs phyml
phymlcmd = PhymlCommandline(cmd=phyml_exe_path,input=alignout_filename)
phymltextout,phymltexterr = phymlcmd()

print ("PhyML output:\n%s"%(phymltextout))


tree_filename = alignout_filename + "_phyml_tree.txt"
tree = Phylo.read(tree_filename, "newick")
print("Ascii tree:\n")
Phylo.draw_ascii(tree)

