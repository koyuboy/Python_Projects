from scipy import spatial


#import os
"""
files = [doc for doc in os.listdir() if doc.endswith('.py')] # load python files

if "row frequency in files.py" in files:
    files.remove("word frequency in files.py") # remove our program from list

files_content =[open(File).read() for File in  files] # load file content into list

################################################################
 bu bir fonksiyon ve parametre olarak iki string alır. bunlar iki satırdır  (row1,row2)  
################################################################
"""

row2 = "I have an apple"
row1 = "She has an apple and apple juice"



################################# fonkso-yon gövdesi





words1 = row1.split()
words2 = row2.split()

dict1 = {}
dict2 = {}


for w in words1: 
    if w in dict1:
        dict1[w] = dict1[w] + 1
    else:
        dict1[w] = 1


for w in words2: 
    if w in dict2:
        dict2[w] = dict2[w] + 1
    else:
        dict2[w] = 1   


all_words_set =  set(words1 + words2)


vector1 = []
vector2 = []

for v in all_words_set:
    if v in dict1:
        vector1.append(int(dict1[v]))
    else:
        vector1.append(0)

    if v in dict2:
        vector2.append(int(dict2[v]))
    else:
        vector2.append(0)



result = 1 - spatial.distance.cosine(vector1, vector2)



print("Similarity :", (result * 100), "%")