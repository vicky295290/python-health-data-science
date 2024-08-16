import os

root_path = "medline/"

def freq_count(filename):
    """counts the number of words in a file.

        Typical usage example:

        dict = freq_count('example.txt')

    Args:
        filename: input string of a file name.

    Returns:
        count: output dict with number of words.
    """
    
    count= {}
    #join with relative folder path with filename
    path = os.path.join(root_path, filename)
    #open file
    file = open(path,'r')
    #read file
    data = file.read()
    #split into individual words
    words = data.split()
    
    #loop through words to get frequency
    for i in words:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return count

# test freq_count function
# print(freq_count('18719013.txt'))

# initialize master dictonary
master_dict = {}
# list to store file names
file_names = []

# loop through directory to get list of file names
for path in os.listdir(root_path):
    file_names.append(path)
    

def merge_dict(dict1, dict2):
    """utility function to merge two given dicts.

        Typical usage example:

        dict = merge_dict(dict1, dict2)

    Args:
        dict1: first dict to be merged.
        dict2: second dict to be merged.

    Returns:
        dict1: a merged dict of input dicts.
    """
    
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1

#merge all files into one master dict
for i in file_names:
    freq = freq_count(i)
    master_dict = merge_dict(freq, master_dict)
    #maybe can try dict1.update(dict_2)


def top_three_dict(dict_input):
    """get top three frequency item in a dict.

        Typical usage example:

        top_three_dict(dict)

    Args:
        dict: input dictonary to find top three frequency items.

    Returns:
        dict containing three most frequent words.
    """
    temp = []
    d = {}
    #remove duplicates in an input dict to ignore repeats
    for key, val in dict_input.items():
        if val not in temp:
            temp.append(val)
            d[key] = val

    d = sorted(d.items(), key=lambda x:x[1], reverse=True)[:3]
    sorted_dict = dict(d)
    # print sorted items from input dict with top three freq items        
    return print(sorted_dict)

#get final output
top_three_dict(master_dict)