#!/usr/bin/env python
# coding: utf-8

# In[34]:


# HW1 PART2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    
        for i in secret_word:
            if i not in letters_guessed:
                return False
        
        return True        





def get_guessed_word(secret_word, letters_guessed):
    
    temp = ""
    for i in secret_word:
            if i  in letters_guessed:
                temp = temp+i
            else:
                temp = temp+"_ "
        
    return temp  
    



def get_available_letters(letters_guessed):
    alphabet = string.ascii_lowercase 
    temp=""
    for i in alphabet:
        if i not in letters_guessed:
            temp+=i
    
    return temp
        

def hangman(secret_word):
    
    print("Helcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secret_word))+" letters long.")
    print("You have 3 warnings left.")
    print("-------------")
    
    guesses= 6
    warnings= 3
    while(True):
        print("You have "+str(guesses)+" guesses left.")
        print("Available letters: "+str(get_available_letters(letters_guessed)))
        print("Please guess a letter:")
        letter = input()
        letter = str.lower(letter)
        
        if (not str.isalpha(letter)) or (len(letter)!=1): 
            warnings-=1
            
            if warnings<0:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "+ str(get_guessed_word(secret_word, letters_guessed)))
                guesses-=1
            else:
                print("Oops! That is not a valid letter. You have "+str(warnings)+" warnings left: "+ str(get_guessed_word(secret_word, letters_guessed)))
            
        elif letter in letters_guessed:
            warnings-=1
            
            if warnings<0:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "+ str(get_guessed_word(secret_word, letters_guessed)))
                guesses-=1
            else:
                print("Oops! You've already guessed that letter. You have "+str(warnings)+" warnings left: "+ str(get_guessed_word(secret_word, letters_guessed)))
                
        
        elif letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: "+str(get_guessed_word(secret_word, letters_guessed)))
            
        
        elif letter not in secret_word:
            letters_guessed.append(letter)
            print("Oops! That letter is not in my word: "+str(get_guessed_word(secret_word, letters_guessed)))
            if (letter=='a' or letter =='e' or letter=='i' or letter=='o' or letter=='u'):
                guesses-=2
            else:
                guesses-=1
                
        print("-------------")
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            unique_letters= list(set(secret_word))
            score= len(unique_letters) * guesses
            print("Your total score for this game is: "+ str(score))
            break
        if guesses <=0: 
            print("Sorry, you ran out of guesses. The word was "+secret_word+".")
            break
        
    
    
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    my_word= my_word.replace(" ", "")
    index = 0
    if (len(my_word)==len(other_word)):
        for i in my_word:
            if i == "_":
                index+=1
                continue
            elif i != other_word[index]:    
                return False
            index+=1
        return True
    
    else:
        return False
    


def show_possible_matches(my_word):
    temp=""
    counter=0
    for i in wordlist:
        if match_with_gaps(my_word, i):
            temp= temp+i+" "
            counter+=1
    if counter==0:
        print("No matches found!")
    else:
        print(temp)
    




def hangman_with_hints(secret_word):
    
    print("Helcome to the game Hangman!")
    print("I am thinking of a word that is "+str(len(secret_word))+" letters long.")
    print("You have 3 warnings left.")
    print("-------------")
    
    guesses= 6
    warnings= 3
    while(True):
        print("You have "+str(guesses)+" guesses left.")
        print("Available letters: "+str(get_available_letters(letters_guessed)))
        print("Please guess a letter:")
        letter = input()
        letter = str.lower(letter)
        
        if letter == "*":
            print("Possible word matches are: ")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif (not str.isalpha(letter)) or (len(letter)!=1): 
            warnings-=1
            
            if warnings<0:
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: "+ str(get_guessed_word(secret_word, letters_guessed)))
                guesses-=1
            else:
                print("Oops! That is not a valid letter. You have "+str(warnings)+" warnings left: "+ str(get_guessed_word(secret_word, letters_guessed)))
            
        elif letter in letters_guessed:
            warnings-=1
            
            if warnings<0:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: "+ str(get_guessed_word(secret_word, letters_guessed)))
                guesses-=1
            else:
                print("Oops! You've already guessed that letter. You have "+str(warnings)+" warnings left: "+ str(get_guessed_word(secret_word, letters_guessed)))
                
        
        elif letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: "+str(get_guessed_word(secret_word, letters_guessed)))
            
        
        elif letter not in secret_word:
            letters_guessed.append(letter)
            print("Oops! That letter is not in my word: "+str(get_guessed_word(secret_word, letters_guessed)))
            if (letter=='a' or letter =='e' or letter=='i' or letter=='o' or letter=='u'):
                guesses-=2
            else:
                guesses-=1
                
        print("-------------")
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            unique_letters= list(set(secret_word))
            score= len(unique_letters) * guesses
            print("Your total score for this game is: "+ str(score))
            break
        if guesses <=0: 
            print("Sorry, you ran out of guesses. The word was "+secret_word+".")
            break
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
    pass
letters_guessed=[]

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #hangman(secret_word)
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)


# In[105]:


#hangman("else")


# In[117]:


match_with_gaps("a_ ple", "apple") # hocada false dönmüş


# In[118]:


#13.sayfada kaldım bu üstte yazdığım hariç çalışıyo fonksyon


# In[16]:


show_possible_matches("a_ g")


# In[27]:


hangman_with_hints("apple")


# In[ ]:




