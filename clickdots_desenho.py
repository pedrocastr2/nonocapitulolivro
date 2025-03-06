import pygame 
pygame.init()

screen =pygame.display.set_mode([800,600]) 
pygame.display.set_caption("Click para desenhar")

keep_going = True
RED = (255,0,0)
radius = 15


while keep_going: #loop de jogo
    for event in pygame.event.get():
       if event.type ==pygame.QUIT:
         keep_going = False  
         
         
       if event.type ==pygame.MOUSEBUTTONDOWN:
          spoot = event.pos
          pygame.draw.circle(screen,RED,spoot,radius)
       
       
    pygame.display.update()
       
       
       
       
pygame.quit()