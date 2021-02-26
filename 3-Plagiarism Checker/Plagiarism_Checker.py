#############################################################################
#                            ### IMPORTANT ###                              #
# In this program SCIPY LIBRARY is used. It has to download with this steps.#
# open cmd and write this -> pip install scipy                              #
#############################################################################

from scipy import spatial # needed to use cosine similarity function
import os   # needed to read .py extension files

def prepareForWrite(lines, reference):  # this function takes lines of files and reference count of lines. Returns a list that referenced lines are highlited with number of repeats.
    myList = []
    for i in range(len(lines)):
        if reference[i] > 0:
            myList.append("*-- " + lines[i] + "!! Similar with " + str(reference[i]) + " lines. --*" + "\n")
        else:
            myList.append(lines[i] + "\n")
    return myList


    
def fillListOfReference(current_rows):  # takes a list and return an zero list with size of current_rows
    myList = []
    for i in range(len(current_rows)):
        myList.append(0)
    return myList

def fillListOfLines(current_rows): # take a list and returns a new list
    myList = []
    for row in current_rows:
        myList.append(row)
    return myList


def writeToFile(fileName, lines): # takes string filename and lines[] and write this list to file.
    f = open(fileName, "w")
    f.writelines(lines)
    f.close()


def remove_values_from_list(the_list, val): # used for remove a specific element from list
   return [value for value in the_list if value != val]


#################### ROW SIMILARITY FUNCTION ###########################
def row_similarity(row1, row2): # this is the most important function of the program. Takes two string as argument.
    threshold = 60  # manually settable threshold

    words1 = row1.split() # splits string by whitespaces
    words2 = row2.split()

    dict1 = {} # dictionary to hold frequency of elements for each string dict and dict2
    dict2 = {}


    for w in words1: # this two loops fill the dictionaries. If the element is in the dictionary, its value is increased by one. If not, its value is added as zero.
        if w in dict1:
            dict1[w] = dict1[w] + 1
        else:
            dict1[w] = 1


    for w in words2: 
        if w in dict2:
            dict2[w] = dict2[w] + 1
        else:
            dict2[w] = 1   


    all_words_set =  set(words1 + words2) # eliminate dublicated words from all words


    vector1 = [] 
    vector2 = []

    #The work done by the operation below is explained in detail in the report. 
    # Also added an example of operation
    for v in all_words_set: # vector1 and vector2 filled
        if v in dict1:
            vector1.append(int(dict1[v]))
        else:
            vector1.append(0)

        if v in dict2:
            vector2.append(int(dict2[v]))
        else:
            vector2.append(0)
    """
    example:
    file0 {"apple":2,"car":3,"mouse":5}
    file1 {"banana":4}
    all_words_set is (apple,banana,car,mouse)
    vectors[0] = [2,0,3,5]
    vectors[1] = [0,4,0,0]
    """


    result = 1 - spatial.distance.cosine(vector1, vector2) # cosine similarity function used and similarity ratio calculated

    if (result * 100) > threshold: # Returns true if higher than the threshold value, returns false otherwise
        return True
    else:
        return False

#################### END OF THE ROW SIMILARITY FUNCTION ################


############################# load files part #############################

files = [doc for doc in os.listdir() if doc.endswith('.py')] # loads python files

if "Plagiarism_Checker.py" in files: # prevented from receiving our own file
    files.remove("Plagiarism_Checker.py") 

files_content =[open(File).read() for File in  files] # load file content into list

###########################################################################

similarity_threshold = .0 # this threshold can be used to print similarity of files after a certain similarity ratio


for current_file_index in range(len(files_content)): # select a files to compare
    
    current_rows = files_content[current_file_index].splitlines() # lines of files loaded to a list
    current_rows = remove_values_from_list(current_rows,"") # empty lines removed
    list_of_lines = fillListOfLines(current_rows)  # holds line of files. if this file have copy lines we use this list
    list_of_reference = fillListOfReference(current_rows) # holds count of reference number of lines

    for other_file_index in range(len(files_content)): # select file to compare with current file
        if(current_file_index == other_file_index): # if they are same file continue
            continue

        
        counter = 0 # counter to hold number of suspicious lines
        
        other_rows = files_content[other_file_index].splitlines() # lines of files loaded to a list
        other_rows = remove_values_from_list(other_rows,"") # empty lines removed

        index = 0 # variable to take current index

        for c_row in current_rows: # loop for turn each row in current file

            temp_counter = 0 # counter to control if this line of current file is suspicious
            for i in range(len(other_rows)): 

                # this if controls that  our line is not just a keyword. If is a keyword not not put into comparison
                if ( (c_row != "") and (other_rows[i] != "") 
                and (c_row != "{") and (c_row != "}") and (c_row != "(") and (c_row != ")") and (c_row != "else:") 
                and (c_row != "if") and (c_row != "else") and (c_row != "else if") ):

                    if row_similarity(c_row, other_rows[i]): # the function that calculates similarity ratio between rows is called
                        temp_counter += 1
                        list_of_reference[index] += 1 # this list holds that current line how many time referenced (find in other files) 
                        
            if temp_counter > 0: # if line is suspicious counter of current files is one increased
                counter += 1

            index += 1   # passed to the index of the next row
              

        similarity = float(counter / len(current_rows)) # calculates similarity ratio of current file
        if(similarity) >= similarity_threshold: # if similarity ratio larger than similarity_threshold its printed with ratio
            print("Similarity of",files[current_file_index],"to",files[other_file_index],"is",(similarity * 100),"%")

    readyToWriteList = prepareForWrite(list_of_lines,list_of_reference) # datas prepared to write
    writeToFile(files[current_file_index], readyToWriteList) # python file highlited
        
print("The program is over!!")





    
