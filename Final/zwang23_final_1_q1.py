import xml.etree.ElementTree as ET
import os

# load xml file
tree = ET.parse('xml_final_1.xml')
root = tree.getroot()

# initialize dicts for all data, days, and cost data.
all_data = dict()
days_data = dict()
cost_data = dict()

# iter through the tags
for item in root.findall('dataset'):
    # find items that exists in both Days and Cost
    if item.find('Days') != None and item.find('Cost') != None:
        # pass in the data that matches both conditions
        for i in item:
            # pass into master dict and seperate Days/Cost dicts
            all_data.setdefault(i.tag, list()).append(i.text)
            days_data = all_data.get('Days')
            cost_data = all_data.get('Cost')

def convert_to_float(data):
    """ utility function for converting lists inside the dict to floats for calculation.

    Typical usage example:

    print(convert_to_float(data))

    Args:
        data: input dict with different lists of string numbers.

    Returns:
        data: list of floats.
    """
    for i in range(0, len(data)):
        data[i] = float(data[i])
    return data

def calc_avg(data):
    """ utlity function for calculating average.

    Typical usage example:

    print(calc_avg(data))

    Args:
        data: input list of numbers

    Returns:
        avg: float type, average of input numbers
    """
    avg = sum(data) / len(data)
    return avg

# final output to match required format
print('AvgCost:', calc_avg(convert_to_float(cost_data)), ',AvgDays:', calc_avg(convert_to_float(days_data)))