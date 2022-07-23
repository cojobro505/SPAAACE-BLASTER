import pygame

from install_compatibility import *

class Ship:
	"""A class to manage the ship"""

	def __init__(self,ai_game):
		"""Initialize the ship and set its starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		self.image = pygame.image.load(resource_path('images/spaceship.png'))
		self.rect = self.image.get_rect()


		# Start each new ship at the bottom center of the screen.
		self.rect.midbottom = self.screen_rect.midbottom
		self.rect.y -= 5

		# Store a decimal value for the ships horizontal position
		self.x = float(self.rect.x)

		# Movement flags
		self.moving_right = False
		self.moving_left = False


	def update(self):
		"""Update the ships position based on the movement flag"""
		# Updates the ships x value and then updates the rect value
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
			self.image = pygame.image.load(resource_path('images/spaceship_right.png'))

		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
			self.image = pygame.image.load(resource_path('images/spaceship_left.png'))

		if (self.moving_left and self.moving_right) or (not self.moving_left and not self.moving_right):
			self.image = pygame.image.load(resource_path('images/spaceship.png'))

		self.rect.x = self.x

	def blitme(self):
		"""Draw ship at its current location"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		"""Center the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.image = pygame.image.load(resource_path('images/spaceship.png'))