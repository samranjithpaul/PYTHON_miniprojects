import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)  # it will chose randomly from the file
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)   # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()      # what the user has guessed

    lives =6

    # getting user input
    while len(word_letters) > 0 and  lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('you have',lives,'lives','\n\nYou have used these letters: ',  ' '.join(used_letters))

        # what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word:',' '.join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters: # if the letter is not used
            used_letters.add(user_letter) 

            if user_letter in word_letters:
                word_letters.remove(user_letter) 
                print('')
            else:
                lives = lives - 1
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        
        
        else:
            print("invslid chracater. Please try again.")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print ('you dies ,sorry',lives)
        print('The word was',word)
    else:
        print('You guessed the word',word,'!!')

if __name__ == '__main__':
    hangman()