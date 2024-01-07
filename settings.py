import pygame


def change_mode(value):
    global mode
    mode = value


def change_num(value):
    global num
    num = value


level_map2 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXX                XX                                                                        XXXXXXXXXXXXXXXXXXX',
    'XXXXX                XX2                                                   XX XX               XXXXXXXXXXXXXXXXXXX',
    'XXXXX  X PXXXXXX   M XXXX    XXXK                                         XXX XX K   X         XXXXXXXXXXXXXXXXXXX',
    'XXXXX  X11XXXXXX   XXX       XXXXXX          X   X                       XXXX    X   s         XXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXXX  XXX   XXXKKKK   XXXXXX       X          X                  XXXXX        X         XXXXXXXXXXXXXXXXXXX',
    'XXXXX  XXXS  XXX   XXXXXXX   Xc                          X             XXXXXX     X     X            XXXXXXXXXXXXX',
    'XXXXX  XXXXX XXX             XXXX                             X    XXXXXXXXXX        K       K                DXXX',
    'XXXXX        XXX             X     XXXXJJX                       KKXXXXXXXXXXJJX     X     XXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXJJXXXXXXXXXJJJXXXXXXXXJJXXXXXXXXXXXXX                       XXXXXXXXXXXXXXX           XXXXXXXXXXXXXXXXXXXXXXX']
level_map1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXX             XXXXXX                                                             XXXXXXXXX',
    'XXXXXP          XXXXXXXXXX             XXXXXX      s                                                    2 XXXXXXXXX',
    'XXXXXXXXXXXXXX  XXXXXXXXXX     XXX     XXXXXXXXXLXXXXLXXXXLXXX                              XKXXKXXKX  XXXXXXXXXXXX',
    'XXXXXXXX        K S    XXX     XXXX    XXXXXXXXXXXXXXXXXXXXXXX              111111        XXXXXXXXXXX  XXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXX   XXX     XXXXX   XXXXXXXXXXXXXXXXXXXXXXX             XXXXXXXXXX XXXXXXXXXXXXXXX  XXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXXX       XJJXXXXX                                       XXXXXXXXXX XXXXXXXXXXXXXXX  XXXXXXXXXXXX',
    'XXXXXXXX  XXXXXXXXXXXX     XXXXXXXXX                                       XXXXXXXXX   XXXXXXXXXXXXXX  XXXXXXXXXXXX',
    'XXXXXXXX                  XXXXXXXXXXD               K   K      XJJX K XJJX XXXXXXXXX c XXXXXXXXXXXXXX           DX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  X X X X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJJJXXXXXXXXXXXXXXJJXXXXXXXXXXX']
level_map3 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXX                    XXXXX            XXXXXXXXXXX                                       XXXXXXXXXXX',
    'XXXXXP  M    M    M  M    XXXXX          S XXXXXXXXXXXXXXXXXXXXXXXXXXX                                XXXXXXXXX',
    'XXXXX                                 XXXXXXXXXXX XXXXXXXXXXXXX',
    'XXXXXXXXXXLLXXXXXXX  XXXX   XXXXXX   XXXXXXXXXXXXXXXXXXXXXXX             XXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXX  XX  XXXXXXXX     s                                  XXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXX               c      XXXXXXXX   XXXXXXXXXXX',
    'XXXXX                                                                                                  DXXXXXXXXXX',
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    'XXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXX  X X X X XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJJXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

homescreen_map = [
    '',
    '  P',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    'XXXXXXXXXXXXXXXXXXX']
levels = [level_map1, level_map2, level_map3]
pygame.font.init()
tile_size = 64
screen_width = 1200
screen_height = len(homescreen_map) * tile_size
jump_speed = -15
screen = pygame.display.set_mode((screen_width, screen_height))
mode = 'home'
font = pygame.font.Font(None, 50)
volume = 1
num = 0
