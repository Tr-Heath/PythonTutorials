#Array to track how many sections of the man to render. The index of the array should be passed 
#to the function as the game state is updated.
#Will need some kind of dictionary of words to pick from.
#Function to search for guess
#Array to keep guesses so far, initialize to array of '_' to the length of the word.
import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]
game_word = ""


def init_game(word_list):
    print("Welcome to the game of hangman!")
    print("Can you complete the word before time runs out?")
    return random.choice(word_list)

def init_player(game_word):
    player_word = []
    for letter in game_word:
        player_word.append("_")
    return player_word

def get_user_choice():
    guess = input("Guess a letter: ").lower()
    return guess

#the correct_list list tracks the indexes in which the guess was found to update the state of player word
def check_guess(guess, player_word, game_Word):
    index = 0
    correct_list = []
    guess_found = False
    for letter in game_word:
        if guess == letter:
            guess_found = True
            correct_list.append(index)
        index += 1
    print(correct_list)
    if guess_found:
        set_player_word(player_word, correct_list, guess)

def set_player_word(player_word, correct_list, guess):
    for num in correct_list:
        player_word[num] = guess
    return player_word

game_word = init_game(word_list)
player_word = init_player(game_word)
print(player_word)
guess = get_user_choice()
check_guess(guess, player_word, game_word)
print(player_word)
