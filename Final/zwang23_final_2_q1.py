import pandas as pd
import numpy as np
import xml.etree.ElementTree as et 

#load xml file
xtree = et.parse("xml_final_1.xml")
xroot = xtree.getroot() 

df_cols = ["DataID", "Days", "Cost"]
rows = []

# find items that exists in both Days and Cost
for item in xroot: 
    if item.find('Days') != None and item.find('Cost')!= None:
        for i in item:
            s_DataID = item.find("DataID").text 
            s_Days = item.find("Days").text 
            s_Cost = item.find("Cost").text 
        rows.append({"DataID": s_DataID, "Days": float(s_Days), 
                    "Cost": float(s_Cost)})
# Convert to data frame
df = pd.DataFrame(rows, columns = df_cols)
#Calculate averages of each
df_Days=df['Days'].mean()
df_Cost=df['Cost'].mean()

# final output to match required format
print('AvgDays:',df_Days)
print ('AvgCost:',df_Cost)