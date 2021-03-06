# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"
STORY_FILENAME = "story.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open(STORY_FILENAME, "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    count = 0 
    Dict = {}
    for i in range(len(string.ascii_lowercase)):
        if i+shift < len(string.ascii_lowercase):
            Dict[string.ascii_lowercase[i]] = string.ascii_lowercase[i+shift]
            Dict[string.ascii_uppercase[i]] = string.ascii_uppercase[i+shift] 
        else:
            Dict[string.ascii_lowercase[i]] = string.ascii_lowercase[count]
            Dict[string.ascii_uppercase[i]] = string.ascii_uppercase[count]
            count += 1 
   
    return Dict # Remove this comment when you code the function

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    newtext = ""
    for c in text:
        newtext += coder.get(c, c)
    ### TODO.
    return newtext # Remove this comment when you code the function

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    shifted_text = applyCoder(text, buildCoder(shift))
    return shifted_text # Remove this comment when you code the function

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    bestshift = 0 
    mostword = 0
    for shift in range(26):
        word_count = 0
        for word in text.split(" "):
            shiftedword = applyShift(word, shift)
            if(isWord(wordList, shiftedword)):
                 word_count += 1
        if (mostword < word_count ):
            mostword = word_count
            bestshift = shift        
    
    return bestshift # Remove this comment when you code the function

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    story = getStoryString()
    BestShift = findBestShift(wordList, story)
    true_story = applyShift(story, BestShift)
    return true_story # Remove this comment when you code the function

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    print s
    bestShift = findBestShift(wordList, s)
    print applyShift(s, bestShift) == 'Hello, world!'
    print decryptStory()
