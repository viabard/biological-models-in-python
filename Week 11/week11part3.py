import pandas as pd 
import numpy as np

fileThing = open("11.3-output.txt", 'w')
df = pd.read_csv("ENS_Genic_Codon_Branch_ADJ_Residuals.tsv", sep='\t', index_col=[0])
df.replace(0, np.NaN, inplace=True)
df2 = pd.DataFrame(df.mean(1))
fileThing.write("Shape: " + str(df2.shape))
fileThing.write('\n\n')
fileThing.write("Mean of means: " + str(df2.mean(0).get(0)))
fileThing.close()