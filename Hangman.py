"""
Hangman Game
------------
A simple text-based Hangman game where the player guesses a word
one letter at a time.

Key Concepts Used: random, while loop, if-else, strings, lists.
"""

import random

# Predefined list of words to choose from
WORD_LIST = ["python", "hangman", "computer", "keyboard", "science"]

MAX_INCORRECT_GUESSES = 6


def choose_word(word_list):
    """Randomly select a word from the list."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORD_LIST)
    guessed_letters = []      # letters the player has already tried
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("Word: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        print("Guessed letters: " + ", ".join(guessed_letters) if guessed_letters else "Guessed letters: none")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

        # Check win condition: every letter of the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word: " + word)
            break
    else:
        # This runs only if the while loop ends without 'break' (i.e. loss)
        print("You've run out of guesses! Game over.")
        print("The word was: " + word)


if __name__ == "__main__":
    play_hangman()