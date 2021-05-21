from game.word import Word

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
        print(sky, parachute, person, ground)

    def change_layer6(self):
        if self.director.game_over:
           person[[0]] = ' X \n'
        return parachute_layer6