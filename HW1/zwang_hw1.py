import os

#define a relative folder path
root_path = "medline/"

#function to display total word count
def word_count(filename):
    #join with relative folder path with filename
    path = os.path.join(root_path, filename)
    #open file
    file = open(path,'r')
    #read file
    data = file.read()
    #split into individual words
    words = data.split()
    #get number of words
    count = len(words)

    return print("Total word count is: " + str(count))

#function to display most frequently used word and count
def word_freq(filename):
    #initialize freq word and count
    frequent_word = "" 
    frequency = 0

    #join with relative folder path with filename
    path = os.path.join(root_path, filename)
    #open file
    file = open(path,'r')
    #read file
    data = file.read()
    #split into individual words
    words = data.split()
    #get number of words
    count = len(words)

    #loop through words
    for i in range(0, count):
        num = 1

        #count words freq 
        for j in range(i+1, count):   
            if(words[i] == words[j]): 
                num += 1
    
        #compare words freq and update
        if(num > frequency):
            frequency = num
            frequent_word = words[i]

    return print("Most frequently used word is: " + frequent_word + ", its frequency count is: " + str(frequency))


#test #1 for first function
word_count("18719013.txt")
#test #2 for first function
word_count("23852273.txt")

#test #1 second function
word_freq("18719013.txt")
#test #2 second function
word_freq("23852273.txt")