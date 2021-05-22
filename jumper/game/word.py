import random

class Word:
    def __init__(self):
        randomized_word = self.random_word()
        return randomized_word

    def random_word(self):
        with open('jumper\game\words.csv', 'rt') as file:
            empty_array = []
            for i in file:
                empty_array.append(i)
            random_word = random.choice(empty_array)
            random_word = random_word.strip('\n')
            return random_word