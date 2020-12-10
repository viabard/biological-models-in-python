# Week 2 - Product Moment Correlation, Matrices, Introduction to .fasta
This week there were three parts for the assignment dealing with PMC, matrices, and an introduction to .fasta.
This worksheet was made and is copyrighted (2020) by Dr. Jody Hey at Temple University

1. Part 1: 

Write a program that:
- Asks the user for the name of a file containing two columns of numbers
- Reads the file with two columns of numbers
- calculates the product moment correlation
- Writes the value of the correlation to a file named "pmc_calc.txt"
- Be sure to include explanatory comments in your program
- Do not import a module that calculates the coorelation 

2. Part 2:

Write a program that:
- Asks the user for the name of a file containing two columsn of numbers
- Reads the file with two columns of numbeers into a list of lists, where each row of the file becomes a row (list) in the list of lists that is the matrix
- Create a transpose of this matrix
- Write this new matrix to a file named "matrix_transpose.txt"

3. Part 3:

Using Dromel_Adh.fasta, write a python program that:
- Opens Dromel_Adh.fasta and loads the contents 
- Count how many times the sequence GCAA occurs in the file
- print this number to the screen
- Determines the reverse complement of the DNA sequence in the file
    - Reverse the sequence
    - Replace every G with C, every C with G, every T by A, and every A with T
- Count how many times the sequence GCAA occurs in the reverse complement sequence
- print this number to the screeen
- Write a new file with nam "reverse_complement.txt" that contains only the reverse complement sequence.
- Do not import a module that calculates the reverse complement

