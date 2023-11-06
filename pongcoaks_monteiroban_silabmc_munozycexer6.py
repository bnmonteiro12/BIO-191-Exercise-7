"""
Author: Andrea Kristine S. Pongco
Student Number: 2020-01929
Author: Bea Alyssa N. Monteiro
Student Number: 2020-05788
Author: Mariellen C. Silab
Student Number: 2020-04157
Author: Yuji C. Munoz
Student Number: 2021-06470

Date of Development: October 23, 2023 @ 11:40 AM
"""

#input_string = list(str(input("Enter file name: ")).split(" "))

import re

def readFile():

    words = []
     
    file = open("species.txt", "r") # open file in reading mode

    wordlines = file.readlines() # read every line and store in the words variable as a list

    for i in wordlines:
        words.append(i.strip())

    return words

words = readFile() #Call readFile function with value

def countWords(words):

    bag_of_words = {} # dictionary
    sentences = []

    for i in words: # for every item in the words list
        if i not in bag_of_words.keys(): # if the said item is not in the dictionary keys
            bag_of_words[i] = 1 # put it in the dictionary and initialize the value as 1
        else: # else, increment the value
            bag_of_words[i] += 1

    for i in bag_of_words:
        sentences.append("{key} {value}\n".format(key=i, value=bag_of_words[i]))    

    return sentences

sentences = countWords(words)

def writeFile(sentences):
    
    file = open("group3_output.txt", "w") 
    file.writelines(sentences)
    file.close()

writeFile(sentences)