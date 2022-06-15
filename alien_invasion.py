import sys

import pygame

from settings import *
from ship import Ship
from bullet import *

class AlienInvasion:
	"""Overall class to manage assets and behavior"""

	def __init__(self):
		"""Initialize the game and create game resources"""
		pygame.init()
		self.settings = Settings()

		"""Windowed Mode"""
		#self.screen = pygame.display.set_mode(
		#	(self.settings.screen_width,self.settings.screen_height))
		
		"""Fullscreen Mode"""
		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption("Alien Invasion")

		# Sets the background color!
		#self.bg_color = (22,23,59)  ~~~ No longer needed with Settings class

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()


	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()


	def _check_events(self):
		# Watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self,event):
		"""Respond to keypresses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q or event.key == 27: # 27 = ESC key
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self,event):
		"""Respond to key releases"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Create new bullet and add it to bullet group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""update position of bullets and get rid of old bullets"""
		self.bullets.update() # With a group update will be called on each instance
		# Get rid of old bullets that have dissapeared
		for bullet in self.bullets.copy(): # python dosent allow modification of list while loop runs
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		# Make most recently drawn screen visible
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()