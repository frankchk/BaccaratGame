class Card(object):
    deck = 0
    suit = 0
    number = 0

    suit_dict = {
        1: "S",
        2: "H",
        3: "C",
        4: "D"
    }

    number_dict = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K"
    }

    def get_str(self):
        return "["+str(self.deck)+"]"+self.suit_dict.get(self.suit)+self.number_dict.get(self.number)

    def __init__(self, deck, suit, number):
        self.deck = deck
        self.suit = suit
        self.number = number

    def __lt__(self, other):
        if self.number < other.number:
            return True
        elif self.number > other.number:
            return False
        else:
            if self.suit > other.suit:
                return True
            else:
                return False

    def __eq__(self, other):
        return not self < other and not other < self

    def __ne__(self, other):
        return self < other or other < self

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not other < self

    def __str__(self):
        return self.get_str()
