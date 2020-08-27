import pygame

BLACK = (0, 0, 0)
FPS = 60


class Dog:

    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.velocity = 5

    def animate(self, direc):
        anim = None

        # stand right
        if direc == 'stand_right':
            anim = [pygame.image.load("pics/dog_right_stand.png"),
                    pygame.image.load("pics/dog_right_stand2.png")]

        # walk right
        if direc == 'walk_right':
            anim = [pygame.image.load("pics/dog_right1.png"),
                    pygame.image.load("pics/dog_right2.png"),
                    pygame.image.load("pics/dog_right3.png"),
                    pygame.image.load("pics/dog_right4.png"),
                    pygame.image.load("pics/dog_right5.png"),
                    pygame.image.load("pics/dog_right6.png"),
                    pygame.image.load("pics/dog_right7.png"),
                    pygame.image.load("pics/dog_right8.png")]

        if direc == 'jump_right':
            anim = pygame.image.load("pics/dog_right_jump.png")

        # stand left
        if direc == 'stand_left':
            anim = [pygame.image.load("pics/dog_left_stand.png"),
                    pygame.image.load("pics/dog_left_stand2.png")]
        # walk left
        if direc == 'walk_left':
            anim = [pygame.image.load("pics/dog_left1.png"),
                    pygame.image.load("pics/dog_left2.png"),
                    pygame.image.load("pics/dog_left3.png"),
                    pygame.image.load("pics/dog_left4.png"),
                    pygame.image.load("pics/dog_left5.png"),
                    pygame.image.load("pics/dog_left6.png"),
                    pygame.image.load("pics/dog_left7.png"),
                    pygame.image.load("pics/dog_left8.png")]

        if direc == 'jump_left':
            anim = pygame.image.load("pics/dog_left_jump.png")

        return anim

    def move(self, direction):
        if direction == "right":
            self.x += self.velocity
            if self.x > 850:
                self.x = 850
        if direction == "left":
            self.x -= self.velocity
            if self.x < 0:
                self.x = 0


class DoggoPygame:

    def __init__(self):
        pygame.init()
        self.w = 1000  # screen width
        self.h = 600  # screen height
        self.screen = pygame.display.set_mode((self.w, self.h))  # initialize the screen
        self.background = pygame.image.load("pics/background.png").convert()
        self.carryOn = True
        self.walkCount = 0
        self.direc_walk = 'walk_right'
        self.direc_stand = 'stand_right'
        self.direc_jump = 'jump_right'
        self.walk_right = False
        self.walk_left = False
        self.is_jump = False
        self.jump_count = 10

        self.dog = Dog((20, 400))
        self.clock = pygame.time.Clock()  # to control how fast the screen updates

    def view(self):
        """
        Draw the game
        :return:
        """
        self.clock.tick(FPS)
        self.screen.blit(self.background, [0, 0])  # reset the latest frame

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.carryOn = False  # Flag that we are done so we exit this loop

        keys = pygame.key.get_pressed()

        # move to the right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if not self.is_jump:
                self.walk_right = True
            self.direc_walk = 'walk_right'
            self.direc_stand = 'stand_right'
            self.direc_jump = 'jump_right'
            if self.walkCount + 1 >= 24:
                self.walkCount = 0
            self.walkCount += 1
            if self.walk_right:
                self.screen.blit(self.dog.animate(self.direc_walk)[self.walkCount // 3], [self.dog.x, self.dog.y])
            self.dog.move('right')

        # move to the left
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if not self.is_jump:
                self.walk_left = True
            self.direc_walk = 'walk_left'
            self.direc_stand = 'stand_left'
            self.direc_jump = 'jump_left'
            if self.walkCount + 1 >= 24:
                self.walkCount = 0
            self.walkCount += 1
            if self.walk_left:
                self.screen.blit(self.dog.animate(self.direc_walk)[self.walkCount // 3], [self.dog.x, self.dog.y])
            self.dog.move('left')

        # just stand still
        elif not any(keys) and not self.is_jump:
            self.walk_right = False
            self.walk_left = False
            if self.walkCount + 1 >= 24:
                self.walkCount = 0
            self.walkCount += 1
            self.screen.blit(self.dog.animate(self.direc_stand)[self.walkCount // 12], [self.dog.x, self.dog.y])

        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
                self.walk_right = False
                self.walk_left = False
        elif self.is_jump:
            self.screen.blit(self.dog.animate(self.direc_jump), [self.dog.x, self.dog.y])
            if self.jump_count >= -10:
                self.dog.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jump = False

        pygame.display.update()
