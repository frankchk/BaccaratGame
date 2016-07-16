from baccarat_rule.hand import Hand
from baccarat_rule.card import Card

def hand_score(hand : Hand) -> int:
    hand_score = 0
    for card in hand.card_list:
        hand_score += card_score(card)
    return hand_score%10

def card_score(card : Card) -> int:
    if card.number > 9:
        return 0
    return card.number

def is_player_draw_3rd(player_hand : Hand, banker_hand : Hand) -> bool:
    if hand_score(player_hand) <= 5 and hand_score(banker_hand) < 8:
        return True
    return False

def is_banker_draw_3rd(player_hand : Hand, banker_hand : Hand) -> bool:
    player_score = hand_score(player_hand)
    banker_score = hand_score(banker_hand)
    if len(player_hand.card_list) < 3:
        if player_score < 8 and banker_score <= 5:
            return True
        else:
            return False
    else:
        player_3rd_card_score = card_score(player_hand.get_card(2))
        if banker_score <= 2:
            return True
        elif banker_score == 3:
            if player_3rd_card_score != 8:
                return True
            else:
                return False
        elif banker_score == 4:
            if player_3rd_card_score in [2,3,4,5,6,7]:
                return True
            else:
                return False
        elif banker_score == 5:
            if player_3rd_card_score in [4,5,6,7]:
                return True
            else:
                return False
        elif banker_score == 6:
            if player_3rd_card_score in [6,7]:
                return True
            else:
                return False
        else:
            return False


