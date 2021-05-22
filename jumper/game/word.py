import random

class Word:
    def __init__(self):
        self.random_word = self.random_word()
        self.incorrect_guesses = 0
        self.guessed = False
        self.correct_guesses = []

    def random_word(self):
        with open('jumper\game\words.csv', 'rt') as file:
            empty_array = []
            for i in file:
                empty_array.append(i)
            random_word = random.choice(empty_array)
            random_word = random_word.strip('\n')
            return random_word

    
    def word_guessed(self):
        random_word = "".join(set(self.random_word))
        if len(random_word) == len(self.correct_guesses):
            return False
        else:
            return True

    def letter_wrong(self, word, guess):
        if guess not in word:
            self.incorrect_guesses += 1
        else:
            self.correct_guesses.append(guess)