from words import *
from random import randint

def possible_gallows():
    '''
    Returns a tuple of all possible gallows.
    '''
    
    gallows = ("--------\n"
               "|      \n"
               "|      \n"
               "|     \n"
               "|     \n"
               "|\n"
               "----\n",
               "--------\n"
               "|      |\n"
               "|      \n"
               "|     \n"
               "|     \n"
               "|\n"
               "----\n",
               "--------\n"
               "|      |\n"
               "|      O\n"
               "|     \n"
               "|     \n"
               "|\n"
               "----\n",
               "--------\n"
               "|      |\n"
               "|      O\n"
               "|     /\n"
               "|     \n"
               "|\n"
               "----\n",
               "--------\n"
               "|      |\n"
               "|      O\n"
               "|     /|\n"
               "|     \n"
               "|\n"
               "----\n",
               "--------\n"
               "|      |\n"
               "|      O\n"
               "|     /|\\\n"
               "|     \n"
               "|\n"
               "----\n",
               "--------\n"
               "|      |\n"
               "|      O\n"
               "|     /|\\\n"
               "|     /\n"
               "|\n"
               "----\n",
               "--------\n"
               "|      |\n"
               "|      O\n"
               "|     /|\\\n"
               "|     / \\\n"
               "|\n"
               "----\n")
    return gallows

def get_word(words):
    '''
    Takes a list of words as a parameter and randomly returns one word from 
    that list.
    '''
    word = words[randint(0, len(words))]
    return word

def enter_guess():
    '''
    Prompts the user to enter a single letter and error checks to ensure that 
    exactly 1 alphabetic character is entered. The single letter will be 
    returned.
    '''
    letter = input("\nEnter a letter: ")
    while not letter.isalpha() or len(letter) != 1:
        letter = input("Please enter 1 and only 1 letter: ")
    return letter

def hangman(word):
    '''
    Takes a string (a target word) as a parameter. Displays the intial gallows
    and the number of underscores in the target word. If the target word has not
    been guessed and the user has not guessed 7 letters incorrectly call 
    enter_guess. If the letter is not in the target word increment a counter 
    that keeps track of the incorrect guesses and adds one piece to the
    gallows. If the letter is in the target word replace the underscores in 
    the location of the letter with that letter. Once the target word has been
    guessed or the user guesses 7 incorrect letters, display the results. 
    '''
    gallows = possible_gallows()   
    letters_guessed = []
    incorrect_guesses = 0
    reconstruction = list('_' * len(word))

    print(gallows[incorrect_guesses])
    print('_' * len(word))
    
    while incorrect_guesses < 7 and "".join(reconstruction) != word:
        guess = enter_guess()
        letters_guessed.append(guess)        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    reconstruction[i] = guess            
        else:
            incorrect_guesses += 1
        print(gallows[incorrect_guesses] + '\n' + "".join(reconstruction), '\t' 
              + "letters guessed:", ", ".join(letters_guessed))
    if incorrect_guesses == 7:
        print("Sorry, you took more than the allowed 7 incorrect guesses -", 
              f"\nthe answer was '{word}'")
    else:
        print(f"You took {len(letters_guessed)} guesses to guess '{word}'")

def main():
    word = get_word(words)
    hangman(word)