#Array to track how many sections of the man to render. The index of the array should be passed 
#to the function as the game state is updated.
#Will need some kind of dictionary of words to pick from.
#Function to search for guess
#Array to keep guesses so far, initialize to array of '_' to the length of the word.
import random, wordlist, art

MAX_GUESSES = 6

class Player_State:
    word = []
    game_word = ""
    guess_count = 0
    recent_guess = ""
    guess_history = []
    game_lost = False
    hangman_state = ""
    
    def __init__(self, game_word):
        self.game_word = game_word
        self.hangman_state = art.stage[0]
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
        print_word(self.word)
        if guess_found:
            return self.set_player_word(correct_list)
        else:
            self.guess_count += 1
            self.hangman_state = art.stage[self.guess_count]
            self.guess_history.append(self.recent_guess)
            return self.word

    def set_player_word(self, correct_list):
        for num in correct_list:
            player.word[num] = player.recent_guess

def init_game():
    print("Welcome to the game of hangman!")
    print("Can you complete the word before time runs out?")
    return random.choice(wordlist.words)

def end_game(loss):
    if loss:
        print(f"Game over! You lost, the answer was {game_word}")
    else:
        print(f"Game over! You win! It was {game_word}")

def print_word(word):
    newstring = "Solve: "
    for letter in word:
        newstring += letter + " "
    print(newstring)
    print("")

game_word = init_game()
player = Player_State(game_word)
print(player.hangman_state)

while "_" in player.word:
    if player.guess_count == MAX_GUESSES:
        player.game_lost = True
        break
    print_word(player.word)
    print(f"You have used {player.guess_count} of 6 guesses and the incorrect letters {player.guess_history}")
    player.get_user_choice()
    player.check_guess()
    print(player.hangman_state)
    

end_game(player.game_lost)
