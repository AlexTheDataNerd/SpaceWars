import pygame 
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from circleshape import *
import sys
def main():
    pygame.init()#Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT)) # We define our screen size 
    clock = pygame.time.Clock()
    dt = 0
    
    #All Sprite.Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    shots = pygame.sprite.Group()
    
    #Closing
    Player.containers = (updatable , drawable) 
    Asteroid.containers = (asteroids , updatable ,drawable) 
    AsteroidField.containers = updatable
    Shot.containers =(shots ,updatable ,drawable)
         ## NOTE !!! ## First we put the objects into the sprite group !!
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2 )
    asteroidfield_1 = AsteroidField()

  
  
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
        
        updatable.update(dt)
        
        for asteroid in asteroids :
            if asteroid.collides_with(player):
                print("GAME OVER!!!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

       
        screen.fill("black") 
        # We colour the surface 
      
        for obj in drawable :
            obj.draw(screen)
        
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000







if __name__ == "__main__" :
    main()
