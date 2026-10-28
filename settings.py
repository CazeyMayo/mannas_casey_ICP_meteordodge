import pygame as pg

WIDTH =1024
HEIGHT = 768
TILESIZE = 32
FPS = 30
#Colors

WHITE = (255,255,255)
BLUE = (50,50, 255)
GREEN = (50, 255, 50)
BLACK = (0, 0, 0)
ORANGE = (253,190,2)
LIGHT_BLUE = (70,130,180)

#Player settings
PLAYER_SPEED = 400
PLAYER_FRIC = -0.1
PLAYER_HIT_RECT = pg.Rect(0,0,TILESIZE, TILESIZE)

def object_hit_rect(object, x, y, tiles):
    OBJECT_HIT_RECT = pg.Rect(x*tiles, y*tiles, TILESIZE, TILESIZE)
    return OBJECT_HIT_RECT