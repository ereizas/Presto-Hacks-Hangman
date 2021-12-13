import pygame
import time
import random
from pygame.locals import *
from pygame.event import wait

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


#### Creating The Game loop
# => frames => stops the frames when the player is loss (the human are k¡lled) and when the player closes the Window
# variable to keep the main loop Running
running = True
font = pygame.font.SysFont("helvetica",30) #or verdana

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
	
	screen.fill((0,0,0))
	screen.blit(font.render("Player Score: " + str(p1score),True, (255,255,255)),(10,50))
	screen.blit(font.render("Computer Score: " + str(compScore),True, (255,255,255)),(500,50))
	hangman = {0: lambda: pygame.draw.line(screen, (150, 75, 0), (200, 350), (400, 350), 10), 1: lambda: pygame.draw.line(screen, (150, 75, 0), (300, 350), (300, 100), 10), 2: lambda: pygame.draw.line(screen, (150, 75, 0), (300, 100), (400, 100), 10),
            3: lambda: pygame.draw.line(screen, (150, 75, 0), (400, 100), (400, 150), 10), 4: lambda: pygame.draw.circle(screen, (250, 250, 250), (400, 180), 30, 5), 5: lambda: pygame.draw.line(screen, (250, 250, 250), (400, 210), (400, 270), 5), 6: lambda: pygame.draw.line(screen, (250, 250, 250),
			(400, 240), (370, 210), 5), 7: lambda: pygame.draw.line(screen, (250, 250, 250), (400, 240), (430, 210), 5), 8: lambda: pygame.draw.line(screen, (250, 250, 250), (400, 270), (370, 300), 5), 9: lambda: pygame.draw.line(screen, (250, 250, 250), (400, 270), (430, 300), 5)}
	answer = []
	guess = []
	incorrGuesses = []
	hangindex = -1
	correct = False
	def arrToStr(arr):
		res = ""
		for i in arr:
			res+=i+" "
		return res

	#makes sure the randomly generated category arrays are not empty
	randInd1 = random.randint(0,3)
	while computerWords[randInd1]==[]:
		randInd1 = random.randit(0,3)
	randInd2 = random.randint(0,len(computerWords[randInd1])-1)
	##print(computerWords[randInd1][randInd2])
	if(randInd1==0):
		screen.blit(font.render("Artists",True,(255,255,255)),(300,10))
	elif(randInd1==1):
		screen.blit(font.render("Instruments",True,(255,255,255)),(300,10))
	elif(randInd1==2):
		screen.blit(font.render("Genres",True,(255,255,255)),(300,10))
	elif(randInd1==3):
		screen.blit(font.render("Musical Terms",True,(255,255,255)),(300,10))

	for char in computerWords[randInd1][randInd2]:
		answer.append(char.lower())
		if char != " ":
			guess.append("_")
		elif char == " ":
			guess.append(" ")
	computerWords[randInd1].remove(computerWords[randInd1][randInd2])
	
	guessStr = arrToStr(guess)
	
	pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,375,800,225))
	output = font.render(guessStr,True,(255,255,255))
	screen.blit(output,(200,400))
	pygame.display.update()

	while not correct:
		letter_guess = ""
		while letter_guess == "" or len(letter_guess)>1 or not letter_guess.isalpha():
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if pygame.key.name(event.key) == "escape":
						pygame.quit()
					letter_guess = pygame.key.name(event.key)
		
				
		if letter_guess in answer:
			index = 0
			for char in answer:
				if char==letter_guess.lower() or char==letter_guess.upper():
					guess[index]=char
				index+=1

			guessStr = arrToStr(guess)
			
			pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,375,800,225))
			output = font.render(guessStr,True,(255,255,255))
			screen.blit(output,(200,400))
			pygame.display.update()

			if guess == answer:

				guessStr = arrToStr(guess)

				pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,375,800,225))
				output = font.render(guessStr,True,(255,255,255))
				screen.blit(output,(200,400))
				pygame.display.update()
				pygame.time.wait(2000)

				p1score+=1
				screen.fill((0,0,0))
				correct=True
		else:
			hangindex+=1
			incorrGuesses.append(letter_guess)
			guessed = font.render(arrToStr(incorrGuesses),True,(255,255,255))
			screen.blit(font.render("Incorrect Guesses:",True,(255,255,255)),(470,160))
			screen.blit(guessed,(470,200))
			f = hangman.get(hangindex)
			#call function:
			f()
			pygame.display.update()
			if hangindex == 9:
				compScore+=1
				f()
				pygame.time.wait(2000)
				screen.fill((0,0,0))
				pygame.display.update()
				break

	guessStr = arrToStr(guess)
	
	pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,375,800,225))
	output = font.render(guessStr,True,(255,255,255))
	screen.blit(output,(200,400))
	pygame.display.update()

pygame.quit()