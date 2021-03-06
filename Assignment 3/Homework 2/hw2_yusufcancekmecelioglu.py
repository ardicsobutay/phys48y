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

WORDLIST_FILENAME = "words.txt"

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
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    for c in secretWord:
        if c in lettersGuessed:
            guessedWord += c
        else:
            guessedWord += '_'
    return guessedWord
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuwxvyz'
    availableletters = ''
    for c in alphabet:
        if c not in lettersGuessed:
            availableletters += c
    return availableletters
    

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
    secretWord = chooseWord(wordlist).lower()
    guessleft = 8
    totalGuessedletters = ''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %s letters long.' % len(secretWord))
    while guessleft>0 and not  isWordGuessed(secretWord, totalGuessedletters):
        print('--------------------------------------')
        print('You have %s guesses left.' % guessleft )
        print('Available letters: %s' % getAvailableLetters(totalGuessedletters))
        lettersGuessed = (raw_input('Please guess a letter:')).lower()
        alphabet = 'abcdefghijklmnopqrstuwxvyz'
        if len(lettersGuessed)!=1 or lettersGuessed==' ' or lettersGuessed not in alphabet:
            print'PYou entered a wrong type of entry!'
        
        else:
            if lettersGuessed in totalGuessedletters:
                print('You have already guessed that letter: %s' % getGuessedWord(secretWord, totalGuessedletters))
            else:
                totalGuessedletters += lettersGuessed
                if lettersGuessed in secretWord:
                    print  'Good guess: %s' % getGuessedWord(secretWord, totalGuessedletters)
                else:
                    print 'Oops!That letter is not in my word: %s' % getGuessedWord(secretWord, totalGuessedletters)
                    guessleft -= 1
        
            
        
        if isWordGuessed(secretWord,totalGuessedletters):
            print('Congratulations, you won!')
        if guessleft == 0 :
            print('Sorry, you ran out of guesses. The word was "%s".' % secretWord)




secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
