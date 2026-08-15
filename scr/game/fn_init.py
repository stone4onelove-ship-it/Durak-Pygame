import random
from game.card import Card, Suit


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
        trump = 20
        trump_id = -1

        for id, player in enumerate(self.players):
            for card in player.cards:
                if card.suit == self.trump.suit and card.num < trump:
                    trump = card.num
                    trump_id = id
        if trump_id == -1:
            trump_id = random.randrange(len(self.players))

        self.active = trump_id
        self.attacker = trump_id
        self.defender = self.opposite_id(trump_id)