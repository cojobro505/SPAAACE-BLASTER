import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
	"""A class to manage bullets fired by the ship"""

	def __init__(self,ai_game):
		"""Create a star object"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_width = ai_game.settings.screen_width
		self.screen_height = ai_game.settings.screen_height
		self.cell_width = ai_game.settings.star_cell_width
		self.cell_height = ai_game.settings.star_cell_height

		self.color = self.settings.star_color

		self.width = randint(1,3) * 3
		self.height = randint(3,5) * 3
		self.rect = pygame.Rect(0,0,self.width,self.height)

		# store stars position as a decimal value
		self.y = float(self.rect.y)

	def update(self):
		"""Move the stars down the screen"""
		# Update the decimal position of the star
		self.y += self.settings.star_speed
		# Update rect position
		self.rect.y = self.y

	def draw_star(self):
		"""Draw the star onto the screen"""
		pygame.draw.rect(self.screen,self.color,self.rect)
	
