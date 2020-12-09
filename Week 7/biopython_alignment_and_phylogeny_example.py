
import os
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline
from Bio.Phylo.Applications import PhymlCommandline


##see clustalw http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc81
# specify the location of the clustalw executable (this depends on your machine)
clustalw_exe_path = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"

#optional check to see if that path exists
assert os.path.isfile(clustalw_exe_path), "Clustal W executable missing"

# create an instance of a Bio.AlignApplication that can be called like a function and runs clustalw
clustalw_cline = ClustalwCommandline(clustalw_exe_path, infile="opuntia.fasta")

clustaltextout, clustaltexterr = clustalw_cline()

if len(clustaltexterr) > 0:
    print("error:\n%s"%(clustaltexterr))
    exit()

print ("clustalw output:\n %s"%(clustaltextout))

# read in the alignment file   and create a MultipleSeqAlignment object
clustalalignment = AlignIO.read("opuntia.aln", "clustal")

#write the alignment to a format that can be read by PhyML

alignout_filename = "opuntia_phylip_alignment.out"
AlignIO.write(clustalalignment,alignout_filename,"phylip-relaxed")

# specify the location of the phyml executable (this depends on your machine)
phyml_exe_path = r"c:\temp\phyml\PhyML-3.1_win32.exe"

#optional check to see if that path exists
assert os.path.isfile(phyml_exe_path), "PhyML executable missing"

# create an instance of a Bio.AlignApplication that can be called like a function and runs phyml
phymlcmd = PhymlCommandline(cmd =phyml_exe_path,input=alignout_filename)
phymltextout,phymltexterr = phymlcmd()

print ("PhyML output:\n%s"%(phymltextout))

from Bio import Phylo
tree_filename = alignout_filename + "_phyml_tree.txt"
tree = Phylo.read(tree_filename, "newick")
print("Ascii tree:\n")
Phylo.draw_ascii(tree)



