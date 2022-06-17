import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to manage bullets fired by the ship"""

	def __init__(self,ai_game):
		"""Create a star object"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.star_color

		self.rect = pygame.Rect(0,0,self.settings.star_width,
			self.settings.star_height)

		# store stars position as a decimal value
		self.y = float(self.rect.y)

	def update(self):
		"""Move the stars down the screen"""
		# Update the decimal position of the star
		self.y += self.settings.star_speed
		# Update rect position
		self.rect.y = self.y
