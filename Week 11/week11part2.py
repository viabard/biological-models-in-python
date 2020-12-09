import pandas as pd 
#open a csv file, write shape of dataframe and names of the columns to a file
fileThing = open("11.2-output.txt", 'w') 
earthquakesDF = pd.read_csv(open("usgs_earthquakes_2014.csv"))
fileThing.write("Shape of CSV: " + str(earthquakesDF.shape))
fileThing.write("\n\n")
fileThing.write("Data types: \n" + str(earthquakesDF.dtypes))
fileThing.write("\n\n")
#print correlations to a file
corr = pd.DataFrame.corr(earthquakesDF)
fileThing.write("Correlations: \n" + str(corr))
fileThing.close()