import pygame
import random
from pygame import USEREVENT
from pygame.sprite import Sprite
from pygame.sprite import collide_mask

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
        if self.x > 850:
            self.x = 850
            self.rect.x = 850
        if self.x < 0:
            self.x = 0
            self.rect.x = 0
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
        jump = None
        if self.direc_jump == 'jump_right':
            jump = pygame.image.load("pics/dog_right_jump.png")
        if self.direc_jump == 'jump_left':
            jump = pygame.image.load("pics/dog_left_jump.png")

        self.render.blit(jump, [self.x, self.y])

    def move(self, direction):
        if direction == "right":
            self.x += self.velocity
            self.rect.x += self.velocity
        if direction == "left":
            self.x -= self.velocity
            self.rect.x -= self.velocity

    def check_collision_obstacle(self, dog, obstacle):
        if collide_mask(dog, obstacle):
            if self.x < obstacle.x <= self.x + self.width and self.y == 430:
                self.keep_scrolling = False
                self.x = (obstacle.rect.x - self.width)
                self.rect.x = (obstacle.rect.x - self.width)
            elif obstacle.x < self.x < obstacle.x + obstacle.width and self.y == 430:
                self.keep_scrolling = False
                self.x = obstacle.x + obstacle.width
                self.rect.x = obstacle.x + obstacle.width
            elif self.y + self.height <= obstacle.y + (obstacle.height / 2):
                self.keep_scrolling = True
                self.y = (obstacle.y - self.height)
                self.rect.y = (obstacle.y - self.height)
            elif self.x + 100 < obstacle.x and not self.is_jump:
                self.keep_scrolling = True
                self.y = 430
                self.rect.y = 430
            elif self.x > obstacle.x + obstacle.width and not self.is_jump:
                self.keep_scrolling = True
                self.y = 430
                self.rect.y = 430

    def check_collision_finish(self, dog, finish):
        if collide_mask(dog, finish):
            print("IS COLLIDING")


class Background:

    def __init__(self, first_background, second_background, _render=None):
        self.render = _render
        self.first_background = first_background
        self.second_background = second_background
        self.bg_x = 0
        self.bg_x2 = self.first_background.get_width()

    def draw(self):
        self.render.blit(self.first_background, [self.bg_x, 0])  # reset the latest frame
        self.render.blit(self.second_background, [self.bg_x2, 0])  # reset the latest frame

    def scroll(self):
        self.bg_x -= 8
        self.bg_x2 -= 8

    def update(self):
        if self.bg_x <= self.first_background.get_width() * -1:  # If our bg is at the -width then reset its position
            self.bg_x = self.first_background.get_width()
        if self.bg_x2 <= self.second_background.get_width() * -1:  # If our bg is at the -width then reset its position
            self.bg_x2 = self.second_background.get_width()
        if self.bg_x > self.first_background.get_width():  # If our bg is at the -width then reset its position
            self.bg_x = self.first_background.get_width() * -1
        if self.bg_x2 > self.second_background.get_width():  # If our bg is at the -width then reset its position
            self.bg_x2 = self.second_background.get_width() * -1


class TreeStump(Sprite):

    def __init__(self, pos, size, _render):
        super().__init__()

        self.treestump = pygame.image.load("pics/treestump.png")
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
        self.render.blit(self.treestump, (self.x, self.y))


class Bush(Sprite):

    def __init__(self, pos, size, _render):
        super().__init__()

        self.bush = pygame.image.load("pics/bush.png")
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
        self.rect.x = pos[0] + 23
        self.rect.y = pos[1]

    def update(self):
        self.render.blit(self.bush, (self.x, self.y))
        pygame.draw.rect(self.image, RED, [0, 0, self.width, self.height])


