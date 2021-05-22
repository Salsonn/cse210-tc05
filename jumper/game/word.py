import random

class Word:
    def __init__(self):
        self.random_word = self.random_word()
        self.incorrect_guesses = 0
        self.guessed = False
        self.correct_letters = []

    def random_word(self):
        with open('jumper\game\words.csv', 'rt') as file:
            empty_array = []
            for i in file:
                empty_array.append(i)
            random_word = random.choice(empty_array)
            random_word = random_word.strip('\n')
            return random_word
    
    def word_guessed(self):
        if len(self.correct_letters) == self.random_word:
            self.guessed = True

    def letter_wrong(self, word, guess):
        if guess not in word:
            self.incorrect_guesses += 1
        else:
            self.correct_letters.append(guess)