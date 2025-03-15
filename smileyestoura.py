import pygame 
import random


BLACK=(0,0,0)
pygame.init()
screen =pygame.display.set_mode([800,600]) 
pygame.display.set_caption("Explosão sorriso")
mousedown = False
keep_going = True
clock = pygame.time.Clock()
pic = pygame.image.load("Crazysmile2.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
sprite_list = pygame.sprite.Group()


class Smiley(pygame.sprite.Sprite):
   
   
    def __init__(self,pos,xvel,yvel):
    
      
         super().__init__() 
         self.image = pic
         self.scale = random.randint(10, 100)
         self.image = pygame.transform.scale(self.image, (self.scale,self.scale))
         self.rect = self.image.get_rect(center=pos)
         self.xvel = xvel 
         self.yvel = yvel

    def update(self):
      self.rect.x += self.xvel
      self.rect.y += self.yvel
    
      if self.rect.x <= 0 or self.rect.x> screen.get_width() - self.scale:
         self.xvel = -self.xvel
         
      if self.rect.y <= 0 or self.rect.y> screen.get_height() - self.scale:    
         self.yvel = -self.yvel

while keep_going: #loop de jogo
    for event in pygame.event.get():
        
       if event.type ==pygame.QUIT:
         keep_going = False  
         
         
       if event.type ==pygame.MOUSEBUTTONDOWN:
             if pygame.mouse.get_pressed()[0]:
                
                mousedown = True
                
             elif pygame.mouse.get_pressed()[2]:  
                  pos = pygame.mouse.get_pos()
                  clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                  for s in clicked_smileys:
                    sprite_list.remove(s)
                  
       if event.type ==pygame.MOUSEBUTTONUP:   
           mousedown = False
           
    screen.fill((BLACK)) #Limpa a tela
    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.update()
    clock.tick(60)  #Limite  
    
    
    if mousedown:
        speedx = random.randint(-5,5)
        speedy = random.randint(-5,5)
        newSmiley = Smiley(pygame.mouse.get_pos(), speedx, speedy)
        sprite_list.add(newSmiley)
pygame.quit()