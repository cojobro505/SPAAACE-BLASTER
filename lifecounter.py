"""Pipipipi *Yugioh noises*"""
import pygame
from pygame.sprite import Sprite

class Lifeboat(Sprite):
	"""A class to manage the ship life counter"""

	def __init__(self,ai_game):
		"""Initialize the ships"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/lifeboat.png')
		self.rect = self.image.get_rect()