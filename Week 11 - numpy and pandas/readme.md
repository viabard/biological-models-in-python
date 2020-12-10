# Week 11 - numpy and pandas
Working with numpy and pandas for better matrices/lists. This assignment had three scripts.
This worksheet was made and is copyrighted (2020) by Dr. Jody Hey at Temple University

1. Script 1:
Use numpy

Write a script that:
- Generates a results file
- Creates a 2D array (10 rows, 7 columns) with random floating point values between 0 and 10
    - print the integer parts of the array
    - print the integer parts of the array to the results file
- Use  np.arange() to make a 1D array with 12 elements, then use "in place" conditions to change the array so that all elements greater than 3 and less than 9 are replaced by their negative values.
    - print the array to the results file

2. Script 2:
Use pandas
Find data in csv or tsv format witha first row containing headers (usgs_earthquakes_2014.csv)

Write a script that:
- generates a results file
- loads the data into a pandas dataframe
- write the shape of the dataframe and the names of the columns to a results file
- write out the datatype for each column to a file
- calculate, using the padnas.DataFrame.corr() method, the correlation between all of the paris of columns that contain numerical data
    - write the correlations to the results file
    - You may need to convert missing data to NaNs

3. Script 3:
Use pandas

Write a script that:
- generates a results file
- loads ENS_Genic_Codon_Branch_ADJ_Residuals.tsv using '\t' as the separator (tab deliminated) (This contains branch lengths for a lot of genes on a tree of 17 species of mammals)
- Replace all the 0's with NaNs (do this in place, read about nans)
- Build a new dataframe with one row peer gene, and one column that contains the mean branch lengths
- Print the shape of this datafram and the mean of all the mean branch lengths, across genes, to a file