from dataclasses import dataclass
from game import UserInfo
from card import Card, Suit


def think(user_info: UserInfo) -> int:
    # get deck ready
    cards = {}
    for i in [6,7,8,9,10,12,13,14,15]:
        for j in Suit:
            cards[Card(i, j)] = float(1)

    # check logs
    for log in user_info.logs:
        match log.status:
            case -1:
                pass
            case user_info.player:
                pass
            case _:
                pass


    print(cards)


    


    return 0

def print_info():
    pass

