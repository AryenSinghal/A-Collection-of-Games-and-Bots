import pygame
from pygame import mixer

from twentyfortyeight.Game import runGame
from twentyfortyeight.AI import runAI

from threading import Thread
import os

pygame.init()
pygame.display.set_caption('A Collection of Games and Bots')

brinjal = pygame.font.SysFont('Comic Sans',25)
screen = pygame.display.set_mode((int(13.5*35), int(16*35)))
clock = pygame.time.Clock()

menu_text = brinjal.render('MENU',True,'#FFFFFF')
menu_text_rect = menu_text.get_rect(center = (int(13.5*35/2), 40))
lemons = mixer.Sound(f'{os.getcwd()}\\assets\\lemons.wav')

class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elevation = elevation
		self.original_y_pos = pos[1]

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text_surf = brinjal.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elevation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elevation = 0
				self.pressed = True
			else:
				self.dynamic_elevation = self.elevation
				if self.pressed == True:
					self.press()
					self.pressed = False
		else:
			self.dynamic_elevation = self.elevation
			self.top_color = '#475F77'
    
	def press(self):
		print('click')

class ImageButton(Button):
	def __init__(self, image, text, width, height, pos, elevation):
		super().__init__(text, width, height, pos, elevation)
		self.image = pygame.image.load(image).convert_alpha()
		self.image = pygame.transform.scale(self.image, (width, height))
		self.image_rect = self.image.get_rect(center = self.top_rect.center)

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elevation
		self.image_rect.center = self.top_rect.center 
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 36)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 36)
		screen.blit(self.image, self.image_rect)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

def on2048PressGame():
	runGame(True)

def on2048PressAI():
	runAI()

def onTicTacToePress():
	from TicTacTerminator import GUI

def onSnekPress():
	from Snake import Snake

def onSnekAIPress():
	from Snake import SnakeAI

def onMazePress():
	from MazeGenerator import MazeGenerationAstar


run = True
_2048Game = Button('2048 Game',200,40,(20, 100),5)
_2048AI = Button('2048 AI',200,40,(250, 100),5)
TicTacToe = Button('TicTacToe',200,40,(20, 180),5)
MazeAI = Button('Maze AI',200,40,(250, 180),5)
Snek = Button('Snake',200,40,(20, 260),5)
SnekAI = Button('SnakeAI',200,40,(250, 260),5)
ClickGame = ImageButton('assets/cookie.png','Cookie clicker',200,200,(135, 340),5)
bootons = [_2048Game, _2048AI, TicTacToe, MazeAI, Snek, SnekAI, ClickGame]

_2048Game.press = on2048PressGame
_2048AI.press = on2048PressAI
TicTacToe.press = onTicTacToePress
MazeAI.press = onMazePress
Snek.press = onSnekPress
SnekAI.press = onSnekAIPress
ClickGame.press = lemons.play

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try: import webbrowser; webbrowser.open("https://youtu.be/OcfqDPAy7zc?t=7")
            except: pass
            run = False
    
    screen.fill((30, 30, 30))
    screen.blit(menu_text, menu_text_rect)
    for b in bootons: b.draw()
    pygame.display.update()

    clock.tick(60)
