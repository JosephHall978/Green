import pygame as pg
vec = pg.math.Vector2


# sets the values for screen size and frames per second
WIDTH = 1280
HEIGHT = 1024
FPS = 30
#define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (135, 206, 235)
GREY = (211, 211, 211)
OFFGREY = (230, 230, 230)


#sets variable called title as goose gunner
title = "Goose Gunner"


#sets the amount of pixels per tile
tilesize = 16
#sets the amount of horizontal tiles
tilewidth = WIDTH / tilesize
#sets the amount of vertical tiles
tileheight = HEIGHT / tilesize

#sets the speed of the player in pixel per frame
playerspeed = 250
#sets the speed of the plane rotation
rotationspeed = 150
#creates a variable called redplane and stores the PNG name in it
redplane = 'redplane.png'
#defines the hit box rectangle
plane_hitrect = pg.Rect(0, 0, 72, 72)
#creates a variable called cloud and stores the PNG name in it
cloud = 'cloud.png'

#creates a variable called goose and stores the PNG name in it
goose_image = 'goose.png'
#sets the speed of the goose in pixels per frame
goose_speed = 250
#sets the constant size for the hitrect of the goose
goose_hitrect = pg.Rect(0, 0, 72, 72)

#gives a variable ame to the bullet image
bullet_image = 'bullet.png'
#sets speed of the bullet
bullet_speed = 500
#sets lifespan of the bullet in milliseconds
bullet_life = 1500
#how fast bullet can shoot when button held down
bullet_rate = 150
#JH change removed gun_offset variable from here