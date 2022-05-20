import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
  
building1 = pygame.Rect(10,250,40,400)
building2 = pygame.Rect(90,150,30,450)
building3 = pygame.Rect(150,300,30,300)
building4 = pygame.Rect(200,100,30,500)
building5 = pygame.Rect(250,150,30,450)
building6 = pygame.Rect(300,50,30,550)
building7 = pygame.Rect(350,200,30,400)

#buildingspeed=1


#create a funtion drawBuilding

pygame.draw.rect(screen,(25,250,50),building1)
pygame.draw.rect(screen,(255,0,250),building2)
pygame.draw.rect(screen,(50,100,150),building3)
pygame.draw.rect(screen,(255,50,150),building4)
pygame.draw.rect(screen,(95,230,50),building5)
pygame.draw.rect(screen,(105,205,50),building6)
pygame.draw.rect(screen,(255,0,50),building7)
    
   
    
    

#screen.fill((50,150,255))
    
while True:    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                
                
                #call the drawBuilding function
                building1()
                building2() 
                building3()
                building4()
                building5()
                building6()
                building7()
   
    pygame.display.update()
    clock.tick(30)
    
    
    
    

