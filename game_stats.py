class GameStats:
	"""Track game statistics for Alien Invasion"""

	def __init__(self,ai_game):
		"""Initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()
		with open('highscore.txt','r+') as f:
			contents = f.read()
			if not contents:
				f.write('0')
				contents = 0
			self.highscore = float(contents)

		# Start alien invasion in an inactive state
		self.game_active = False

	def reset_stats(self):
		"""Initialize stats that change throughout the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1


