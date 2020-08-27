import pygame

BLACK = (0, 0, 0)
FPS = 60

class Dog:

    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]

    def draw(self):
        walk_right = [pygame.image.load("pics/dog_right1.png"),
                      pygame.image.load("pics/dog_right2.png"),
                      pygame.image.load("pics/dog_right3.png"),
                      pygame.image.load("pics/dog_right4.png"),
                      pygame.image.load("pics/dog_right5.png"),
                      pygame.image.load("pics/dog_right6.png"),
                      pygame.image.load("pics/dog_right7.png"),
                      pygame.image.load("pics/dog_right8.png")]
        # dog_image = pygame.image.load("dog_run1.png").convert()
        return walk_right

class DoggoPygame:

    def __init__(self):
        pygame.init()
        self.w = 1000  # screen width
        self.h = 600  # screen height
        self.screen = pygame.display.set_mode((self.w, self.h))  # initialize the screen
        self.background = pygame.image.load("pics/background.png").convert()
        self.carryOn = True
        self.walkCount= 0

        self.dog = Dog((20, 400))
        self.clock = pygame.time.Clock()  # to control how fast the screen updates

    def view(self):
        """
        Draw the game
        :return:
        """
        self.clock.tick(FPS)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.carryOn = False  # Flag that we are done so we exit this loop

        self.screen.blit(self.background, [0, 0])  # reset the latest frame

        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        self.walkCount += 1
        self.screen.blit(self.dog.draw()[self.walkCount//3], [self.dog.x, self.dog.y])

        pygame.display.update()
