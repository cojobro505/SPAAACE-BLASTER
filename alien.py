import pygame
from pygame.sprite import Sprite
from install_compatibility import *

class Alien(Sprite):
	"""A class to represent a single alien in a fleet"""

	def __init__(self, ai_game):
		"""Initialize alien and its starting position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the alien image and set its rect atribute
		self.image = pygame.image.load(resource_path('images/alien.png'))
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store alien's exact horizontal position
		self.x = float(self.rect.x)


	def update(self):
		"""Move alien to the right"""
		self.x += (self.settings.alien_speed *
						self.settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		"""return true if alien is at edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
