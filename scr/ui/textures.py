import pygame
import sys, os
from game.card import Suit

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.SCALED)

def resource_path(relative_path: str):
    path = "assets/textures/" + relative_path
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path) # type: ignore
    return path

textures = {
    'cards' : {
        'r' : {
            15 : pygame.image.load(resource_path("nums/15r.png")).convert_alpha(),
            14 : pygame.image.load(resource_path("nums/14r.png")).convert_alpha(),
            13 : pygame.image.load(resource_path("nums/13r.png")).convert_alpha(),
            12 : pygame.image.load(resource_path("nums/12r.png")).convert_alpha(),
            10 : pygame.image.load(resource_path("nums/10r.png")).convert_alpha(),
             9 : pygame.image.load(resource_path("nums/09r.png")).convert_alpha(),
             8 : pygame.image.load(resource_path("nums/08r.png")).convert_alpha(),
             7 : pygame.image.load(resource_path("nums/07r.png")).convert_alpha(),
             6 : pygame.image.load(resource_path("nums/06r.png")).convert_alpha(),
        },
        'b' : {
            15 : pygame.image.load(resource_path("nums/15b.png")).convert_alpha(),
            14 : pygame.image.load(resource_path("nums/14b.png")).convert_alpha(),
            13 : pygame.image.load(resource_path("nums/13b.png")).convert_alpha(),
            12 : pygame.image.load(resource_path("nums/12b.png")).convert_alpha(),
            10 : pygame.image.load(resource_path("nums/10b.png")).convert_alpha(),
             9 : pygame.image.load(resource_path("nums/09b.png")).convert_alpha(),
             8 : pygame.image.load(resource_path("nums/08b.png")).convert_alpha(),
             7 : pygame.image.load(resource_path("nums/07b.png")).convert_alpha(),
             6 : pygame.image.load(resource_path("nums/06b.png")).convert_alpha(),
        },
    },
    'suits' : {
        Suit.H : pygame.image.load(resource_path("suits/h.png")).convert_alpha(),
        Suit.D : pygame.image.load(resource_path("suits/d.png")).convert_alpha(),
        Suit.S : pygame.image.load(resource_path("suits/s.png")).convert_alpha(),
        Suit.C : pygame.image.load(resource_path("suits/c.png")).convert_alpha(),
    },
    'face_down' : {
        'rd' : pygame.image.load(resource_path("cards/face_down_rd.png")).convert_alpha(),
        'db' : pygame.image.load(resource_path("cards/face_down_db.png")).convert_alpha(),
        'bl' : pygame.image.load(resource_path("cards/face_down_bl.png")).convert_alpha(),
    },
    'deck_side' : {
        'rd' : pygame.image.load(resource_path("cards/deck_side_rd.png")),
        'db' : pygame.image.load(resource_path("cards/deck_side_db.png")),
        'bl' : pygame.image.load(resource_path("cards/deck_side_bl.png")),
    },
    'empty_card'  : pygame.image.load(resource_path("cards/empty_card.png")).convert_alpha(),
    'beaten_card' : pygame.image.load(resource_path("cards/beaten_card.png")).convert_alpha(),

    'button_up'   : pygame.image.load(resource_path("button_up.png")).convert_alpha(),
    'button_down' : pygame.image.load(resource_path("button_down.png")).convert_alpha(),
    'button_act'  : pygame.image.load(resource_path("button_act.png")).convert_alpha(),
    'button_pas'  : pygame.image.load(resource_path("button_pas.png")).convert_alpha(),
    
    'loading'     : pygame.image.load(resource_path("loading.png")).convert_alpha(),
    'menu'        : pygame.image.load(resource_path("menu.png")).convert_alpha(),
    'menu_title'  : pygame.image.load(resource_path("menu_title.png")).convert_alpha(),
    'menu_button' : pygame.image.load(resource_path("menu_button.png")).convert_alpha(),
    'menu_but_red': pygame.image.load(resource_path("menu_but_red.png")).convert_alpha(),
    'pause'       : pygame.image.load(resource_path("pause.png")).convert_alpha(),
    'win_panel'   : pygame.image.load(resource_path("win_panel.png")).convert_alpha(),
    'lose_panel'  : pygame.image.load(resource_path("lose_panel.png")).convert_alpha(),
    'back_pattern': pygame.image.load(resource_path("back_pattern.png")).convert_alpha(),
    'reset'       : pygame.image.load(resource_path("reset.png")).convert_alpha(),
    'logo'        : pygame.image.load(resource_path("logo.png")).convert_alpha(),
    'block'       : pygame.image.load(resource_path("block.png")),
    'lose_fade'   : pygame.image.load(resource_path("lose_fade.png")),
    'win_fade'    : pygame.image.load(resource_path("win_fade.png")),
}


CARD_SIZE = (200, 300)

def resize_card(textures: dict, CARD_SIZE):
    textures['empty_trump'] = pygame.transform.rotate(textures['empty_card'], 90)



resize_card(textures, CARD_SIZE)