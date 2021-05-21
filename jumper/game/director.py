# TODO: Create Director Class here
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
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs():
        console.get_guess() # either store this in the Classes variable or make one in director to return to

    def do_updates():
        parachute.check_parachute(console.last_guess) # sends latest guess to parachute to see what happens

    def do_outputs():
        console.print_parachute