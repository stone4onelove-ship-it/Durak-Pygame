import copy
from dataclasses import dataclass
from game.card import Card
from game.table import Table, Log


@dataclass
class UserInfo:
    id: int

    table: Table
    logs: list[Log]
    deck_len: int
    trump_card: Card
    player_hand: list[Card]
    opponent_hand_len: int

    active: int   # player id
    attacker: int # player id
    defender: int # player id



def viewpoint(self, id: int) -> UserInfo:
    return copy.deepcopy(UserInfo(
        id = id,

        table = self.table,
        logs = self.logs,
        deck_len = len(self.deck),
        trump_card = self.trump,
        player_hand = self.players[id].cards,
        opponent_hand_len = len(self.players[self.opposite_id(id)].cards),

        active = self.active,
        attacker = self.attacker,
        defender = self.defender
    ))