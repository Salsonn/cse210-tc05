from game.word import Word
import random

class Parachute:
    def __init__(self):
        self.word = Word()

    def create_graphics(self):
        sky = '__ __ __ __ __ \n\n'
        parachute = [
            [' ___'],
            ['/___\\'],
            ['\\   /'],
            ['\\ /']
            ]
        person = [
            [' 0'],
            ['/|\\'],
            ['/ \\']
        ] 
        ground = '^^^^^^^^^^^^'

    def change_layer6(self, person):
        if self.director.game_over:
            person[[0]] = '   X  \n'
            return person[[0]]
        
