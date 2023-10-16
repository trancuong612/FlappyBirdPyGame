import pygame 

from random import randint

# pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 2, buffer = 512)
pygame.init()
RONG = 400
CAO = 600
screen = pygame.display.set_mode((RONG,CAO))
pygame.display.set_caption('Flappy Bird')
running = True
BLUE = (0, 0, 255)
GREEN = (109, 236, 66)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELOOW = (255,255, 0)

clock = pygame.time.Clock()

SPEED = 3
ONG = 50
KHCACH = 150
BIRD_x = 50
BIRD_N = 35
BIRD_C = 35
GRAVITY = 0.5

speed_down = 0
ong1_x = 600
ong2_x = 800
ong3_x = 1000
bird_y = 400
score = 0

ong1_hight = randint(100, 400)
ong2_hight = randint(100, 400)
ong3_hight = randint(100, 400)

font = pygame.font.SysFont('sans', 20)

ong1_check = False
ong2_check = False
ong3_check = False
pausing = False
background_image = pygame.image.load("background.png")
bird_image = pygame.image.load("bird33.png")
bird_image = pygame.transform.scale(bird_image, (BIRD_N, BIRD_C))
# music = pygame.mixer.Sound("Những Gì Anh Nói - BOZITT - MV Lyrics HD.mp3")

while running:
	clock.tick(60)
	screen.fill(BLUE)
	screen.blit(background_image, (0, 0))
	# music.play()
	# mouse = pygame.mouse.get_pos()
	# mouse_x = mouse[0]
	# mouse_y = mouse[1]
	# ve ong
	ong1_darw = pygame.draw.rect(screen,GREEN,(ong1_x,0,ONG,ong1_hight))
	ong2_darw = pygame.draw.rect(screen,GREEN,(ong2_x,0,ONG,ong2_hight))
	ong3_darw = pygame.draw.rect(screen,GREEN,(ong3_x,0,ONG,ong3_hight))

	ong1_darw_inv = pygame.draw.rect(screen,GREEN,(ong1_x,ong1_hight + KHCACH,ONG,CAO - ong1_hight - KHCACH))
	ong2_darw_inv = pygame.draw.rect(screen,GREEN,(ong2_x,ong2_hight + KHCACH,ONG,CAO - ong2_hight - KHCACH))
	ong3_darw_inv = pygame.draw.rect(screen,GREEN,(ong3_x,ong3_hight + KHCACH,ONG,CAO - ong3_hight - KHCACH))

	ong1_x = ong1_x - SPEED
	ong2_x = ong2_x - SPEED
	ong3_x = ong3_x - SPEED
# =====
	a = pygame.draw.rect(screen, YELOOW, (0, 599, 400, 10))

# ve chim
	# bird_darw = pygame.draw.rect(screen,RED,(BIRD_x, bird_y, BIRD_N, BIRD_C))

	bird_darw = screen.blit(bird_image, (BIRD_x, bird_y)) 
	bird_y += speed_down
	speed_down += GRAVITY

# tao ong moi
	if ong1_x < -ONG:
		ong1_x = 550
		ong1_check = False
		ong1_hight = randint(100, 400)
	if ong2_x < -ONG:
		ong2_x = 550
		ong2_check = False
		ong2_hight = randint(100, 400)
	if ong3_x < -ONG:
		ong3_x = 550
		ong3_check = False
		ong3_hight = randint(100, 400)

# tinh diem

	score_txt = font.render("Score: " + str(score), True, BLACK)
	screen.blit(score_txt, (5,5))
	# update_score

	if ong1_x + ONG <= BIRD_x and ong1_check == False:
		score += 1
		ong1_check = True
	if ong2_x + ONG <= BIRD_x and ong2_check == False:
		score += 1
		ong2_check = True
	if ong3_x + ONG <= BIRD_x and ong3_check == False:
		score += 1 
		ong3_check = True

	# check
	for ong in [ong1_darw, ong2_darw, ong3_darw, ong1_darw_inv, ong2_darw_inv, ong3_darw_inv, a]:
		if bird_darw.colliderect(ong) ==  True:
			pausing = True
			SPEED = 0
			speed_down = 0
			game_over_txt = font.render("Game Over, score: " + str(score), True, BLACK)
			screen.blit(game_over_txt, (200,300))
			game_continue_txt = font.render("bam dau cach de tiep tuc: ", True, BLACK)
			screen.blit(game_continue_txt, (200,400))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				# reset
				if pausing:
					ong1_x = 600
					ong2_x = 800
					ong3_x = 1000
					bird_y = 400
					score = 0
					SPEED = 3
					pausing = False

			speed_down = 0
			speed_down -= 6
	pygame.display.flip()

pygame.quit()