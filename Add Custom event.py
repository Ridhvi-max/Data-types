import pygame,random
pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Sprite Color Change")
def random_color():return(random.randint(50,255),random.randint(50,255),random.randint(50,255))
class MySprite(pygame.sprite.Sprite):
 def __init__(self,color,x,y,w,h):
  super().__init__()
  self.image=pygame.Surface((w,h))
  self.color=color
  self.image.fill(self.color)
  self.rect=self.image.get_rect(topleft=(x,y))
 def change_color(self):
  self.color=random_color()
  self.image.fill(self.color)
s1=MySprite(random_color(),100,150,80,80)
s2=MySprite(random_color(),300,150,80,80)
sprites=pygame.sprite.Group()
sprites.add(s1,s2)
CHANGE_COLOR=pygame.USEREVENT+1
pygame.time.set_timer(CHANGE_COLOR,1000)
running=True
clock=pygame.time.Clock()
while running:
 screen.fill((30,30,30))
 for e in pygame.event.get():
  if e.type==pygame.QUIT:running=False
  elif e.type==CHANGE_COLOR:
   for s in sprites:s.change_color()
 sprites.draw(screen)
 pygame.display.flip()
 clock.tick(60)
pygame.quit()
