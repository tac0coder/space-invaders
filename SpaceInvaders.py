from random import choices
import pygame
# Start the game
pygame.init()
game_width = 570
game_height = 550
# play forever?
if input('\n\n\n\nPlay forever mode? Y/N ') == 'Y':
    play_forever = True
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
player_lives = 3
rockets = []
aliens = []
# set up variables
player_hit = pygame.image.load(
    r'C:\Users\Growl\OneDrive\CodaKid\CodaKid_Python_1\My Classwork\space invaders\images\player_01_hit.png')
player = pygame.image.load(
    'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\player_01.png')
player_rect = pygame.Rect(220, 480,
                          player.get_width(), player.get_height())
earth = pygame.Rect(0, 470, 570, 120)
'''#MARK'''
frame_counters = [45, 145, 35, 20, 30]
player_def = pygame.image.load(
    'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\player_01.png')
# test shoot function to test if i can shoot

# setup rocket


class Rocket():
    def __init__(self, rocket_x, rocket_y, speed, alien):
        # self.rocket_x = rocket_x
        # self.rocket_y = rocket_y
        self.speed = speed
        self.alien = alien
        if self.alien:
            self.image = pygame.image.load(
                'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\alien_laser.png')
        else:
            self.image = pygame.image.load(
                'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\laser.png')
        self.rect = pygame.Rect(rocket_x, rocket_y-self.image.get_height(),
                                self.image.get_width(), self.image.get_height())

    def shoot(self):
        # self.image.get_rect().x = self.rocket_x
        # self.image.get_rect().y = self.rocket_y
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.alien:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

# Setup Alien


class Alien():
    def __init__(self, alien_x, alien_y, speed, rocket_speed):

        self.speed = speed
        self.rocket_speed = rocket_speed
        self.image = pygame.image.load(
            'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\alien_01.png')
        self.rect = pygame.Rect(
            alien_x, alien_y, self.image.get_width(), self.image.get_height())

    def shoot(self):
        if __import__('random').choice([True, False]):
            rocket = Rocket(self.rect.x+(self.rect.width/2), self.rect.y,
                            self.rocket_speed, True)
            global rockets

            rockets.append(rocket)

    def move(self):
        self.rect.x += self.speed
        if self.rect.x >= 530:
            self.rect.x = 0
            self.rect.y += 60

        global screen
        if self.rect.y >= 420:
            global player_lives
            player_lives = 0


# make aliens
for i in range(0, 501, __import__('math').ceil(500/7.5)):
    for var in range(50, 326, __import__('math').ceil(250/5.5)):
        aliens.append(Alien(i, var, 25, 5))

# The main game loop.  This code repeats forever
while running:

    # blit lives
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
        0, 0, 60, player.get_height()))
    for (i, var) in zip([20, 75, 130], list(range(__import__('math').ceil(player_lives)))):
        screen.blit(pygame.image.load(
            'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\player_01.png'), (i, 20))

    # decrease frame counters
    frame_counters[0] -= 1
    frame_counters[1] -= 1
    frame_counters[2] -= 1
    frame_counters[3] -= 1
    frame_counters[4] -= 1

    # draw earth

    pygame.draw.rect(screen, (43, 186, 33), earth)
    # draw player
    screen.blit(player, (player_rect.x, player_rect.y))
    # shoot rockets
    for i in rockets:
        i.shoot()

    # exit test
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    # move and shoot
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not player_rect.x-6 <= 0:
        player_rect.x -= 5

    if keys[pygame.K_RIGHT] and not player_rect.x+5 >= 530:
        player_rect.x += 5

    if keys[pygame.K_SPACE] and frame_counters[0] <= 0:
        rockets.append(Rocket(player_rect.x, player_rect.y-10, 3, False))
        frame_counters[0] = 45

    # revert player to normal image
    if frame_counters[4] == 0:
        player = player_def
        frame_counters[4] = 30
    '''#MARK Change this for faster shooting'''
# test if an alien's shot hit the player or vice versa
    for i in rockets:

        if i.alien and player_rect.colliderect(i.rect) and frame_counters[3] <= 0 and not play_forever:
            player_lives -= 1
            frame_counters[3] = 20
            player = player_hit
            del rockets[rockets.index(i)]
        for var in aliens:

            if not i.alien and i.rect.colliderect(var.rect):
                del aliens[aliens.index(var)]
                i.hit = True
                del rockets[rockets.index(i)]
# test if lives are O.K.
    if player_lives == 0:
        screen.blit(player_hit, dest=(player_rect.x, player_rect.y))
        pygame.time.delay(200)
# test if aliens can shoot:
    if frame_counters[1] <= 0:
        try:
            for i in choices(aliens, k=7):
                i.shoot()
            frame_counters[1] = 145
        except IndexError:
            if not play_forever:
                screen.blit(pygame.image.load(
                    r'C:\Users\Growl\OneDrive\CodaKid\CodaKid_Python_1\My Classwork\space invaders\images\victory.png'), (250, (250)))
            else:
                for i in range(0, 501, __import__('math').ceil(500/7.5)):
                    for var in range(50, 326, __import__('math').ceil(250/5.5)):
                        aliens.append(Alien(i, var, 25, 5))

# Blit aliens
    for i in aliens:
        screen.blit(i.image, (i.rect.x, i.rect.y))
    if frame_counters[2] <= 0:
        frame_counters[2] = 35
        for i in aliens:
            i.move()
    # test if lives are ok
    if player_lives <= 0:
        running = False
    pygame.display.flip()
    clock.tick(50)
    screen.fill((0, 0, 0))
while not running and player_lives == 0:
    screen.blit(pygame.image.load(
        'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\defeat.png'), (220, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = True
    pygame.display.flip()
    clock.tick(50)
    screen.fill((0, 0, 0))
