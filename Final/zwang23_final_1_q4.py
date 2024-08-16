import csv
import os

# initialize dicts for all data, glucose, location, and average data.
all_data = dict()
glucose_data = dict()
location_data = dict()
avg_data = dict()

# load csv file
with open('csv_final_2.csv', mode = 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    cols = next(csv_reader)
    for row in csv_reader:
        # check for "NA" values and skip
        if 'NA' in row:
            continue
        for i, j in enumerate(cols):
            # pass into master dict and seperate glucose, location dicts
            all_data.setdefault(j, list()).append(row[i])
            glucose_data = all_data.get('Glucose')
            location_data = all_data.get('Location')

def convert_to_float(data):
    """ utility function for converting lists inside the dict to floats for calculation.

    Typical usage example:

    print(convert_to_float(data))

    Args:
        data: input dict with different lists of string numbers.

    Returns:
        data: dict type, list of floats.
    """
    for i in range(0, len(data)):
        data[i] = float(data[i])
    return data

# convert glucose data to float for calculation
glucose_data_float = convert_to_float(glucose_data)

# based on location data gather corresponding glucose data
for i, j in enumerate(location_data):
    avg_data.setdefault(j, list()).append(glucose_data_float[i])

def avg_dict(data):
    """ utlity function for calculating average.

    Typical usage example:

    print(avg_dict(data))

    Args:
        data: input dict with list of numbers

    Returns:
        result: average number of each key in the dict
    """
    result = {k:sum(x)/len(x) for k ,x in data.items()}
    return result

# compute average
avg = avg_dict(avg_data)
# final output to match required format
for i, j in avg.items():
    print('Location:', i, ',AvgGlucose:', j)
