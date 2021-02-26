from scipy import spatial
import os

def row_similarity(row1, row2):
    threshold = 50

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

    if (result * 100) > threshold:
        return True
    else:
        return False


################################################################  load files part

files = [doc for doc in os.listdir() if doc.endswith('.py')] # load python files

if "word frequency in files.py" in files:
    files.remove("word frequency in files.py") # remove our program from list

files_content =[open(File).read() for File in  files] # load file content into list

################################################################

data_list = [] # it will store list of dictionaries
all_words = []
for f in files_content: # this loop split word and create a dictionary with frequency of word
     
    words = f.split()
    all_words = all_words + words
    wordDict = {}
    for word in words:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1
        
    data_list.append(wordDict)

all_words_set = set(all_words) # this set holds all words, i hold them in a set to avoid dublicated words

vectors=[] # this list holds list of frequency for each file and words

"""
example:
file0 {"apple":2}
file1 {"banana":4}
all_words_set is (apple,banana)
vectors[0] = [2, 0]
vectors[1] = [0, 4]
"""


for w in all_words_set: # The loop that does the work in the example above
  
    for index in range(len(data_list)):
        
        if len(vectors) == index:
            vectors.append([])

        if w in data_list[index]:
            vectors[index].append(data_list[index][w])
        else:
            vectors[index].append(0)
        

"""
I use SCIPY library and cosine similarity
Cosine similarity measures the similarity between two vectors of an inner product space
"""

for i in range(len(files)):
    for j in range(len(files)):
        if i <= j :
            continue
        similarity = 1 - spatial.distance.cosine(vectors[i], vectors[j])
        print("Similarity between",files[i],"and",files[j],"is",(similarity * 100),"%")


        



"""
print(files)
print(data_list)
"""



    
