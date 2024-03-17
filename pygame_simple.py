import pygame

successes, failures = pygame.init()
print("INF: pygame int: %s successes and %s failure(s)" % (successes, failures))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0) 
blue = (0, 0, 255)

class Object:
    def __init__(self,x=10,y=10,w=32,h=32):
        self.x = w
        self.y = y
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((720, 480))
        self.clock = pygame.time.Clock()
        self.fps = 60  # Frames per second.
        
        self.square = Object()
        self.square.img = pygame.Surface((self.square.w, self.square.h))
        self.square.img.fill(white)
        self.square.x = 0
        self.square.y = 0
        self.square.vx = 5

        self.obs = Object()
        self.obs.img = pygame.Surface((self.obs.w, self.obs.h))
        self.obs.img.fill(blue)
        self.obs.x = 400
        self.obs.y = 100
        self.obs.vx = 200
        
        self.keypressed={} # will store current keyboard pressed
        
    def handleInput(self):
        """
        Analyse user command
        return True if user want to quit
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                
            if event.type == pygame.KEYDOWN:     
                print("DBG: key '%s' pressed" % event.key )
                self.keypressed[event.key] = 1
                
            if event.type == pygame.KEYUP:
                self.keypressed[event.key] = 0
                
        for key, bPressed in self.keypressed.items():
            if bPressed:
                if key == pygame.K_a or key == pygame.K_UP:
                    self.square.y -= 4
                elif key == pygame.K_q or key == pygame.K_DOWN:
                    self.square.y += 4
                elif key == pygame.K_ESCAPE:
                    return True
                elif key == pygame.K_SPACE:
                    self.square.vx *= 1.3
            
                    
        return False
    
    def update(self):
        """
        Update internal state of the world
        """
        
        self.clock.tick(self.fps)
        
        self.square.x += self.square.vx
        if      (self.square.vx > 0 and self.square.x + self.square.w > self.screen.get_width()) \
            or  (self.square.vx < 0 and self.square.x < 0) \
            :
            self.square.vx *= -0.5
       
        self.square.y += self.square.vy
        if self.square.y < 0:
            self.square.y = 0

        elif self.square.y + self.square.h > self.screen.get_height():
            self.square.y = self.screen.get_height() - self.square.h
           
        return False

    def render(self):
        """
        Show a representation of the world to the user
        """
        self.screen.fill(black)
        self.screen.blit(self.square.img, [self.square.x,self.square.y,self.square.x+self.square.w,self.square.y+self.square.h] )
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