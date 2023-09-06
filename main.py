from words import words
import random
import string


def get_valid_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, 'lives left and used these letters: ', ' '.join(used_letter))

        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word is: ', ' '.join(word_list))

        user_letter = input('Please enter a letter: ').upper()
        if user_letter in alphabet:
            if user_letter not in used_letter:
                used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print("Letter is not in the word!")
        
        elif user_letter in used_letter:
            print("You've already used this letter.")
        else:
            print("Invalid character. Please try again!")
    
    if lives == 0:
        print('You died! Sorry the word was: ', word)
    else:
        print('You guessed the correct word: ', word)
hangman()