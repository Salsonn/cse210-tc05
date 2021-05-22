from game.parachute import Parachute
from game.word import Word
from game.console import Console

class Director:

    def __init__(self):
        self.parachute = Parachute()
        self.word = Word()
        self.console = Console()
        self.keep_playing = True

    def start_game(self):
        self.word = self.word.random_word()
        self.parachute.create_graphics()
        self.console.print_parachute()
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        self.console.print_parachute()
        exit()

    def get_inputs():
        self.console.user_guess()

    def do_updates():
        pass


    def do_outputs():
        self.console.print_guesses(self.word, self.console.letters)
        self.console.print_parachute()
