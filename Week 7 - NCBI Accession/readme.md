# Week 7 - NCBI Accession
NCBI accession numbers for between 8 and 20 NCBI records of homologous sequences and analyze. This assignment was one part.
This worksheet was made and is copyrighted (2020) by Dr. Jody Hey at Temple University

1. Get NCBI accession numbers:
- Get NCBI accession numbers for between 8 and 20 NCBI records of homologous sequences that are each under 50,000 bp in length
- Homologous sequences by definition share a common ancestral sequence. It should be possible to align them and build an evolutionary tree
- One useful method is to search google scholar for evolutionary papaers that include "accession" in the text. These may then give you a list of thee accessions of the sequences they used.

2. Write a python program that:
- downloads your NCBI records using Entrez
- prints the lengths of the sequences to the screen or a file (avoid datasets where the sequences are of very different lengths) 
- writes a file in Fasta format of the records
- aligns the sequences usint clustalW
- build a phylogeny using PhyML
- Writes an ASCII version of the treee to a file