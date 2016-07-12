import random
from BaccaratRule.Card import Card

class Stack(object):
    stack = []
    def __init__(self,deck):
        for no_deck in range(1,deck+1):
            for suit in range(1,5):
                for number in range(1,14):
                    card = Card(no_deck, suit, number)
                    self.stack.append(card)

    def clean(self):
        stack = []

    def shuffle(self):
        random.shuffle(self.stack)

    def print(self):
        for card in self.stack:
            print(card)