from os import times
from game.parachute import Parachute

class Console:
    '''
    Runs 2 methods
    
    print_guesses, which takes the guesses
    of the user as a list, and the word that was generated

    print_parachute prints the parachute based on how many 
    times a user got an entry incorrect 
    '''
    
    def __init__(self):
        self.letters = []
        self.parachute = Parachute()

    def user_guess(self):
        letter_in_array = True
        while letter_in_array:
            letter_guess = input("What letter do you wish to guess? ").lower()
            if letter_guess not in self.letters:
                letter_in_array = False
            else:
                print('That letter has already been guessed!')
        self.letters.append(letter_guess)
        return self.letters

    def print_guesses(self, randomized_word, list_of_letters_guessed):
        i = 0
        while i != len(randomized_word):
            letter_guessed = False

            for n in list_of_letters_guessed:
                if n == randomized_word[i]:
                    letter_guessed = True
            
            if letter_guessed:
                print(f'{randomized_word[i]} ', end="")
            
            else:
                print('_ ', end="")
            i += 1
        print()

    def print_parachute(self, times_user_was_wrong):
        for i in range(times_user_was_wrong, len(self.parachute.parachute)):
            print(self.parachute.parachute[i])
        for i in range(len(self.parachute.person)):
            if times_user_was_wrong == 5:
                self.parachute.person[0] = '  X'
            print(self.parachute.person[i])
        print(self.parachute.ground)
