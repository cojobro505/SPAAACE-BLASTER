class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""initialize game all game settings"""
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (10,10,20)

		# Ship settings
		self.ship_limit = 2

		# Bullet settings
		self.bullet_width = 6
		self.bullet_height = 30
		self.bullet_color = (255,93,204)
		self.bullets_allowed = 100 # I dislike so i made redundant >;)

		# Alien Settings
		self.fleet_drop_speed = 15

		# Star settings
		"""Stars should be randomly placed (x,y) coords in certain 
		cells that can be found on the screen on initiation of the game;
		Then stars should move downwards and increment to the right at
		the top of the screen by their cell width plus 2.5 (or some other
		arbitrary number) when they reach the bottom of the screen"""
		self.star_color = (180,180,140)
		self.star_cell_width = 200
		self.star_cell_height = 200

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		# Scoring
		self.alien_points = 50

		self. initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game"""	
		self.star_speed = 1
		self.alien_speed = 1.75
		self.bullet_speed = 3
		self.ship_speed = 3.5

		# fleet direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

	def increase_speed(self):
		"""Increase speed settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points *= (self.speedup_scale)*2