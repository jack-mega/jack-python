import pygame, sys
from pygame.locals import *

class MyBallClass(pygame.sprite.Sprite):
    def _init_(self, image_file, speed, location):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_Rect()
        self.rect.left, self.rect.top = loaction
        self.speed = speed
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.lef < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
            
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            
class MyPaddleCLass(pygame.sprite.Sprite):
    def init_(self, location = [0,0]):
        pygame.sprite.Sprite._init_(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
pygame.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
ball_speed = [10, 5]
myBall = MyBallClass('wackyball.bmp', ball_speed, [50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])

while 1:
    clock.tick()
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]
            
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myball.speed[1] = -myBall.speed[1]
        
    myBall.move()
    screen.blit(myBall.image, myBall.rect)
    screen.blit(paddle.imag, paddle.rect)
    pygame.display.flip()
    
    
            