import pygame
import random
from random import randrange
pygame.init()

successes, failures = pygame.init()
print("INF: pygame int: %s successes and %s failure(s)" % (successes, failures))

black, white, red, green, blue = (0, 0, 0),(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)
screen = pygame.display.set_mode((720, 480))
def distSquared(a,b):
    return (a)

class entite:
    def __init__(self,x=10,y=10,w=32,h=32):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0
    def display(self):
        pygame.draw.circle(screen, white, (self.x, self.y), 20, 2)

class obs:
    def __init__(self,x=10,y=10,w=70,h=70):
        self.x = w
        self.y = y
        self.w = w
        self.h = h


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((720, 480))
        self.clock = pygame.time.Clock()
        self.fps = 60  # Frames per second.

        self.square = entite()
        self.square.x = 0
        self.square.y = 0
        self.square.vx = 5

        self.obs = obs()
        self.obs.img = pygame.Surface((self.obs.w, self.obs.h))
        self.obs.img.fill(red)
        self.obs.x = random.randrange(670)
        self.obs.y = random.randrange(430)
       
        

        self.keypressed={} 

    def handleInput(self):
        """
        Analyse user command
        return True if user want to quit
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.KEYDOWN:
                self.keypressed[event.key] = 1

            if event.type == pygame.KEYUP:
                self.keypressed[event.key] = 0

        for key, bPressed in self.keypressed.items():
            if bPressed:
                if key == pygame.K_w or key == pygame.K_UP:
                    self.square.y -= 5
                elif key == pygame.K_s or key == pygame.K_DOWN:
                    self.square.y += 5
                elif key == pygame.K_d or key == pygame.K_RIGHT:
                    self.square.x += 5
                elif key == pygame.K_a or key == pygame.K_LEFT:
                    self.square.x -= 5
                elif key == pygame.K_SPACE:
                    self.square.x += 10
                elif key == pygame.K_ESCAPE:
                    return True

        return False

    def update(self):
        """
        Update internal state of the world
        """

        self.clock.tick(self.fps)

        if self.square.y<0:
            self.square.y = 0
        if self.square.y>self.screen.get_height()-self.square.h:
            self.square.y = self.screen.get_height()-self.square.h
        if self.square.x<0:
            self.square.x = 0
        if self.square.x>self.screen.get_width()-self.square.w:
            self.square.x = self.screen.get_width()-self.square.w

        if self.square.x>self.screen.get_width()-self.square.w:
            self.square.x = self.screen.get_width()-self.square.w

        # for p in self.entite + self.obs:
        #     if distSquared(proj, p) < p.r*p.r:





    def render(self):
        """
        Show a representation of the world to the user
        """
        self.screen.fill(black)
        self.square.display()
        self.screen.blit(self.obs.img, [self.obs.x,self.obs.y,self.obs.x+self.obs.w,self.obs.y+self.obs.h] )

        pygame.display.update()  # or pygame.display.flip()

# class Game - end


def startGame():
    game = Game()
    while 1:
        bQuit = game.handleInput()
        game.update()
        if bQuit:
            break
        game.render()

# startGame - end


startGame()

