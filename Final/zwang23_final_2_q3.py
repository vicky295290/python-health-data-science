import pandas as pd
import numpy as np

# load csv file into dataframe
df = pd.read_csv('csv_final_1.csv')
df['Glucose'] = df['Glucose'].astype(float)

#filter out rows that have glucose value >120
df_120 = df[df.Glucose>120]

#Calculate standard deviation for glucose,
# and how many standard deviation for each glucose value.
df_120['SD']=(df_120['Glucose']-df_120['Glucose'].mean())/df_120['Glucose'].std()

#Filter out results for SD<1
print(df_120[df_120['SD']<1])


