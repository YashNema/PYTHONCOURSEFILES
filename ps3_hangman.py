# -*- coding: utf-8 -*-
# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "‪D:\software\MOOC\600X\600XFILES\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...






def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    a=0
    for i in secretWord:
        if i in lettersGuessed:
            a=a+1
    return a==len(secretWord)     
            
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    l=[]
    for i in secretWord:
        if i in lettersGuessed:
            l.append(i)
        else:
            l.append('_')
    return "".join(l)
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    l=''
    g=''
    for ch in string.ascii_lowercase:
        if ch in lettersGuessed:
            g=g+ch
        else:
            l=l+ch
    return l        
            
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    l=''
    g=''
    for ch in string.ascii_lowercase:
        if ch in lettersGuessed:
            g=g+ch
        else:
            l=l+ch
    return l        
            
# When your hangman function passes the checks in the previous
# box, paste your function definition here to test it on harder 
# input cases.
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is %i letters long'%len(secretWord)
    guesses = 8
    a=0
    lettersGuessed = []
    guessed = False
    while guesses > 0 & guessed == False:
            print '------------'
            print 'You have %i guesses left' % guesses
            print 'Available Letters: %s' % getAvailableLetters(lettersGuessed)
            
        

            yourguess = raw_input('Please guess a letter:')
            if len(yourguess)!=1:
                print 'Please enter a single character again'
                yourguess = raw_input('Please guess a letter:')
                
            yourguess = yourguess.lower()

            if isWordGuessed(yourguess, lettersGuessed) == True:
                print "Oops! You've already guessed that letter:",

            else:
                lettersGuessed.append(yourguess)
                if yourguess in secretWord:
                    print "Good guess:",
                    if ' '.join(secretWord) == getGuessedWord(secretWord, lettersGuessed):
                        print secretWord
                        a=1
                        guessed = True
                        break
                else:
                    print "Oops! That letter is not in my word:",
                    guesses -= 1
            
            print getGuessedWord(secretWord, lettersGuessed)
            if isWordGuessed(secretWord, lettersGuessed):
                a=1
                break
    print '------------'
    if a==0:
        print 'Sorry, you ran out of guesses. The word was %s.' % secretWord
    else:
        print 'Congratulations, you won!'
        
    
         
