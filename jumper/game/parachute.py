from game.word import Word
import random

class Parachute:
    def __init__(self):
        self.word = Word()
        self.parachute = [
            ' ___',
            '/___\\',
            '\\   /',
            ' \\ /'
            ]
        self.person = [
            '  0',
            ' /|\\',
            ' / \\'
        ] 
        self.ground = '^^^^^^^^^^^^'

    def create_graphics(self):
        sky = '__ __ __ __ __ \n\n'
        parachute = [
            [' ___'],
            ['/___\\'],
            ['\\   /'],
            ['\\ /']
            ]
        person = [
            ' 0',
            '/|\\',
            '/ \\'
        ] 
        ground = '^^^^^^^^^^^^'
