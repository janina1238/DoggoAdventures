import pygame
import random
from pygame import USEREVENT
from pygame.sprite import Sprite

BLACK = (0, 0, 0)
FPS = 60
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Dog(Sprite):

    def __init__(self, pos, size, _render):
        super().__init__()

        self.render = _render
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = size[0]  # 135
        self.height = size[1]  # 115
        self.velocity = 1
        self.walkCount = 0
        self.direc_jump = 'jump_right'
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.is_jump = False
        self.keep_scrolling = True

    def update(self):
        pygame.draw.rect(self.image, RED, [0, 0, self.width, self.height])

    def animate_run(self, direc):
        anim = None
        frames = 0

        # stand right
        if direc == 'stand_right':
            anim = [pygame.image.load("pics/dog_right_stand.png"),
                    pygame.image.load("pics/dog_right_stand2.png")]
            self.direc_jump = 'jump_right'
            frames = 12

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
            self.direc_jump = 'jump_right'
            frames = 3

        # stand left
        if direc == 'stand_left':
            anim = [pygame.image.load("pics/dog_left_stand.png"),
                    pygame.image.load("pics/dog_left_stand2.png")]
            self.direc_jump = 'jump_left'
            frames = 12

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
            self.direc_jump = 'jump_left'
            frames = 3

        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        self.walkCount += 1
        self.render.blit(anim[self.walkCount // frames], [self.x, self.y])

    def animate_jump(self):
        if self.direc_jump == 'jump_right':
            jump = pygame.image.load("pics/dog_right_jump.png")
        else:
            jump = pygame.image.load("pics/dog_left_jump.png")

        self.render.blit(jump, [self.x, self.y])

    def move(self, direction):
        if direction == "right":
            self.x += self.velocity
            self.rect.x += self.velocity
            if self.x > 850:
                self.x = 850
                self.rect.x = 850
        if direction == "left":
            self.x -= self.velocity
            self.rect.x -= self.velocity
            if self.x < 0:
                self.x = 0
                self.rect.x = 0

    def check_collision(self, dog, obstacle):
        if pygame.sprite.collide_mask(dog, obstacle):
            if self.x < obstacle.x <= self.x + self.width and self.y == 410:
                self.keep_scrolling = False
                self.x = (obstacle.rect.x - self.width)
                self.rect.x = (obstacle.rect.x - self.width)
            elif obstacle.x < self.x < obstacle.x + obstacle.width and self.y == 410:
                self.keep_scrolling = False
                self.x = obstacle.x + obstacle.width
                self.rect.x = obstacle.x + obstacle.width
            elif self.y + self.height <= obstacle.y + (obstacle.height / 2):
                self.keep_scrolling = True
                self.y = (obstacle.y - self.height)
                self.rect.y = (obstacle.y - self.height)
            elif self.x + 100 < obstacle.x and not self.is_jump:
                self.keep_scrolling = True
                self.y = 410
                self.rect.y = 410
            elif self.x > obstacle.x + obstacle.width and not self.is_jump:
                self.keep_scrolling = True
                self.y = 410
                self.rect.y = 410


class Treestump(Sprite):

    def __init__(self, pos, size, _render):
        super().__init__()

        self.render = _render
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]  # 85
        self.height = size[1]  # 95
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0] + 23
        self.rect.y = pos[1]

    def update(self):
        pygame.draw.rect(self.image, GREEN, [0, 0, self.width, self.height])
        treestump = pygame.image.load("pics/treestump.png")
        self.render.blit(treestump, (self.x, self.y))


class Bush(Sprite):

    def __init__(self, pos, size, _render):
        super().__init__()

        self.render = _render
        self.image = _render
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]  # 100
        self.height = size[1]  # 95
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0] + 8
        self.rect.y = pos[1]

    def update(self):
        bush = pygame.image.load("pics/bush.png")
        self.render.blit(bush, (self.x, self.y))
        pygame.draw.rect(self.image, RED, [0, 0, self.width, self.height])


