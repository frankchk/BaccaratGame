import random
from baccarat_rule.card import Card

class Stack(object):
    def __init__(self,deck):
        self.stack = []
        for no_deck in range(1,deck+1):
            for suit in range(1,5):
                for number in range(1,14):
                    card = Card(no_deck, suit, number)
                    self.stack.append(card)

    def clean(self):
        self.stack = []

    def shuffle(self):
        random.shuffle(self.stack)

    def print(self):
        for card in self.stack:
            print(card)

    def pop(self):
        return self.stack.pop(0)

    @property
    def size(self):
        return len(self.stack)