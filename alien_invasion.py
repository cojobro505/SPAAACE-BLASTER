import sys
from time import sleep

import pygame
from random import randint

from settings import *
from ship import Ship
from bullet import *
from alien import Alien 
from star import *
from game_stats import GameStats
from button import *

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

		self.stats = GameStats(self)

		# Sets the background color!
		#self.bg_color = (22,23,59)  ~~~ No longer needed with Settings class
		self.stars = pygame.sprite.Group()
		self._start_stars()

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		self.play_button = Button(self,"Start Game")


	def run_game(self):
		"""Start the main loop for the game"""
		clock=pygame.time.Clock()
		while True:
			clock.tick(240) # refresh rate
			self._check_events()
			self._update_screen()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_stars()
				self._update_aliens()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	def _check_events(self):
		# Watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_keydown_events(self,event):
		"""Respond to keypresses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q or event.key == 27: # 27 = ESC key
			sys.exit()
		elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
			self._fire_bullet()
		elif event.key == pygame.K_RETURN: 
			if not self.stats.game_active:
				self._start_game()

	def _check_keyup_events(self,event):
		"""Respond to key releases"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _check_play_button(self,mouse_pos):
		"""Start a new game when a player clicks the play button"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self._start_game()

	def _start_game(self):
		self.stats.reset_stats()
		self.settings.initialize_dynamic_settings()
		self.stats.game_active = True
		# Get rid of remaining aliens and bullets
		self.aliens.empty()
		self.bullets.empty()
		# Create new fleet and recenter ship
		self._create_fleet()
		self.ship.center_ship()
		# Hide the mouse cursor
		pygame.mouse.set_visible(False)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###########  ALIEN  #############################################

	def _create_fleet(self):
		"""Create a fleet of aliens"""
		alien = Alien(self)
		# Make one alien
		#self.aliens.add(alien)
		alien_width,alien_height = alien.rect.size 

		available_space_x = self.settings.screen_width - (2*alien_width)
		number_aliens_x = available_space_x//(2*alien_width)

		# Determine the number of rows that fit on the screen.
		ship_height = self.ship.rect.height 
		available_space_y = (self.settings.screen_height -
								(3*alien_height) - ship_height)
		number_rows = available_space_y // (2*alien_height)

		# Create sir fleetwood of mac
		for row_num in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number,row_num)

	def _create_alien(self,alien_number,row_number):
		"""Create an alien and place it in a row"""
		alien = Alien(self)
		alien_width,alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien_height + 2 * alien.rect.height * row_number 
		self.aliens.add(alien)

	def _update_aliens(self):
		"""update position of all the aliens in the fleet"""
		self._check_fleet_edges()
		self.aliens.update()

		#look for alien-ship collisions
		if pygame.sprite.spritecollideany(self.ship,self.aliens):
			self._ship_hit()

		# Look for aliens reaching the bottom
		self._check_aliens_bottom()

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached the edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop entire fleet and change fleets direction"""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _ship_hit(self):
		"""Respond to the ship being hit by an alien"""
		# Decrement lives left
		if self.stats.ships_left > 0 :
			self.stats.ships_left -= 1

			# Get rid of remaining aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			# Create new fleet and recenter ship
			self.ship.center_ship()
			self._update_screen()
			sleep(1) # Pause for dramatic effect 'o'
			self._create_fleet()
		else:
			self.aliens.empty()
			self.bullets.empty()
			self.ship.center_ship()
			self._update_screen()
			self._create_fleet()
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _check_aliens_bottom(self):
		"""Check to see if any aliens have reached the bottom of the screen"""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# Treat same as ship getting hit
				self._ship_hit()
				break
	
##############  STARS  ###########################################

	def _start_stars(self):
		"""Create a sky of stars"""
		self.star_dist = 0
		available_space_x = self.settings.screen_width
		number_cols = available_space_x // (self.settings.star_cell_width) + 2
		self.number_cols = number_cols

		available_space_y = self.settings.screen_height
		number_rows = available_space_y // (self.settings.star_cell_height) + 2
		
		# Create sir fleetwood of mac starry edition
		for row_num in range(number_rows):
			for col_num in range(number_cols):
				self._create_star(col_num,row_num)

	def _create_star(self,col_number,row_number):
		"""Create a star and place it in a row"""
		star = Star(self)
		star.x = randint(1,star.cell_width) + star.cell_width * (col_number-1)
		star.rect.x = star.x
		star.y = randint(1,star.cell_height) + star.cell_height * (row_number - 1)
		star.rect.y = star.y 
		self.stars.add(star)

	def _update_stars(self):
		"""update position of old stars, get rid of old stars 
		   and replace new stars"""
		self.stars.update()
		self.star_dist += self.settings.star_speed
		# Adds new stars
		if self.star_dist >= self.settings.star_cell_height:
			self.star_dist -= self.settings.star_cell_height
			for col_num in range(self.number_cols):
				self._create_star(col_num,0)
		# Get rid of old stars
		for star in self.stars.copy():
			if star.rect.top >= self.settings.screen_height:
				self.stars.remove(star)

############  BULLETS  ##############################################

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

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		"""Respond to bullets-alien collisions"""
		# Remove the bullets and aliens that have collided
		collisions = pygame.sprite.groupcollide(
			self.bullets,self.aliens,True,True)
		if not self.aliens:
			# Destroy existing bullets and create a new fleet
			self.bullets.empty()
			self._create_fleet()
			self.settings.increase_speed()

######  SCREEN REFRESH  ###########################################

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""
		self.screen.fill(self.settings.bg_color)
		#self.ship.blitme()
		for star in self.stars.sprites():
			star.draw_star()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.ship.blitme()
		self.aliens.draw(self.screen)
		if not self.stats.game_active:
			self.play_button.draw_button()
		# Make most recently drawn screen visible
		pygame.display.flip()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
	# Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()