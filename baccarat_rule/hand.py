from baccarat_rule.card import Card

class Hand(object):
    def __init__(self):
        self.card_list = []

    def add(self,card):
        self.card_list.append(card)

    def clean(self):
        self.card_list = []

    def card_list(self):
        return self.card_list

    def print(self):
        i = 1
        for card in self.card_list:
            print("{} : {}".format(i,card))
            i += 1

    def get_card(self, pos : int) -> Card:
        return self.card_list[pos]

    def get_size(self) -> int:
        return len(self.card_list)