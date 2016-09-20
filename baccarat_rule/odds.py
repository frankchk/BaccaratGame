

class Odds(object):
    odds_dict = {
       -1 : -100,
        0 : 95,
        1 : 100,
        2 : 800
    }

    def case(situation : int) -> int:
        return Odds.odds_dict.get(situation)