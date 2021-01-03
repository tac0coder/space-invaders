import pygame as A
from random import choices as V
U = 'math'
T = 'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\player_01.png'
S = range
N = True
M = False
A.init()
W = 570
X = 550
D = A.display.set_mode((W, X))
P = A.time.Clock()
F = N
K = 3
G = []
H = []
Q = A.image.load(
    'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\player_01_hit.png')
J = A.image.load(T)
E = A.Rect(220, 480, J.get_width(), J.get_height())
Y = A.Rect(0, 470, 570, 120)
C = [45, 145, 35, 20, 50, 30]
Z = A.image.load(T)


class R:
    def __init__(B, rocket_x, rocket_y, speed, alien):
        B.speed = speed
        B.alien = alien
        if B.alien:
            B.image = A.image.load(
                'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\alien_laser.png')
        else:
            B.image = A.image.load(
                'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\laser.png')
        B.rect = A.Rect(rocket_x, rocket_y-B.image.get_height(),
                        B.image.get_width(), B.image.get_height())

    def shoot(A):
        D.blit(A.image, (A.rect.x, A.rect.y))
        if A.alien:
            A.rect.y += A.speed
        else:
            A.rect.y -= A.speed


class a:
    def __init__(B, alien_x, alien_y, speed, rocket_speed): B.speed = speed; B.rocket_speed = rocket_speed; B.image = A.image.load(
        'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\alien_01.png'); B.rect = A.Rect(alien_x, alien_y, B.image.get_width(), B.image.get_height())

    def shoot(A):
        if __import__('random').choice([N, M]):
            B = R(A.rect.x+(A.rect.width/2), A.rect.y, A.rocket_speed, N)
            global G
            G.append(B)

    def move(A):
        A.rect.x += A.speed
        if A.rect.x >= 530:
            A.rect.x = 0
            A.rect.y += 60
        global K
        if A.rect.y >= 420:
            K = 0


for B in S(0, 501, __import__(U).ceil(500/7.5)):
    for L in S(50, 326, __import__(U).ceil(250/5.5)):
        H.append(a(B, L, 25, 5))
while F:
    A.draw.rect(D, (0, 0, 0), A.Rect(0, 0, 60, J.get_height()))
    for (B, L) in zip([20, 75, 130], list(S(__import__(U).ceil(K)))):
        D.blit(A.image.load(T), (B, 20))
    C[0] -= 1
    C[1] -= 1
    C[2] -= 1
    C[3] -= 1
    C[4] -= 1
    C[5] -= 1
    A.draw.rect(D, (43, 186, 33), Y)
    D.blit(J, (E.x, E.y))
    for B in G:
        B.shoot()
    for I in A.event.get():
        if I.type == A.QUIT:
            F = M
        if I.type == A.KEYDOWN and I.key == A.K_ESCAPE:
            F = M
    O = A.key.get_pressed()
    if O[A.K_LEFT] and not E.x-6 <= 0:
        E.x -= 5
    if O[A.K_RIGHT] and not E.x+5 >= 530:
        E.x += 5
    if O[A.K_SPACE] and C[0] <= 0:
        G.append(R(E.x, E.y-10, 3, M))
        C[0] = 45
    if C[5] == 0:
        J = Z
        C[5] = 30
    for B in G:
        if B.alien and E.colliderect(B.rect) and C[3] <= 0:
            K -= 1
            C[3] = 20
            A.time.delay(200)
            J = Q
            del G[G.index(B)]
        for L in H:
            if not B.alien and B.rect.colliderect(L.rect) and C[4] <= 0:
                del H[H.index(L)]
                C[4] = 50
                A.time.delay(200)
                del G[G.index(B)]
    if K == 0:
        D.blit(Q, dest=(E.x, E.y))
        A.time.delay(200)
    if C[1] <= 0:
        try:
            for B in V(H, k=7):
                B.shoot()
            C[1] = 145
        except IndexError:
            D.blit(A.image.load(
                'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\victory.png'), (250, 250))
    for B in H:
        D.blit(B.image, (B.rect.x, B.rect.y))
    if C[2] <= 0:
        C[2] = 35
        for B in H:
            B.move()
    if K <= 0:
        F = M
    A.display.flip()
    P.tick(50)
    D.fill((0, 0, 0))
while not F and K == 0:
    D.blit(A.image.load(
        'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\defeat.png'), (220, 250))
    for I in A.event.get():
        if I.type == A.QUIT:
            F = N
        if I.type == A.KEYDOWN and I.key == A.K_ESCAPE:
            F = N
    A.display.flip()
    P.tick(50)
    D.fill((0, 0, 0))
