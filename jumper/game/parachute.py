from game.letter import Letter

class Parachute:
    def __init__(self):
        self.letter = Letter()

    def create_graphics(self):
        sky = '__ __ __ __ __ \n\n'
        parachute_layer1 = ' ______\n'
        parachute_layer2 = '/\t\\\n'
        parachute_layer3 = ' ____\n'
        parachute_layer4 = '\\   /\n'
        parachute_layer5 = '\\  /\n'
        parachute_layer6 = '   0  \n'
        parachute_layer7 = '/ | \\\n'
        parachute_layer8 = '/  \\\n\n'
        ground = '^^^^^^^^^^^^'

    def change_layer6(self):
        if self.director.game_over:
            parachute_layer6 = '   X  \n'
            return parachute_layer6