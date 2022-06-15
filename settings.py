class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""initialize game settings"""
		# Screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (10,10,20)

		# Ship settings
		self.ship_speed = 0.75

		# Bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 6
		self.bullet_height = 30
		self.bullet_color = (255,93,204)
		self.bullets_allowed = 100 # I dislike so i made redundant >;)