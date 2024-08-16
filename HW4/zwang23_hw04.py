import os
import csv

#initialize dataset and columns
data = []
cols = []

#open and read csv file
with open('outpatient_sample.csv', mode = 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    cols = next(csv_reader)
    for row in csv_reader:
        data.append(row)

#initialize for q1: total visits per patient
visits = {}
#get both visit_ID and patient_ID columns
visits_col = cols.index('Visit_ID')
patient_col = cols.index('Patient_ID')

#initialize for q2: total unique physicians seen per patient
physicians = {}
#get all three types of physicians columns
#all three columns shares the common word "Physician"
physicians_col = [
    index for index, value in enumerate(cols) 
    if 'Physician' in value
    ]

#initialize for q3: Total unique diagnosis per patient
diagnosis = {}
#get all diff types of diagnosis columns
#all columns shares the common word "ICD9"
diagnosis_col = [
    index for index, value in enumerate(cols) 
    if 'ICD9' in value
    ]

#initialize for q4: Most frequent diagnosis per patient
ICD_total = {}
ICD_freq = {}

#q1:
#combine Visit_ID to corresponding Patient_ID
for i in data:
    visits.setdefault(i[patient_col], set()).add(i[visits_col])

#gets the len of keys for number of visits
for key in visits.keys():
    visits[key] = len(visits[key])

#q2:
#combine Physicians to corresponding Patient_ID
#check if the Physicians filed is empty
for i in data:
    for phys in physicians_col:
        if i[phys] == '':
            continue
        physicians.setdefault(i[patient_col], set()).add(i[phys])

#gets the len of keys for number of physicians
for key in physicians.keys():
    physicians[key] = len(physicians[key])

#q3:
#combine diagnosis to corresponding Patient_ID
#check if the diagnosis filed is empty
for i in data:
    for diag in diagnosis_col:
        if i[diag] == '':
            continue
        diagnosis.setdefault(i[patient_col], set()).add(i[diag])
        #this is for q4
        ICD_total.setdefault(i[patient_col], []).append(i[diag])

#gets the len of keys for number of diagnosis
for key in diagnosis.keys():
    diagnosis[key] = len(diagnosis[key])

#q4:
#compute a most freq diagnosis item for each patient
for x in ICD_total.keys():
    freq= {}
    most_freq = 0
    freq_name = ''
    #loop through to get all freqency
    for i in set(ICD_total[x]):
        count = 0
        for j in ICD_total[x]:
            if i == j:
                count = count + 1
        freq[i] = count

    #look through to compare and get the most freq item
    for i in freq.keys():
        if freq[i] > most_freq:
            freq_name = i
            most_freq = freq[i]

    ICD_freq[x] = freq_name

#utils function to merge dicts
def merge_dict(*dicts):
    """helper function to merge multiple dicts

    Example usage:

    master_dict = merge_dict(dict1, dict2, dict3, dict4)

    Args:
        *dicts: input dict type, many different dicts

    Returns:
        combined dict of all input dicts
    """
    res = {}
    for d in dicts:
        if not isinstance(d, dict):
            continue
        for k, v in d.items():
            res.setdefault(k, [])
            if isinstance(v, list):
                res[k].extend(v)
            else:
                res[k].append(v)
    return res

#master dict to combine all 4 questions output
master_dict = merge_dict(visits, physicians, diagnosis, ICD_freq)

#pour outputs into csv file with corresponding headers
with open('zwang23_hw04.csv', mode='w',newline='') as csv_file:
    header_key = ['Patient_ID', 'Total_Visits', 'Total_Physicians', 'Total_Diagnosis', 'Most_Freq_Diganosis']
    csv_writer = csv.DictWriter(csv_file, fieldnames=header_key)
    csv_writer.writeheader()

    writer = csv.writer(csv_file)
    for key, value in master_dict.items():
        writer.writerow([key, *value])