from game import UserInfo
from game.card import Card, Suit

def opposite_id(id: int) -> int:
    return 0 if id == 1 else 1



class Brain:
    def __init__(self):
        self.free_cards: set[Card] = set()
        self.opponent_cards: set[Card] = set()

        self.sorted_free_cards: dict[int, list[Card]] = {}
        self.sorted_opponent_cards: list[Card] = []


    def think(self, user: UserInfo) -> int:
        # get deck ready
        free_cards = set()
        for i in (6,7,8,9,10,12,13,14,15):
            for j in Suit:
                free_cards.add(Card(i, j))

        # withdraw player's cards
        free_cards -= set(user.player_hand)

        # check logs
        opponent_cards = set()
        for log in user.logs:
            played_cards: set = set(sum(log.table.cards, []))

            if log.status == -1:
                free_cards -= played_cards
                opponent_cards -= played_cards

            elif log.status == user.id:
                free_cards -= played_cards
                opponent_cards -= played_cards
                
            elif log.status == (0 if user.id == 1 else 1):
                free_cards -= played_cards
                opponent_cards |= played_cards

        self.free_cards = free_cards
        self.opponent_cards = opponent_cards


        return 0



    def __str__(self):
        return f"""\n
Free cards : {self.free_cards}
Opponent cards : {self.opponent_cards}
\n"""


    def sort(self) -> None:
        sorted_free_cards = {
            15: [],
            14: [],
            13: [],
            12: [],
            10: [],
             9: [],
             8: [],
             7: [],
             6: [],
        }
        for card in self.free_cards:
            sorted_free_cards[card.num].append(card)


        

