from baccarat_rule.stack import Stack
from baccarat_rule.hand import Hand
from baccarat_rule.card import Card
from baccarat_flow.utility import *



player_win_count = 0
banker_win_count = 0
draw_count = 0
match_counter = 0

for i in range(10000):
    print("8 deck : {}".format(i+1))
    s1 = Stack(8)
    s1.shuffle()
    s1.print()
    while s1.size() > 6:
        match_counter += 1
        print("\n")
        print("round {}".format(match_counter))


        banker_hand = Hand()
        player_hand = Hand()

        player_hand.add(s1.pop())
        banker_hand.add(s1.pop())
        player_hand.add(s1.pop())
        banker_hand.add(s1.pop())

        print("player : ")
        player_hand.print()
        print("score : {}".format(hand_score(player_hand)))
        print("banker : ")
        banker_hand.print()
        print("score : {}".format(hand_score(banker_hand)))
        if is_player_draw_3rd(player_hand,banker_hand):
            player_hand.add(s1.pop())
        if is_banker_draw_3rd(player_hand,banker_hand):
            banker_hand.add(s1.pop())
        if len(player_hand.card_list) > 2 or len(banker_hand.card_list) > 2:
            print("\nAfter drawing 3rd cards")
            print("player : ")
            player_hand.print()
            print("score : {}".format(hand_score(player_hand)))
            print("banker : ")
            banker_hand.print()
            print("score : {}".format(hand_score(banker_hand)))


        if hand_score(banker_hand) > hand_score(player_hand):
            print("banker win")
            banker_win_count += 1
        else:
            if hand_score(banker_hand) < hand_score(player_hand):
                print("player win")
                player_win_count += 1
            else:
                print("draw")
                draw_count += 1

print("--------------------------------------------")
print("total match : {}".format(match_counter))
print("banker win : {}".format(banker_win_count))
print("player win : {}".format(player_win_count))
print("draw : {}".format(draw_count))