class DoggoPygame:

    def __init__(self):
        pygame.init()
        self.w = 1000  # screen width
        self.h = 600  # screen height
        self.screen = pygame.display.set_mode((self.w, self.h))  # initialize the screen
        self.clock = pygame.time.Clock()  # to control how fast the screen updates

        self.background = pygame.image.load("pics/background.png")
        self.bg_x = 0
        self.bg_x2 = self.background.get_width()
        self.carryOn = True
        self.direc_walk = 'walk_right'
        self.direc_stand = 'stand_right'
        self.direc_jump = 'jump_right'
        self.walk_right = False
        self.walk_left = False
        self.jump_count = 10
        self.vel_obj = 0

        self.scroll = False
        self.is_out = False

        self.dog = Dog((50, 410), (135, 115), self.screen)
        self.rand_x = random.randint(100, 600)
        self.rand_x2 = random.randint(100, 600)
        self.obstacles = []  # random objects

        self.jump_effect = pygame.mixer.Sound('sound/8bitgame10_16bit_short.wav')
        self.run_effect = pygame.mixer.Sound('sound/step_grass.wav')
        self.run_effect.set_volume(0.18)
        pygame.mixer.music.load('sound/purrple-cat-field-of-fireflies.mp3')
        pygame.mixer.music.play(-1)

        pygame.time.set_timer(USEREVENT + 2, 5000)

        # This will be a list that will contain all the sprites we intend to use in our game.
        self.all_sprites_list = pygame.sprite.Group()

        # Add the paddles and the ball to the list of objects
        self.all_sprites_list.add(self.dog)

        self.finish = pygame.image.load("pics/finish2.png")
        self.f_x = 1500

    def rand_obj(self):
        if self.dog.x > 100:
            self.is_out = True

    def view(self):
        """
        Draw the game
        :return:
        """
        self.clock.tick(FPS)

        for obstacle in self.obstacles:
            self.all_sprites_list.add(obstacle)
            self.dog.check_collision(self.dog, obstacle)

        self.all_sprites_list.draw(self.screen)

        if self.bg_x <= self.background.get_width() * -1:  # If our bg is at the -width then reset its position
            self.bg_x = self.background.get_width()
        if self.bg_x2 <= self.background.get_width() * -1:  # If our bg is at the -width then reset its position
            self.bg_x2 = self.background.get_width()
        if self.bg_x > self.background.get_width():  # If our bg is at the -width then reset its position
            self.bg_x = self.background.get_width() * -1
        if self.bg_x2 > self.background.get_width():  # If our bg is at the -width then reset its position
            self.bg_x2 = self.background.get_width() * -1
        self.screen.blit(self.background, [self.bg_x, 0])  # reset the latest frame
        self.screen.blit(self.background, [self.bg_x2, 0])  # reset the latest frame

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.carryOn = False  # Flag that we are done so we exit this loop

        if self.dog.x == 100 or self.dog.x == 150 or self.dog.x == 300 or self.dog.x == 500 or self.dog.x == 580:
            r = random.randrange(0, 2)
            if r == 0:
                self.obstacles.append(Treestump((1000, 430), (85, 95), self.screen))
            elif r == 1:
                self.obstacles.append(Bush((1000, 430), (85, 95), self.screen))

        self.all_sprites_list.update()

        # check if any key is pressed
        keys = pygame.key.get_pressed()

        if self.dog.x > 750:
            self.screen.blit(self.finish, (self.f_x, 380))

        # move to the right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.dog.keep_scrolling and self.dog.x < 850:
                self.bg_x -= 8
                self.bg_x2 -= 8
                if self.dog.x > 750:
                    self.f_x -= 7           # TO-DO: Ziel soll bleiben, wenn erreicht und hintergrund nicht mehr bewegen
                self.dog.velocity = 1
                for obstacle in self.obstacles:
                    obstacle.x -= 8
                    obstacle.rect.x -= 8
                    if obstacle.x < obstacle.width * -1:  # If our obstacle is off the screen we will remove it
                        self.obstacles.pop(self.obstacles.index(obstacle))
                        self.all_sprites_list.remove(obstacle)
            if not self.dog.is_jump:
                self.run_effect.play()
                self.walk_right = True
            self.direc_walk = 'walk_right'
            self.direc_stand = 'stand_right'
            self.direc_jump = 'jump_right'
            if self.walk_right:
                self.dog.animate_run(self.direc_walk)
            self.dog.move('right')

        # move to the left
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.run_effect.play()
            self.dog.velocity = 6
            for obstacle in self.obstacles:
                obstacle.x += 0
                obstacle.rect.x += 0
                if obstacle.x < obstacle.width * -1:  # If our obstacle is off the screen we will remove it
                    self.obstacles.pop(self.obstacles.index(obstacle))
            if not self.dog.is_jump:
                self.walk_left = True
            self.direc_walk = 'walk_left'
            self.direc_stand = 'stand_left'
            self.direc_jump = 'jump_left'
            if self.walk_left:
                self.dog.animate_run(self.direc_walk)
            self.dog.move('left')

        # just stand still
        elif not any(keys) and not self.dog.is_jump:
            self.run_effect.stop()
            self.dog.animate_run(self.direc_stand)

        # jump
        if not self.dog.is_jump:
            if keys[pygame.K_SPACE]:
                self.run_effect.stop()
                self.jump_effect.play()
                self.dog.is_jump = True
                self.walk_right = False
                self.walk_left = False
        elif self.dog.is_jump:
            self.dog.animate_jump()
            if self.jump_count >= -10:
                self.dog.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.dog.rect.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.dog.is_jump = False

        pygame.display.update()
