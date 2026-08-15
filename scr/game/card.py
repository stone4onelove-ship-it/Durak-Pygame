from enum import Enum

class Suit(Enum):
    D = 0
    H = 1
    S = 2
    C = 3

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)



class Card:
    def __init__(self, num: int, suit: Suit):
        self.suit = suit
        self.num = num
        
    def __str__(self):
        return f"{self.num}{self.suit}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.num == other.num and self.suit == other.suit
    
    def __hash__(self):
        return hash((self.num, self.suit))
