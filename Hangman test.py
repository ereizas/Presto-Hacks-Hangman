import pygame
import time
import random
from pygame.locals import *
# The Design of the Game
# when the user reveil two letters will give them a bonus of one letter

# import pygame.locals for some interaction with key coordinates
from pygame.locals import (
	K_ESCAPE,
	QUIT,
	KEYDOWN,
	K_SPACE,
	
)

# Initialize the game
pygame.init()

# Defines Constent for the screen width and hights
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create a screen object
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# Drawing on The Scrren

screen.fill((0,0,0)) # change the background to black



# .blit => block transfer (it blit a surface into another surface)



# Create a sprite object for Player (not sure if needed)
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surface = pygame.Surface((75,25))
		self.surface.fill((202,228,241))
		self.rect = self.surface.get_rect()
# Create a new instance of player
player = Player()

#### Creating The Game loop
# => frames => stops the frames when the player is loss (the human are k¡lled) and when the player closes the Window
# variable to keep the main loop Running
running = True
font = pygame.font.SysFont("helvetica",5) #or verdana

pygame.display.flip()
p1score = 0
compScore = 0
computerWords = [#artists
	["Wolfgang Amadeus Mozart","Ludwig Van Beethoven", "Johann Sebastian Bach","Pyotr Ilyich Tchaikovsky","The Beatles","Elvis Presley",
	"Michael Jackson","Elton John","Louis Armstrong","David Bowie","The Rolling Stones","Tupac Shakur","Kurt Cobain","Pink Floyd","Madonna", "Eminem",
	"Aerosmith","Charlie Parker","Taylor Swift","Drake","Beyonce Knowles","Kanye West","Ariana Grande","Katy Perry","Bruno Mars","Ed Sheeran",
	"Machine Gun Kelly","Justin Bieber","Lady Gaga","Selena Gomez"],
	#instruments
	["piano","guitar","saxophone","ukulele","organ","violin","trumpet","clarinet","cello","drum","accordion","flute","xylophone","trombone","harmonica",
	"tuba","bassoon","synthesizer","tambourine","bagpipe","harpischord"],
	#genres
	["classical","rock","jazz","folk","pop","electronic dance music","reggae","dubstep","heavy metal","blues","disco","hip hop","country","punk",
	"alternative","bluegrass"],
	#musical terms
	["allegro","ballad","baritone","soprano","alto","tenor","cadence","pitch","tone","chord","song","music","concert","album","beat","instrumental",
	"crescendo","decrescendo","diminuendo","ensemble","flat","harmony","intonation","largo","major","minor","octave","conductor","musician","note",
	"quarter note","eigth note","half note","whole note","scale","symphony","orchestra","band","accent","beats per minute","dynamics","forte","vibrato"]]
# Main loop
while running:
	pygame.display.set_caption("Hangmoo")
	font = pygame.font.SysFont("helvetica",30) #or verdana
	screen.fill((250,0,0))
	screen.blit(font.render("Hello",True,(250,250,250)),(300,20))
	# Look  at every event in the queue and start the event handler
	for event in pygame.event.get(): # pygame.event it has all the events associated with it
		# check if the player hit the key ?
		if event.type == KEYDOWN:
			# check if the key was K_ESCAPE
			if event.key == K_ESCAPE:
				running = False
		
		if event.type == pygame.QUIT: 
			break

		# Check if the user click into the Close Button ? if so , stop the loop
		elif event.type == QUIT:
			running = False
	

	##player_1 = input("Enter the name of the player 1:")##
	

	hangman = {0:pygame.draw.line(screen,(150,75,0),(200,350),(400,350),10), 1:pygame.draw.line(screen,(150,75,0),(300,350),(300,100),10),2:pygame.draw.line(screen,(150,75,0),(300,100),(400,100),10),
	3:pygame.draw.line(screen,(150,75,0),(400,100),(400,150),10),4:pygame.draw.circle(screen,(250,250,250),(400,180),30,5),5:pygame.draw.line(screen,(250,250,250),(400,210),(400,270),5),6:pygame.draw.line(screen,(250,250,250),
	(400,240),(370,210),5), 7:pygame.draw.line(screen,(250,250,250),(400,240),(430,210),5), 8:pygame.draw.line(screen,(250,250,250),(400,270),(370,300),5),9:pygame.draw.line(screen,(250,250,250),(400,270),(430,300),5)}
	##^

	

	##print(F"#{player_1} Score => {str(p1score)} ")##
	answer = []
	guess = []
	hangindex = -1
	correct = False
	def arrToStr(arr):
		res = ""
		for i in arr:
			res+=i
		return res
	


	#makes sure the randomly generated category arrays are not empty
	randInd1 = random.randint(0,3)
	while computerWords[randInd1]==[]:
		randInd1 = random.randit(0,3)
	randInd2 = random.randint(0,len(computerWords[randInd1])-1)
	print(computerWords[randInd1][randInd2])
	for char in computerWords[randInd1][randInd2]:
		answer.append(char)
		if char != " ":
			guess.append("_")
		elif char == " ":
			guess.append(" ")
	computerWords[randInd1].remove(computerWords[randInd1][randInd2])
	
	guessStr = arrToStr(guess)
	output = font.render(guessStr,True,(255,255,255))
	pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,375,800,225))
	screen.blit(output,(200,400))

	while not correct:
		letter_guess = ""
		while letter_guess == "" or len(letter_guess)>1 or not letter_guess.isalpha():
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					letter_guess = pygame.key.name(event.key)
					print(letter_guess)
		if letter_guess in answer:
			index = 0
			for char in answer:
				if char==letter_guess.lower() or char==letter_guess.upper():
					guess[index]=char
				index+=1

			guessStr = arrToStr(guess)
			output = font.render(guessStr,True,(0,0,0))
			pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,375,800,225))
			screen.blit(output,(200,400))

			if guess == answer:

				guessStr = arrToStr(guess)
				output = font.render(guessStr,True,(0,0,0))
				pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,375,800,225))
				screen.blit(output,(200,400))

				p1score+=1
				screen.fill((0,0,0))
				correct=True
		else:
			print("+1")
			hangindex+=1
			if hangindex == 0:
				pygame.draw.line(screen,(150,75,0),(200,350),(400,350),10)
				print("hanging")
		##this ends program if user is wrong
		if hangindex == 9:
			print("done")
			compScore+=1
			screen.fill((0,0,0))
			break

	guessStr = arrToStr(guess)
	output = font.render(guessStr,True,(0,0,0))
	pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,375,800,225))
	screen.blit(output,(200,400))

pygame.quit()