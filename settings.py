class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""initialize game settings"""
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (10,10,20)

		# Ship settings
		self.ship_speed = 3.5

		# Bullet settings
		self.bullet_speed = 3
		self.bullet_width = 6
		self.bullet_height = 30
		self.bullet_color = (255,93,204)
		self.bullets_allowed = 100 # I dislike so i made redundant >;)

		# Star settings
		"""Stars should be randomly placed (x,y) coords in certain 
		cells that can be found on the screen on initiation of the game;
		Then stars should move downwards and increment to the right at
		the top of the screen by their cell width plus 2.5 (or some other
		arbitrary number) when they reach the bottom of the screen"""
		self.star_speed = 1.75
		