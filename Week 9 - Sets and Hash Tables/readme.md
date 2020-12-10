# Week 9 - Sets and Hash Tables
Two parts, first working with sets, and then working with hash tables.
This worksheet was made and is copyrighted (2020) by Dr. Jody Hey at Temple University

1. Part 1:
The file genelist.txt contains a long list of gene names for 14 species. Each list is headed by 'Species_#' where " ranges from 0 to 14. All the genes for species 0 are between Species_0 and Species_1.

Write a program that:
- Has the count of the total number of gene names for each speices
- Has the number of unique gene names for each speices
- Gets the number of gene names that are unique for speices i that are also among the unique names for species j. Do this for all pairs and print out values in a 14x14 table. Then have the program generate a matrix, with 14 rows and 14 columns with all pairs and write this to the file.

2. Part 2:
Write a program that implements a kind of dictionary using a hash function (that you will write) that returns indices of a list, which in turn holds the data.
- The hash function must match the length of your list, so that every call to the has function returns a valid index. 
- For this assignment, this number can be much larger than the amoung of data, but not larger than 1 million
- The data values will be species names made by reading in Myotis_aligned.fa
    - This has 75 sequences, so your list must have a length of at least 75
- The keys will be the accession numbers obtained from reading in the fasta file
- If your list is myotisseqs and your hash unction is called myhash() then the location of the data for the key will be found at myotisseqs[myhash(key)]
- The program will:
    - Read in the data file and store the sequences in your list using your hash function
    - Also put the key values (your accession numbers) in a seperate list
    - loop over your list of accession numbers and for each accession number print to the screen and write to a file the accession number and the species named returned from the list using your hash function