from xml.etree import ElementTree as ET
import os

# load xml file
tree = ET.parse('xml_final_2.xml')
root = tree.getroot()

# initialize dicts for all data, before, after, location and diff data.
all_data = dict()
before_data = dict()
after_data = dict()
loc_data = dict()
diff_data = dict()

# iter through the tags
for item in root.findall('dataset'):
    for i in item:
        # pass into master dict and seperate before/after/location dicts
        all_data.setdefault(i.tag, list()).append(i.text)
        before_data = all_data.get('BP_Before')
        after_data = all_data.get('BP_After')
        loc_data = all_data.get('Location')

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

# convert both before and after data to float for calculation
before_data_float = convert_to_float(before_data)
after_data_float = convert_to_float(after_data)

# based on location calculate the different between before and after
for i, j in enumerate(loc_data):
    diff_data.setdefault(j, list()).append(before_data_float[i] - after_data_float[i])

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
avg = avg_dict(diff_data)
# final output to match required format
for i, j in avg.items():
    print('Location:', i, ',AvgBPDiff:', j)
