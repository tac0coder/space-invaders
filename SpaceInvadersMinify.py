import pygame as A
from random import choices as X
W = 'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\player_01.png'
Q = 'math'
P = range
N = False
M = True
A.init()
Y = 570
Z = 550
if input('\n\n\n\nPlay forever mode? Y/N ') == 'Y':
	O = M
else:
	O = N
D = A.display.set_mode((Y, Z))
S = A.time.Clock()
H = M
I = 3
F = []
G = []
T = A.image.load(
	'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\player_01_hit.png')
L = A.image.load(W)
E = A.Rect(220, 480, L.get_width(), L.get_height())
a = A.Rect(0, 470, 570, 120)
C = [45, 145, 35, 20, 30]
b = A.image.load(W)


class U:
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


class V:
	def __init__(B, alien_x, alien_y, speed, rocket_speed): B.speed = speed; B.rocket_speed = rocket_speed; B.image = A.image.load(
		'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\alien_01.png'); B.rect = A.Rect(alien_x, alien_y, B.image.get_width(), B.image.get_height())

	def shoot(A):
		if __import__('random').choice([M, N]):
			B = U(A.rect.x+A.rect.width/2, A.rect.y, A.rocket_speed, M)
			global F
			F.append(B)

	def move(A):
		A.rect.x += A.speed
		if A.rect.x >= 530:
			A.rect.x = 0
			A.rect.y += 60
		global D
		if A.rect.y >= 420:
			global I
			I = 0


for B in P(0, 501, __import__(Q).ceil(500/7.5)):
	for J in P(50, 326, __import__(Q).ceil(250/5.5)):
		G.append(V(B, J, 25, 5))
while H:
	A.draw.rect(D, (0, 0, 0), A.Rect(0, 0, 60, L.get_height()))
	if not O:
		for (B, J) in zip([20, 75, 130], list(P(__import__(Q).ceil(I)))):
			D.blit(A.image.load(W), (B, 20))
	C[0] -= 1
	C[1] -= 1
	C[2] -= 1
	C[3] -= 1
	C[4] -= 1
	A.draw.rect(D, (43, 186, 33), a)
	D.blit(L, (E.x, E.y))
	for B in F:
		B.shoot()
	for K in A.event.get():
		if K.type == A.QUIT:
			H = N
		if K.type == A.KEYDOWN and K.key == A.K_ESCAPE:
			H = N
	R = A.key.get_pressed()
	if R[A.K_LEFT] and not E.x-6 <= 0:
		E.x -= 5
	if R[A.K_RIGHT] and not E.x+5 >= 530:
		E.x += 5
	if R[A.K_SPACE] and C[0] <= 0:
		F.append(U(E.x, E.y-10, 3, N))
		C[0] = 45
	if C[4] == 0:
		L = b
		C[4] = 30
	for B in F:
		if B.alien and E.colliderect(B.rect) and C[3] <= 0:
			I -= 1
			C[3] = 20
			L = T
			del F[F.index(B)]
		for J in G:
			if not B.alien and B.rect.colliderect(J.rect):
				del G[G.index(J)]
				B.hit = M
				del F[F.index(B)]
	if I == 0:
		D.blit(T, dest=(E.x, E.y))
	if C[1] <= 0:
		try:
			for B in X(G, k=7):
				B.shoot()
			C[1] = 145
		except IndexError:
			if not O:
				D.blit(A.image.load(
					'C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\victory.png'), (250, 250))
			else:
				for B in P(0, 501, __import__(Q).ceil(500/7.5)):
					for J in P(50, 326, __import__(Q).ceil(250/5.5)):
						G.append(V(B, J, 25, 5))
	for B in G:
		D.blit(B.image, (B.rect.x, B.rect.y))
	if C[2] <= 0:
		C[2] = 35
		for B in G:
			B.move()
	if I <= 0 and not O:
		H = N
	A.display.flip()
	S.tick(50)
	D.fill((0, 0, 0))
while not H and I == 0:
	D.blit(A.image.load('C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\defeat.png'), (220, 250))
	for K in A.event.get():
		if K.type == A.QUIT:
			H = M
		if K.type == A.KEYDOWN and K.key == A.K_ESCAPE:
			H = M
	A.display.flip()
	S.tick(50)
	D.fill((0, 0, 0))
