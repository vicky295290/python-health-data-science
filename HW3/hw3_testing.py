import csv
from hw3 import HWReader

csv_data = HWReader("icu_data.csv")

#Get a SAPS-1 score of specific record
print(csv_data.get_saps("132582"))

#Get average of length of stay for SOFA < 15
#logic lt less than
#logic gt greather than
#logic lte less than equal
#logic gte greather than equal
print(csv_data.calc_avg("Length_of_stay", filter="SOFA", logic="lt", threshold="15"))