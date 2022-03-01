import pandas as pd
import numpy as np
import os
import glob


csv_files = glob.glob('DataSet/*.csv')
for i in csv_files:
    print(i)

data_list = []

#Scannez la liste des fichiers à lire
for file in csv_files:
    data_list.append(pd.read_csv(file))

#Combinez toutes les listes dans le sens des lignes
df = pd.concat(data_list, axis=0, sort=True)

df.to_csv("DataSet/total.csv",index=False)

print(df)