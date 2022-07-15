# Hangman game

import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guesses = []
    for i in secretWord:
        guesses.append( i )
    message = ""
    count = 0
    j = 0
    letter = ""
    if len( lettersGuessed ) == 0:
        message = False
        return message
    while True:
        if guesses[count] == lettersGuessed[j]:
            letter += guesses[count]
            #remove to avoid detecting duplicates
            lettersGuessed.pop( j )
            j = 0
            if (len( guesses ) - 1) != count:
                count += 1
            else:
                pass
            if len( letter ) == (len( guesses )):
                message = True
                break
        else:
            j += 1
            if j == len( lettersGuessed ):
                j = 0
                length = len( guesses ) - 1
                if count == length:
                    message = False
                    break
                else:
                    count += 1
    return message

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guesses = []
    correct_guess = []
    for i in secretWord:
        guesses.append( i )
    count = 0
    j = 0
    empty_count=0# if letterguessed is empty
    letter = ""
    if len( lettersGuessed ) == 0:
        while True:
            correct_guess.append( "_" )
            empty_count += 1
            if empty_count == len( secretWord ):
                return "".join( correct_guess )
    while True:
        if guesses[count] == lettersGuessed[j]:
            letter += guesses[count]
            correct_guess.append( guesses[count] )
            j = 0
            if (len( guesses )-1) != count:
                count += 1
            else:
                break
            if len( letter ) == (len( guesses )):
                break
        else:
            j += 1
            if j == len( lettersGuessed ):
                correct_guess.append( "_" )
                j = 0
                length = len( guesses )-1
                if count == length:
                    break
                else:
                    count += 1

    return "".join( correct_guess )


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    message = ""
    count = 0
    j = 0
    alphabet = []
    letter = ""
    if len( lettersGuessed ) == 0:
        return string.ascii_lowercase
    while True:
        if string.ascii_lowercase[count] == lettersGuessed[j]:
            letter += string.ascii_lowercase[count]
            j = 0
            if (len( string.ascii_lowercase ) - 1) != count:
                count += 1
            else:
                break
            if len( letter ) == len( string.ascii_lowercase ):
                message = "True"
                break
        else:
            j += 1
            if j == len( lettersGuessed ):
                j = 0
                alphabet.append( string.ascii_lowercase[count] )
                length = len( string.ascii_lowercase ) - 1
                if count == length:
                    message = "False"
                    break
                else:
                    count += 1

    return "".join( alphabet )
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    '''
    print( "Welcome to the game of Hangman!" )
    print( "I am thinking of a word that is", len( secretWord ), "letters long" )
    print( "-------------" )
    # print(secretWord)
    lettersGuessed=[]
    mistakes=[]
    correct_guesses=[]
    available_guesses = 8
    while secretWord!=0:
        print("You have",available_guesses,"guesses left")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        letter=input("Please guess a letter: ")
        lettersGuessed.append(letter)
        if letter in correct_guesses:
            print( "Oops! You've already guessed that letter:", getGuessedWord( secretWord, lettersGuessed ) )
            print( "-------------" )

        elif letter in getGuessedWord(secretWord,lettersGuessed):
            correct_guesses.append(letter)
            print( "Good guess:", getGuessedWord( secretWord, lettersGuessed ) )
            print( "-------------" )

        if letter in mistakes:
            print( "Oops! You've already guessed that letter:", getGuessedWord( secretWord, lettersGuessed ) )
            print( "-------------" )

        elif letter not in getGuessedWord(secretWord,lettersGuessed):
            mistakes.append(letter)
            print("Oops! That letter is not in my word:",getGuessedWord( secretWord, lettersGuessed ))
            print( "-------------" )
            available_guesses-=1

        if getGuessedWord(secretWord,lettersGuessed)==(secretWord):
            if isWordGuessed(secretWord,lettersGuessed)==True:
                print('Congratulations, you won!')
                break
        if available_guesses==0:
            print("Sorry, you ran out of guesses. The word was",secretWord)
            break


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
