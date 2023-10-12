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
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
background = transform.scale(image.load('holst.jpg'), (win_width, win_height))
player1 = Player('palcka.jpg',0,100,5,50,120)
player2 = Player('palcka.jpg',650,100,5,50,120)
ball = GameSprite('shar.png',250,250,5,60,60)
FPS = 90
clock = time.Clock()
finish = False 
speed_x = 3
speed_y = 3
game = True
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180,0,0))
font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSE!', True, (180,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0,0))
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
    if ball.rect.x > 620:
        finish = True
        window.blit(lose2, (200,200))
    if ball.rect.y > win_height -80 or ball.rect.y <0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    player1.update_l()
    player2.update_r()
    player1.reset()
    player2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)