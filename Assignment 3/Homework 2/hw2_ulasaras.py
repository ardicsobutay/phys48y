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
    print "Congratulations! Secret word was %s." % secretWord
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    for c in secretWord:
        if c in lettersGuessed:
            word += c
        else:
            word += "_"
    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    full = "abcdefghijklmnopqrstuvwxyz"
    availableLetters = ""
    for c in full:
        if c not in lettersGuessed:
            availableLetters += c
    return availableLetters
        

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
    totalGuesses = 8
    end = False
    guesses = ""
    
    while end == False and totalGuesses > 0:
        print "Guesses Remaining: ", totalGuesses
        print "Available Letters: ",getAvailableLetters(guesses)
        print "Secret Word:", getGuessedWord(secretWord, guesses)
        guess = raw_input("Guess a letter> ")
        if len(guess) == 1 and guess in "abcdefghijklmnopqrstuvwxyz":
            if guess in guesses:
                print "You have already guessed %c." % guess
                continue
            else: 
                if guess in secretWord:
                    print "Correct!"
                else:
                    print "Incorrect!"
                    totalGuesses -= 1
                guesses += guess
                end = isWordGuessed(secretWord, guesses)
        else:
            print "You must guess one letter at a time."
            continue
            
    if totalGuesses <= 0:
            print "You're out of guesses. Secret word was %s." % secretWord

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord = "ananza"
hangman(secretWord)
