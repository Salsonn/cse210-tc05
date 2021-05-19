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
        pass

    def do_updates():
        pass

    def do_outputs():
        pass
