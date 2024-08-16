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


#filter and create BMI groups
df1 = df[df['BMI']<18.5].copy()
df1['BMIGroup']='18.5'
df2 = df[(df['BMI']>18.5) & (df['BMI']<24.9)].copy()
df2['BMIGroup']='18.5-24.9'
df3 = df[(df['BMI']>25) & (df['BMI']<29.9)].copy()
df3['BMIGroup']='25-29.9'
df4 = df[df['BMI']>30].copy()
df4['BMIGroup']='>30'

#merge BMI groups
df=pd.concat([df1,df2,df3,df4])

#Calculate Gluocse mean for each BMI groups. 
print(df.groupby('BMIGroup').agg({'Glucose':'mean'}))