class Bird:

    def __init__(self, _render=None):
        self.render = _render
        self.start_moving = False
        self.bird = [pygame.image.load("pics/bird1.png"), pygame.image.load("pics/bird2.png"),
                     pygame.image.load("pics/bird3.png"), pygame.image.load("pics/bird4.png")]
        self.fly_count = 0
        self.x = 1000
        self.y = 280

    def animate(self):
        if self.fly_count + 1 >= 24:
            self.fly_count = 0
        self.fly_count += 1
        self.render.blit(self.bird[self.fly_count // 6], (self.x, self.y))

    def update(self, velocity):
        if self.start_moving:
            self.x -= velocity


class DogHouse(Sprite):

    def __init__(self, _render=None):
        super().__init__()

        self.image = _render
        self.house = [pygame.image.load("pics/house3_flag1.png"),
                      pygame.image.load("pics/house3_flag3.png"),
                      pygame.image.load("pics/house3_flag4.png"),
                      pygame.image.load("pics/house3_flag5.png"),
                      pygame.image.load("pics/house3_flag6.png")]
        self.render = _render
        self.walk_count = 0
        self.x = 960
        self.y = 330
        self.width = 250
        self.height = 220
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def animate(self):
        if self.walk_count + 1 >= 40:
            self.walk_count = 0
        self.walk_count += 1
        self.render.blit(self.house[self.walk_count // 8], (self.x, self.y))

    def draw(self):
        self.render.blit(self.house[self.walk_count // 8], (self.x, self.y))

    def update(self):
        if self.x > 660:
            self.x -= 8
            self.rect.x -= 8
        else:
            self.x -= 0
            self.rect.x -= 0
        pygame.draw.rect(self.image, RED, [0, 0, self.width, self.height])


class DoggoPygame:

    def __init__(self):
        pygame.init()
        self.w = 1000  # screen width
        self.h = 600  # screen height
        self.screen = pygame.display.set_mode((self.w, self.h))  # initialize the screen
        self.clock = pygame.time.Clock()  # to control how fast the screen updates
        self.direc_walk = 'walk_right'
        self.direc_stand = 'stand_right'
        self.direc_jump = 'jump_right'
        self.walk_right = False
        self.walk_left = False
        self.jump_count = 10
        self.scroll = False

        # set all objects
        self.background = Background(pygame.image.load("pics/background_tree_advanced2.png"),
                                     pygame.image.load("pics/background_tree_advanced.png"), self.screen)
        self.dog = Dog((50, 430), (135, 115), self.screen)
        self.bird = Bird(self.screen)
        self.obstacles = []  # random objects
        self.house_with_flag = [pygame.image.load("pics/house3_flag1.png"),
                                pygame.image.load("pics/house3_flag3.png"),
                                pygame.image.load("pics/house3_flag4.png"),
                                pygame.image.load("pics/house3_flag5.png"),
                                pygame.image.load("pics/house3_flag6.png"), ]
        self.finish = DogHouse(self.screen)

        # set all sounds
        self.jump_effect = pygame.mixer.Sound('sound/8bitgame10_16bit_short.wav')
        self.run_effect = pygame.mixer.Sound('sound/step_grass.wav')
        self.run_effect.set_volume(0.18)
        pygame.mixer.music.load('sound/purrple-cat-field-of-fireflies.mp3')
        pygame.mixer.music.play(-1)

        # This will be a list that will contain all the sprites we intend to use in our game.
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.dog)
        self.sprites.add(self.finish)

        self.walk_action = 'stand_right'
        self.stand_action = 'stand_right'
        self.flag = 0

    def action(self, action):
        """
        action:
            stand still, move left, move right, jump, jump left, jump right
        :param action:
        :return:
        """
        if not self.dog.is_jump:
            if action == 0:
                self.walk_action = self.stand_action
                self.run_effect.stop()
            if action == 1:
                self.walk_action = 'walk_right'
                self.dog.move('right')
                self.stand_action = 'stand_right'
                self.run_effect.play()
            if action == 2:
                self.walk_action = 'walk_left'
                self.dog.move('left')
                self.stand_action = 'stand_left'
                self.run_effect.play()
        if action == 3 and self.flag != 2 and self.flag != 3:
            self.dog.is_jump = True
            self.flag = 1
            if self.jump_count >= -10:
                self.dog.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.dog.rect.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
                if self.jump_count == 9:
                    self.jump_effect.play()
            else:
                self.jump_count = 10
                self.dog.is_jump = False
                self.flag = 0
        #'''
        if action == 4 and self.flag != 1 and self.flag != 3:
            self.flag = 2
            self.dog.is_jump = True
            self.dog.direc_jump = 'jump_left'
            if self.jump_count >= -10:
                self.dog.x -= 5  # left jump
                self.dog.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.dog.rect.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
                if self.jump_count == 9:
                    self.jump_effect.play()
            else:
                self.jump_count = 10
                self.dog.is_jump = False
                self.flag = 0
        if action == 5 and self.flag != 1 and self.flag != 2:
            self.flag = 3
            self.dog.is_jump = True
            self.dog.direc_jump = 'jump_right'
            if self.jump_count >= -10:
                self.dog.x += 5  # right jump
                self.dog.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.dog.rect.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
                if self.jump_count == 9:
                    self.jump_effect.play()
            else:
                self.jump_count = 10
                self.dog.is_jump = False
                self.flag = 0
        self.dog.update()
        print(action)

    def view(self):
        """
        Draw the game
        :return:
        """
        self.clock.tick(FPS)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.carryOn = False  # Flag that we are done so we exit this loop

        for obstacle in self.obstacles:
            self.sprites.add(obstacle)
            self.dog.check_collision_obstacle(self.dog, obstacle)

        self.dog.check_collision_finish(self.dog, self.finish)

        # draws the rects from the sprites for colliding
        # call this before background.draw() so the rects aren't visible
        self.sprites.draw(self.screen)

        # set the background
        self.background.draw()
        self.background.update()

        # set bird animation
        self.bird.animate()
        self.bird.update(3)

        # random object at some points
        if self.dog.x == 100 or self.dog.x == 150 or self.dog.x == 300 or self.dog.x == 450 or self.dog.x == 500:
            r = random.randrange(0, 2)
            if r == 0:
                self.obstacles.append(TreeStump((1000, 450), (85, 95), self.screen))
            elif r == 1:
                self.bird.start_moving = True
                self.obstacles.append(Bush((1000, 450), (85, 95), self.screen))

        # call this after appending the obstacles, so they are visible
        self.dog.update()
        for obstacle in self.obstacles:
            obstacle.update()

        # draw dog house/finish
        if self.dog.x > 600:
            self.finish.animate()
            self.finish.update()

        # check if any key is pressed
        keys = pygame.key.get_pressed()

        '''
        # move to the right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.dog.keep_scrolling and self.dog.x < 640:
                self.background.scroll()
                self.bird.update(8)
                self.dog.velocity = 1
                for obstacle in self.obstacles:
                    obstacle.x -= 9
                    obstacle.rect.x -= 9
                    if obstacle.x < obstacle.width * -1:  # If our obstacle is off the screen we will remove it
                        self.obstacles.pop(self.obstacles.index(obstacle))
                        self.sprites.remove(obstacle)
            else:
                self.dog.velocity = 6
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
        '''

        if not self.dog.is_jump:
            self.dog.animate_run(self.walk_action)
        if self.dog.is_jump:
            self.dog.animate_jump()

        # '''

        pygame.display.set_caption('Doggo Adventure')
        pygame.display.update()
