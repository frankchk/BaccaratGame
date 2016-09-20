from baccarat_rule.hand import Hand
from baccarat_rule.card import Card
from baccarat_rule.stack import Stack

class CountCard(object):
    score_dict = {
        1 : 0,
        2 : -1,
        3 : -2,
        4 : -2,
        5 : -1,
        6 : 0,
        7 : 0,
        8 : 1,
        9 : 1,
        10 : 1,
        11 : 1,
        12 : 1,
        13 : 1
    }

    # score_dict = {
    #     1 : 0,
    #     2 : 1,
    #     3 : 2,
    #     4 : 2,
    #     5 : 1,
    #     6 : 0,
    #     7 : 0,
    #     8 : -1,
    #     9 : -1,
    #     10 : -1,
    #     11 : -1,
    #     12 : -1,
    #     13 : -1
    # }

    bet_dict = {
        0 : "banker",
        1 : "player",
        2 : "draw"
    }

    def __init__(self):
        self.count_score = 0
        self.profit = 0
        self.win = 0

    def reset_score(self):
        self.count_score = 0

    def calculate_score(self, hand : Hand):
        for card in hand.card_list:
            self.count_score += self.card_score(card)

    def card_score(self, card : Card) -> int:
        # print(card)
        # print(self.score_dict.get(card.number))
        return self.score_dict.get(card.number)

    def score(self) -> int:
        return self.count_score

    def bet(self):
        if(self.count_score < -50):
            return 0
        elif(self.count_score > 50):
            return 1
        return -1

    def clearing(self, money : int):
        self.profit += money
        if(money > 0):
            self.win += 1


# s1 = Stack(1)
# s1.print()
# hand = Hand()
# hand.add(s1.pop())
#
#
#
#
# cc = CountCard()
# cc.calculate_score(hand)
# print(cc.score())