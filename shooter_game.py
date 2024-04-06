from pygame import *
from random import *
font.init()
class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y             
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += 10
    def fire(self):
        pass
class Enemy(GameSprite):
    def update(self):
        if self.rect.y <= 630:
            speed = randint(1,10)
            self.rect.y += speed
        else:
            self.rect.y = 0
            self.rect.x = randint(80, win_w - 80)
class Bullet(GameSprite):
    def update(self):
            self.rect.y += self.speed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

win_count = 0
lost_count = 0
                                                                                                                                                                                                                                   
win_w = 700
win_h = 500

f1 = font.Font(None, 36)
text1 = f1.render('Hello Привет' + str(lost_count), 1, (180, 0, 0))

window = display.set_mode((win_w, win_h))
display.set_caption('Ракета Бомба Петарда')

background = transform.scale(image.load('rbt.png'), (700, 500))
hero = Player('inv.png', 0, win_h - 100, 80, 100, 4)
monsters = sprite.Group()
for i in range(1, 300):
    monster = Enemy('peta.png', randint(80, win_w - 80), -50, 80, 50, randint(1,5))
    monsters.add(monster)

clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

game = True
finish = False

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False 

    if finish != True:
        window.blit(background, (0, 0))
        hero.update()
        hero.reset()
        text1 = f1.render('Пропущено: ' + str(lost_count), 1, (180, 0, 0))
        text2 = f1.render('Сбито: ' + str(win_count), 1, (180, 0, 0))
        window.blit(text1, (10 ,15))
        window.blit(text2, (10 ,50))
        monsters.update()
        monsters.draw(window)
    if monster.rect.y == 500:
        lost_count += 1
        print(lost_count)

    clock.tick(FPS)
    display.update()