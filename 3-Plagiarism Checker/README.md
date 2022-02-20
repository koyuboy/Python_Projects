# PLAGIARISM CHECKER REPORT

A Line or word based algorithms, deep learning based methods etc. detects and reveals
a plagiarized content, whether intentional or not.

There are many approaches and methods to detect plagiarized contents. Line or word
based algorithms, deep learning based methods etc. Usually, plagiarism checkers work online,
which means they search and detect content online.

We developed an algorithm based on row analysis in our project and we made use of
the scipy library while doing this. We used Cosine Similarity Function from Scipy library.

Cosine similarity is a metric used to determine how similar the documents are
irrespective of their size. Another definition is Cosine similarity measures the
similarity between two vectors of an inner product space.

The function is -> cosine(u, v)

u and v are one dimensional arrays. Function computes the Cosine distance between two
arrays. After returns a double value.

All program based on row_similarity(row1, row2) funciton. So we will
understand how this works. This function takes two arguments. They are row1 and
row2 and they are in string type. Function take this rows and splitis. After that uses
two dictionary to reveal frequency of splitted elements. After that, three things are
important to us. Two lists vector1 , vector2 and a set of all_words_set. We used a set to
eliminate duplicate elements. We have filled vector1 and vector2 with this set in a loop
with a rule. After that cosine similarity function called with vector1 and vector2.

There is an example of this operation:

row1 = “I have an apple”

row2 = “She has an apple and apple juice”

all_words_set = [“I”, “have”, “an”, “apple”, “She”, “has”, “and”, “juice”]

vector1 = [1, 1, 1, 1, 0, 0, 0, 0]

vector2 = [0, 0, 1, 2 , 1, 1, 1, 1]

1 – spatial.distance.cosine(vector1, vector2)

This operation returns a similarity ratio. We can manually choose a threshold for
accepting these two contents as duplicates. We finished explaining what this function
does. Let's see what the whole program does.

Other jobs of the program is quite simple. The program and the files to be
compared must be in the same directory. It reads files with Python extension, splits
them into lines and puts them into some preprocessing. Lastly it sends the lines in pairs
to the row_similarity function. Each line in a file is compared with lines in other files.

The number of times it has been detected in other files is written next to each line in the
files. At the end, the similarity ratios of the files are printed on the screen and the
program ends.


## CONCLUSION

This program looks at every line and then every word. This is a little bad
approach. Algorithm can be developed with recognize the structs like functions, loops,
switch-cases etc. After that program can compares that structs with each other. This
will make better accuracy. Because some code lines can be in all the programs and this
lines increase our plagiarism ratio. Therefore program should look code files by part
based not only line based.

Also in our program threshold is setting manually by programmer. This
threshold ratio should be setted nicely. A deep learning model or AI based programs
can be used to determine the threshold.

Lastly if this algorithm improves it can be detailed checker. Because we can say
that this plagiarism checker algorithm is variable-free. It means is that revealing
plagiarism is not affected from changing function names, if program improved to part
based algorithm.




***Open report.pdf to see examples***
