import pandas as pd
import numpy as np

#load csv file into dataframe
df=pd.read_csv('csv_final_2.csv')

#drop rows that have NA
df_drop=df.dropna()

#print the average of glucose values by location
print(df_drop.groupby('Location').agg({'Glucose':'mean'}))

