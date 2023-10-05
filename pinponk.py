from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('ping pong')


class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
           self.rect.x += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
           self.rect.x += self.speed
background = transform.scale(image.load('holst.jpg'), (win_width, win_height))
Player1 = Player('palca.PNG',0,100,5,75,90)
Player2 = Player('palca.PNG',500,100,5,75,90)
ball = GameSprite('shar.png',250,250,5,60,60)
FPS = 60
clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))  
    display.update()
    clock.tick(FPS)