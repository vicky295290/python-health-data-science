import json

#define path of json file
rootpath = 'bundle.json'

#read json input
def json_read(filepath):
    with open(filepath, mode = 'r') as f:
        file = json.load(f)
        f.close()
    return file

#get name of hospital
def hospital_name(input):
    output = input['Hospital']['Name']
    return output

#count of measures for hospital
def measure_count(input):
    output = len(input['Measures'])
    return output

#check if given measure is present
def present(input, measure):
    total_measure = [i['Name'] for i in input['Measures']]
    if measure in total_measure:
        return "Yes"
    else:
        return "No"

#load our input json file
data = json_read(rootpath)['entry']

# print for each hospital
for i in data:
    print('Name of the hospital: ', hospital_name(i), '\nTotal count of Measures for the hospital: ', measure_count(i), '\nif measure "READM-30-CABG-HRRP" is present: ', present(i, measure="READM-30-CABG-HRRP"), '\n')
