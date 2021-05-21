import random
import os

word_file = 'words.csv'

class Word:
    def __init__(self):
        randomized_word = self.random_word()

    def random_word(self):
        PATH = os.path.dirname(os.path.abspath(__file__))
        MESSAGES = open(PATH + "/words.csv").read().splitlines()
        #with open('jumper\game\words.csv', 'r') as file:
        empty_array = []
        for i in MESSAGES:
            empty_array.append(i)
        random_word = random.choice(empty_array)
        random_word = random_word.strip('\n')
        return random_word
    def guessed_word(self):
        self.list_of_letters_guessed = 0