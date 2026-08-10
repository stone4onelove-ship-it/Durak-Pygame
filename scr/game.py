import random
from card import Card, Suit
from dataclasses import dataclass
import copy


@dataclass
class UserInfo:
    table: Table
    logs: list[Log]
    deck_len: int
    trump_card: Card
    player_hand: list[Card]
    opponent_hand_len: int

    active: int   # player id
    attacker: int # player id
    defender: int # player id

    player: int
    

    



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
        elif len(self.cards) < 6 or (len(self.cards) <= 6 and first_pile) and \
        any(c.num == card.num for c in sum(self.cards, [])):
            return True
        return False

    def can_defend(self, card: Card, trump: Suit) -> bool:
        if len(self.cards[-1]) == 1:
            if self.cards[-1][0].suit == card.suit and self.cards[-1][0].num < card.num:
                return True
            elif card.suit == trump and self.cards[-1][0].suit != trump:
                return True
        return False

    def can_pass(self, card: Card):
        pass



class Player:
    def __init__(self):
        self.cards: list[Card] = []


class Game:
    def __init__(self, passing: bool):
        self.table: Table = Table()
        self.players: list[Player] = [Player(),Player()]
        self.deck: list[Card] = []
        self.trump: Card

        self.logs: list[Log] = []
        self.has_pile: bool = False

        self.active: int # player id
        self.attacker: int # player id
        self.defender: int # player id

        self.passing: bool = passing


    def init(self):
            # create and shuffle the deck
            for i in [6,7,8,9,10,12,13,14,15]:
                for j in Suit:
                    self.deck.append(Card(i, j))

            running = True
            while running:
                # shuffle the deck
                random.shuffle(self.deck)
                running = False

                # fill player's hands
                for player in self.players:
                    player.cards = self.deck[:6]
                    del self.deck[:6]

                    # if more than 4 card are the same suit
                    for suit in Suit:
                        amount = 0
                        for card in player.cards:
                            if card.suit == suit:
                                amount += 1
                        if amount >= 5:
                            running = True

            

            # set the trump card and sort cards
            self.trump = self.deck[0]
            self.sort_cards()

            # find who moves first
            high_trump = 0
            high_trum_id = -1

            for id, player in enumerate(self.players):
                for card in player.cards:
                    if card.suit == self.trump.suit and card.num > high_trump:
                        high_trump = card.num
                        high_trum_id = id
            if high_trum_id == -1:
                high_trum_id = random.randrange(len(self.players))


            self.active = high_trum_id
            self.attacker = high_trum_id
            self.defender = self.opposite_id(high_trum_id)



    def reset_match(self, status: int):
        
        # if cards gone into pile
        if status == -1:
            self.has_pile = True
            # change attack player
            self.defender, self.attacker = self.attacker, self.defender
        else:
            for cards in self.table.cards:
                self.players[status].cards.extend(cards)
        # add Logs
        self.logs.append( Log(
            table = copy.deepcopy(self.table),
            status = status
        ))
        # clean the table
        self.table = Table()
        self.active = self.attacker
        # grab cards
        self.grab_cards()



    
    def grab_cards(self):
        # previous attacker grabs first
        while self.deck and len(self.players[self.attacker].cards) < 6:
            self.players[self.attacker].cards.append(self.deck.pop())
        # previous defender grabs last
        while self.deck and len(self.players[self.defender].cards) < 6:
            self.players[self.defender].cards.append(self.deck.pop())
        self.sort_cards()



    def sort_cards(self):
        # divide by suit
        for player in self.players:
            sorted = [[],[],[],[]]
            for card in player.cards:
                sorted[card.suit.value].append(card)

            # sort individualy
            for sorted_suits in sorted:
                sorted_suits.sort(key=lambda card: card.num)

            # move trump card to the front
            sorted.append(sorted.pop(self.trump.suit.value))
            player.cards = sum(sorted, [])




    def play(self, index: int):
        match self.active:
            case self.attacker as id: 

                # end attack
                if index == -1 and len(self.table.cards) > 0:
                    self.reset_match(-1)

                # add cards
                elif self.table.can_attack(self.players[id].cards[index], self.has_pile):
                    self.table.cards.append([self.players[id].cards.pop(index)])
                    # change active
                    self.active = self.defender

            case self.defender as id: 

                # grab table cards
                if index == -1:
                    self.reset_match(self.defender)

                # defend last attack card
                elif self.table.can_defend(self.players[id].cards[index], self.trump.suit):
                    self.table.cards[-1].append(self.players[id].cards.pop(index))
                    # change active
                    self.active = self.attacker


    def opposite_id(self, id: int) -> int:
        return 0 if id == 1 else 1



    def get_user_info(self, id: int) -> UserInfo:
        return copy.deepcopy(UserInfo(
            table = self.table,
            logs = self.logs,
            deck_len = len(self.deck),
            trump_card = self.trump,
            player_hand = self.players[id].cards,
            opponent_hand_len = len(self.players[self.opposite_id(id)].cards),

            active = self.active,
            attacker = self.attacker,
            defender = self.defender,

            player = id
        ))




    def print_info(self):
        print()
        print()
        print()
        print()
        print(f"deck length: {len(self.deck)}")
        print(f"trump card: {self.deck[0]}")
        print()
        print(f"active player: {self.active}")
        print()
        print(f"player 0: {self.players[0].cards}")
        print()
        print(f"table : {self.table.cards}")
        print()
        print(f"player 1: {self.players[1].cards}")
        

    
        

