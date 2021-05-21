from game.parachute import Parachute

# parachute = [
#     [' ___'],
#     ['/___\\'],
#     ['\\   /'],
#     ['\\ /']
# ]
# person = [
#     [' 0'],
#     ['/|\\'],
#     ['/ \\']
# ] 

class Console:
    def __init__(self, times_user_was_wrong, randomized_word, list_of_letters_guessed):
        
        self.print_guesses(randomized_word, list_of_letters_guessed)
        self.print_parachute(times_user_was_wrong, )
    
    def print_guesses(self, random_word, list_of_letters_guessed):
        i = 0
        while i != len(random_word):
            ### Check for i while it's the same length as the word
            ### If the letter returns equal to a guess, return that letter followed by a space
            ### Otherwise return an Underscore followed by a space 
            pass

    def print_parachute(self, times_user_was_wrong):
        print(self.parachute.create_graphics())


