import pandas as pd
import numpy as np
import json

# load json file into dataframe
path = "json_final_1.json"
jfile = open(path, "r").read()
data = json.loads(jfile) 

df = pd.DataFrame(data['Data']['Dataset'])
df = df[["Age", "BMI", 'Glucose', 'Systolic']]
df = df.astype(float)

#filter and create Age groups
df1 = df[df['Age']<24].copy()
df2 = df[(df['Age']>25) & (df['Age']<44)].copy()
df2['AgeGroup']='25-44'
df3 = df[(df['Age']>45) & (df['Age']<65)].copy()
df3['AgeGroup']='45-65'
df4 = df[df['Age']>65].copy()
df4['AgeGroup']='>65'

#merge Age groups
df=pd.concat([df1,df2,df3,df4])

#Calculate systolic mean for each age groups. 
print(df.groupby('AgeGroup').agg({'Systolic':'mean'}))