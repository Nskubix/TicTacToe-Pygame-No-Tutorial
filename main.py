import pygame

pygame.init()

pygame.display.set_caption("2.2")
ikona = pygame.image.load("E:/YUUPI/Prank.jpg")
pygame.display.set_icon(ikona)
#fireinthehole = pygame.mixer.music.load("D:\Grydogrania\Pobrane/fire-in-the-hole-geometry-dash.mp3")
screaminginpublic = pygame.mixer.music.load("D:/Grydogrania/Pobrane/screaming-in-public-restrooms-prank-made-with-Voicemod-technology.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000



tura = False
clicked = False
clock = pygame.time.Clock()

start_pos = pygame.Vector2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

#nasze okno
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#tworzymy czworokąt
player = pygame.Rect((screen.get_width()/2,screen.get_height()/2,40,40))



game_tab = [[None,None,None],[None,None,None],[None,None,None]]

def draw_grid():
	#RYSUJEMY GRIDA
	pygame.draw.line(screen,(230,230,230),(screen.get_width()/3,screen.get_height()),(screen.get_width()/3,0),20)
	pygame.draw.line(screen,(230,230,230),(screen.get_width()-screen.get_width()/3,screen.get_height()),(screen.get_width()-screen.get_width()/3,0),20)

	pygame.draw.line(screen,(230,230,230),(screen.get_width(),screen.get_height()-screen.get_height()/3),(0,screen.get_height()-screen.get_height()/3),20)
	pygame.draw.line(screen,(230,230,230),(screen.get_width(),screen.get_height()-(2*screen.get_height()/3)),(0,screen.get_height()-(2*screen.get_height()/3)),20)

def movement():
	key_pressed = pygame.key.get_pressed()
	if(key_pressed[pygame.K_a]):
		player.move_ip(-1,0)
	if(key_pressed[pygame.K_w]):
		player.move_ip(0,-1)
	if(key_pressed[pygame.K_d]):
		player.move_ip(1,0)
	if(key_pressed[pygame.K_s]):
		player.move_ip(0,1)

def draw_player():
	pygame.draw.rect(screen,(255,0,0),player)

#Funckja robi gdzie klikniemy tam się game_tab uzupełni w odpowiednim miejscu X albo O 
def game_tab_click(mouse,width,height,ltura):
	x = 0
	y = 0

	if(mouse[0] < width/3):
		y=0
	elif(width/3 < mouse[0] < 2*(width/3)):
		y=1
	elif(2*(width/3) < mouse[0] <= width):
		y=2

	if(mouse[1] < height/3):
		x=0
	elif(height/3 < mouse[1] < 2*(height/3)):
		x=1
	elif(2*(height/3) < mouse[1] <= height):
		x=2
	if(game_tab[x][y] == None):	
		if(ltura == False):
			game_tab[x][y] = "X"
			ltura = True
			return ltura
		elif(ltura == True):
			game_tab[x][y] = "O"
			ltura = False
			return ltura
	else:
		if(ltura == False):
			return ltura
		elif(ltura == True):
			return ltura


def draw_XO():
	has_none = False
	run = True
	for i in range(3):
		for j in range(3):
			if(game_tab[i][j] == 'O'):
				
				r = pygame.Rect((333*j+45,333*i+45),(240,240))
				pygame.draw.ellipse(screen,(100,149,237),r,16)
			elif(game_tab[i][j] == 'X'):
				r = pygame.Rect((333*j+45,333*i+45),(240,240))			
				pygame.draw.line(screen,(196, 30, 58),(333*j+55,333*i+45),(333*j+45+230,333*i+45+240),20)
				pygame.draw.line(screen,(196, 30, 58),(333*j+35+240,333*i+45),(333*j+55,333*i+45+240),20)


			elif(game_tab[i][j] == None):
				has_none = True
	if(has_none == False):
		pygame.time.delay(500)
		run = False
	return run
		
def check_for_win():
	#game_tab[0][0] == game_tab[0][1] == game_tab[0][2]
	run = True
	for i in range(3):
		if(game_tab[i] == ['X', 'X', 'X'] or game_tab[i] == ['O', 'O', 'O'] and game_tab[0][0] != None):
			pygame.time.delay(500)
			run = False
		if(game_tab[0][i] == game_tab[1][i] == game_tab[2][i] and game_tab[0][i] != None):
			pygame.time.delay(500)
			run = False
	if(game_tab[0][0] == game_tab[1][1] == game_tab[2][2] and game_tab[0][0] != None):
			pygame.time.delay(500)
			run = False
	if(game_tab[2][0] == game_tab[1][1] == game_tab[0][2] and game_tab[2][0] != None):
			pygame.time.delay(500)
			run = False
	return run

run = True
#game loop
while(run):
	mouse_pos = pygame.mouse.get_pos()
	clock.tick(120)

	#ekran wypełniamy kolorem aby poprzednie klatki się zflushowały
	screen.fill((10,10,10))

	
	draw_grid()
	run = draw_XO()
	if(run == False):
		break 
	run = check_for_win()

	movement()
	draw_player()
	#print(pygame.mouse.get_pos())
	
	#event handler
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			run = False
		if(event.type == pygame.MOUSEBUTTONDOWN and clicked == False):
			clicked = True
			tura = game_tab_click(mouse_pos,screen.get_width(),screen.get_height(),tura)
		if(event.type == pygame.MOUSEBUTTONUP and clicked == True):
			clicked = False


	clock.tick(120)
	#updatujemy ekran żeby się wyświetlało wszystko poprawnie	
	pygame.display.update()




pygame.quit()