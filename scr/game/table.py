from dataclasses import dataclass
from game.card import Card, Suit



@dataclass
class Log:
    table: Table
    status: int



class Table:
    def __init__(self):
        self.cards: list[list[Card]] = []

    def can_attack(self, card: Card, first_pile: bool) -> bool:
        if len(self.cards) == 0:
            return True
        elif (len(self.cards) < 6 or (len(self.cards) <= 6 and first_pile)) and \
        any(c.num == card.num for c in sum(self.cards, [])):
            print(self.cards)
            print(card)
            print("WOrked 2")
            return True
        return False

    def can_defend(self, card: Card, trump: Suit) -> bool:
        if len(self.cards[-1]) == 1:
            if self.cards[-1][0].suit == card.suit and self.cards[-1][0].num < card.num:
                return True
            elif card.suit == trump and self.cards[-1][0].suit != trump:
                return True
        return False