#Array to track how many sections of the man to render. The index of the array should be passed 
#to the function as the game state is updated.
#Will need some kind of dictionary of words to pick from.
#Function to search for guess
#Array to keep guesses so far, initialize to array of '_' to the length of the word.
import random

MAX_GUESSES = 6
word_list = ["aardvark", "baboon", "camel"]

class Player_State:
    word = []
    game_word = ""
    guess_count = 0
    recent_guess = ""
    game_lost = False
    
    def __init__(self, game_word):
        self.game_word = game_word
        for letter in game_word:
            self.word.append("_")

    def get_user_choice(self):
        self.recent_guess = input("Guess a letter: ").lower()
    
    #the correct_list list tracks the indexes in which the guess was found to update the state of player word
    def check_guess(self):
        index = 0
        correct_list = []
        guess_found = False
        for letter in game_word:
            if self.recent_guess == letter:
                guess_found = True
                correct_list.append(index)
            index += 1
        print(self.word)
        if guess_found:
            return self.set_player_word(correct_list)
        else:
            self.guess_count += 1
            return self.word

    def set_player_word(self, correct_list):
        print("set player word")
        for num in correct_list:
            player.word[num] = player.recent_guess

def init_game(word_list):
    print("Welcome to the game of hangman!")
    print("Can you complete the word before time runs out?")
    return random.choice(word_list)

def end_game(loss):
    if loss:
        print(f"Game over! You lost, the answer was {game_word}")
    else:
        print(f"Game over! You win!")

game_word = init_game(word_list)
player = Player_State(game_word)
print(player)
print(game_word)
while "_" in player.word:
    print(player.word)
    print(f"You have used {player.guess_count} of 6 guesses")
    if player.guess_count == MAX_GUESSES:
        player.game_lost = True
        break
    player.get_user_choice()
    player.check_guess()

end_game(player.game_lost)
