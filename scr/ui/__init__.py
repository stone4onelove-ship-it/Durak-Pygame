from game.card import Card, Suit
from game import Game
from ui.textures import textures
import pygame

pygame.init()

class Ui:
    def __init__(self, game: Game):
        self.screen: pygame.Surface = pygame.display.set_mode((1920, 1080), pygame.SCALED, pygame.FULLSCREEN)
        self.game: Game = game

        self.font = pygame.font.Font(None, 36)
        

    def update(self):
        self.screen.fill((35,35,35))

        self.draw_player_deck((550,850))
        self.draw_opponent_deck((550, 10))
        self.draw_table((450, 400))
        self.draw_deck((100,450))
        self.draw_info((10, 10))


    def draw_deck(self, pos: tuple[float,float]):
        # trump
        if self.game.deck:
            self.draw_card(self.game.deck[0], (pos[0] + 75, pos[1] + 35), 85)
        # deck
            if len(self.game.deck) > 1:
                self.screen.blit(textures['deck_side']['rd'], (pos[0] + 10, pos[1] + 10))
                self.screen.blit(textures['deck_side']['rd'], (pos[0] + 5, pos[1] + 5))
                self.screen.blit(textures['face_down']['rd'], pos)
        


    def draw_table(self, pos: tuple[float,float]):
        for card_pair in self.game.table.cards:
            self.draw_card(card_pair[0], (pos[0], pos[1] + 80))
            if len(card_pair) > 1:
                self.draw_card(card_pair[1], (pos[0] + 50, pos[1]))
            pos = (pos[0] + 130, pos[1])
    

    def draw_opponent_deck(self, pos: tuple[float,float]):
        OPEN_VIEW = False
        for card in self.game.players[0].cards:
            if OPEN_VIEW:
                self.draw_card(card, pos)
            else:
                self.screen.blit(textures['face_down']['rd'], pos)
            pos = (pos[0] + 120, pos[1])

            

    def draw_player_deck(self, pos: tuple[float,float]):
        angle = 15


        for card in self.game.players[1].cards:
            self.draw_card(card, pos, angle)
            pos = (pos[0] + 120, pos[1])
            angle -= 5
    

    def draw_card(self, card: Card, pos: tuple[float,float], angle=0):
        angle = 0
        if angle:
            empty = pygame.transform.rotate(textures['empty_card'], angle)
            color = 'r' if card.suit in (Suit.H, Suit.D) else 'b'
            num = pygame.transform.rotate(textures['cards'][color][card.num], angle)
            suit = pygame.transform.rotate(textures['suits'][card.suit], angle)
        else:
            empty = textures['empty_card']
            num = textures['cards']['r' if card.suit in (Suit.H, Suit.D) else 'b'][card.num]
            suit = textures['suits'][card.suit]

        self.screen.blit(empty, pos)
        self.screen.blit(num, pos)
        self.screen.blit(suit, (pos[0] + 8, pos[1] + 65))


    def draw_info(self, pos: tuple[float,float]):
        text = self.font.render(f"{self.game.brain}", True, (255, 255, 255))
        self.screen.blit(text, pos)
        text = self.font.render(f"{self.game}", True, (255, 255, 255))
        self.screen.blit(text, (pos[0], pos[1] + 35))



class UiAllCards:
    def __init__(self, screen: pygame.Surface, game: Game):
        self.screen = screen
        self.game = game

        self.cards: set[UiCard] = set()

        self.PLAYER_CARDS_POS = (550,850)
        self.TABLE_POS = (450, 400)

        self.update()

    def update(self):
        pass






class UiCard:
    def __init__(self, screen: pygame.Surface, card: Card, pos: tuple[float,float], angle=0):
        self.screen = screen
        self.surface = self.create_surface()

        self.suit = card.suit
        self.num = card.num

        self.pos = pos
        self.angle = angle

        self.real_pos = pos
        self.real_angle = angle

        self.CARD_SIZE = (200, 300)


    def create_surface(self) -> pygame.Surface:
        combined = pygame.Surface(self.CARD_SIZE, pygame.SRCALPHA)
        combined.blit(textures['empty_card'], (0, 0))
        color = 'r' if self.suit in (Suit.H, Suit.D) else 'b'
        combined.blit(textures['cards'][color][self.num], (0, 0))
        combined.blit(textures['suits'][self.suit], (8, 65))

        upside_down_num = pygame.transform.rotate(textures['cards'][color][self.num], 180)
        upside_down_suit = pygame.transform.rotate(textures['cards'][color][self.num], 180)
        combined.blit(upside_down_num, self.CARD_SIZE)
        combined.blit(upside_down_suit, (self.CARD_SIZE[0] - 8, self.CARD_SIZE[1] - 65))

        return combined


    def change(self, pos=None, angle=None):
        if pos:
            self.pos = pos
        if angle:
            self.angle = angle



    def update(self):
        if self.pos != self.real_pos:
            pass

        if self.angle != self.real_angle:
            pass

        empty = pygame.transform.rotate(textures['empty_card'], self.real_angle)
        color = 'r' if self.suit in (Suit.H, Suit.D) else 'b'
        num = pygame.transform.rotate(textures['cards'][color][self.num], self.real_angle)
        suit = pygame.transform.rotate(textures['suits'][self.suit], self.real_angle)

        self.screen.blit(empty, self.real_pos)
        self.screen.blit(num, self.real_pos)
        self.screen.blit(suit, self.real_pos)



    def __eq__(self, other):
        return self.num == other.num and self.suit == other.suit

    def __hash__(self):
        return hash((self.num, self.suit))
