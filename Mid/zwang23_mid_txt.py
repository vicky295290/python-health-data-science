import os

#set root path
rootpath = './'

#get all freqency of words
def freq(filename):
    count = {}
    path = os.path.join(rootpath, filename)

    file = open(path, mode = 'r')
    words = file.read().lower().split()

    #append freqency for each word
    for i in words:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1

    return count

#sort and get top 10 freq words
def top_ten_freq(input):
    temp = []
    d = {}

    #remove duplicates
    for key, val in input.items():
        if val not in temp:
            temp.append(val)
            d[key] = val

    #sort all freq and get first 10
    d = sorted(d.items(), key = lambda x:x[1], reverse=True)[:10]

    return dict(d)

#print results
print('top 10 words and frequency: \n', top_ten_freq(freq(filename='abstract.txt')))