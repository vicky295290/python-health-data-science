import json

# load json file
with open('json_final_1.json', mode = 'r') as json_file:
    data = json.load(json_file)

# get to the node that contains all data
data = data['Data']['Dataset']
# initialize a new dict
avg = dict()

# initialize 4 keys, one for each age group
for i in range(0, 4):
    avg[i] = list()

# put corresponding age condition and systolic data in the correct range
for i in data:
    age = float(i['Age'])
    systolic = float(i['Systolic'])
    # range one: < 18.5
    if age < 24:
        avg[0].append(systolic)
    # range two: 18.5 - 24.9
    elif age >= 25 and age <= 44:
        avg[1].append(systolic)
     # range three: 25 - 29.9
    elif age >= 45 and age <= 65:
        avg[2].append(systolic)
    # range four: > 30
    elif age > 65:
        avg[3].append(systolic)
    else:
        0

# calculate average for each range
for i, j in avg.items():
    # if any of the range is empty, then the avg will be 0
    if len(j) == 0:
        avg[i] = 0
        continue
    # avg calculation
    avg[i] = sum(j) / len(j)

# rename the key names with the required ranges
avg['<24'], avg['25-44'], avg['45-65'], avg['>65'] = avg[0], avg[1], avg[2], avg[3]
# delete the old keys
del avg[0], avg[1], avg[2], avg[3]

# final output to match required format
for i, j in avg.items():
    print('Group:', i, ',AvgBP:', j)