import pandas as pd
import numpy as np
import xml.etree.ElementTree as et 

# load xml file
xtree = et.parse("xml_final_2.xml")
xroot = xtree.getroot() 

#Create columns for df
df_cols = ["DataID", "BP_Before", "BP_After","Location","Group"]
rows = []

#iter through data and load data into dataframe
for item in xroot: 
     s_DataID = item.find("DataID").text 
     s_BP_Before = item.find("BP_Before").text  
     s_BP_After = item.find("BP_After").text 
     s_Location = item.find("Location").text 
     s_Group = item.find("Group").text 
     rows.append({"DataID": s_DataID, "BP_Before":float(s_BP_Before), "BP_After":float(s_BP_After),
     "Location":s_Location,"Group":s_Group})
#calculate the different between before and after
df = pd.DataFrame(rows, columns = df_cols)
df = df.assign(BP_Diff = df['BP_Before'] - df['BP_After'])


# print the average of BP differences for each location
print(df.groupby('Location').agg({'BP_Diff':'mean'}))

