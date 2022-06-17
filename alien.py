import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in a fleet"""

	def __init__(self, ai_game):
		"""Initialize alien and its starting position"""
		super().__init__()
		self.screen = ai_game.screen

		# Load the alien image and set its rect atribute
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store alien's exact horizontal position
		self.x = float(self.rect.x)