W='C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\player_01.png'
Q=False
P='math'
O=True
N=range
from random import choices as X
import pygame as A
A.init()
Y=570
Z=550
if input('\n\n\n\nPlay forever mode? Y/N ')=='Y':H=O
else:H=Q
D=A.display.set_mode((Y,Z))
T=A.time.Clock()
I=O
J=3
G=[]
E=[]
U=A.image.load('C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\player_01_hit.png')
M=A.image.load(W)
F=A.Rect(220,480,M.get_width(),M.get_height())
a=A.Rect(0,470,570,120)
C=[45,145,35,20,30]
b=A.image.load(W)
class V:
	def __init__(B,rocket_x,rocket_y,speed,alien):
		B.speed=speed;B.alien=alien
		if B.alien:B.image=A.image.load('C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\alien_laser.png')
		else:B.image=A.image.load('C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\laser.png')
		B.rect=A.Rect(rocket_x,rocket_y-B.image.get_height(),B.image.get_width(),B.image.get_height())
	def shoot(A):
		D.blit(A.image,(A.rect.x,A.rect.y))
		if A.alien:A.rect.y+=A.speed
		else:A.rect.y-=A.speed
class R:
	def __init__(B,alien_x,alien_y,speed,rocket_speed):B.speed=speed;B.rocket_speed=rocket_speed;B.image=A.image.load('C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\alien_01.png');B.rect=A.Rect(alien_x,alien_y,B.image.get_width(),B.image.get_height())
	def shoot(A):
		if __import__('random').choice([O,Q]):B=V(A.rect.x+A.rect.width/2,A.rect.y,A.rocket_speed,O);global G;G.append(B)
	def move(A):
		A.rect.x+=A.speed
		if A.rect.x>=530:A.rect.x=0;A.rect.y+=60
		global D,H,E
		if A.rect.y>=420 and not H:global J;J=0
		if A.rect.y>=420 and H:
			E=[]
			for B in N(0,501,__import__(P).ceil(500/7.5)):
				for C in N(50,326,__import__(P).ceil(250/5.5)):E.append(R(B,C,25,5))
for B in N(0,501,__import__(P).ceil(500/7.5)):
	for K in N(50,326,__import__(P).ceil(250/5.5)):E.append(R(B,K,25,5))
while I:
	A.draw.rect(D,(0,0,0),A.Rect(0,0,60,M.get_height()))
	if not H:
		for (B,K) in zip([20,75,130],list(N(__import__(P).ceil(J)))):D.blit(A.image.load(W),(B,20))
	C[0]-=1;C[1]-=1;C[2]-=1;C[3]-=1;C[4]-=1;A.draw.rect(D,(43,186,33),a);D.blit(M,(F.x,F.y))
	for B in G:B.shoot()
	for L in A.event.get():
		if L.type==A.QUIT:I=Q
		if L.type==A.KEYDOWN and L.key==A.K_ESCAPE:I=Q
	S=A.key.get_pressed()
	if S[A.K_LEFT]and not F.x-6<=0:F.x-=5
	if S[A.K_RIGHT]and not F.x+5>=530:F.x+=5
	if S[A.K_SPACE]and C[0]<=0:G.append(V(F.x,F.y-10,3,Q));C[0]=45
	if C[4]==0:M=b;C[4]=30
	for B in G:
		if B.alien and F.colliderect(B.rect)and C[3]<=0:J-=1;C[3]=20;M=U;del G[G.index(B)]
		for K in E:
			if not B.alien and B.rect.colliderect(K.rect):del E[E.index(K)];B.hit=O;del G[G.index(B)]
	if J==0:D.blit(U,dest=(F.x,F.y))
	if C[1]<=0:
		try:
			for B in X(E,k=7):B.shoot()
			C[1]=145
		except IndexError:
			if not H:D.blit(A.image.load('C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\victory.png'),(250,250))
			else:
				for B in N(0,501,__import__(P).ceil(500/7.5)):
					for K in N(50,326,__import__(P).ceil(250/5.5)):E.append(R(B,K,25,5))
	for B in E:D.blit(B.image,(B.rect.x,B.rect.y))
	if C[2]<=0:
		C[2]=35
		for B in E:B.move()
	if J<=0 and not H:I=Q
	A.display.flip();T.tick(50);D.fill((0,0,0))
while not I and J==0:
	D.blit(A.image.load('C:\\Users\\Growl\\OneDrive\\CodaKid\\CodaKid_Python_1\\My Classwork\\space invaders\\images\\defeat.png'),(220,250))
	for L in A.event.get():
		if L.type==A.QUIT:I=O
		if L.type==A.KEYDOWN and L.key==A.K_ESCAPE:I=O
	A.display.flip();T.tick(50);D.fill((0,0,0))