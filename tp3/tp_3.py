import numpy as np
import pandas as pd

df = pd.read_csv('D:/VsCode/Python/tp3/winter_olympics_medals.csv')


print ("Les JO ont eu lieu seulement pandant les années :",df.year.unique())

print ("Voici la liste des pays qui ont participé au JO et qui ont gagné une médaile",df.pays.unique())

df_host = df[df["host"] == True]["pays"]
print("Voici la liste des pays qui ont organisé les JO et qui ont gagné une médaile",df_host.unique())

df_moyenne = df.groupby('country').size().mean()
print("moyenne de médailles par pays",df_moyenne)

