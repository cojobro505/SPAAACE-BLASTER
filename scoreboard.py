import pygame.font

class Scoreboard:
	"""A class to report scoring information"""

	def __init__(self,ai_game):
		"""Initialize scorekeeping attributes"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Font setting for scoring information
		self.text_color = (235, 223, 12)
		self.font = pygame.font.SysFont('lucidaconsole',48)

		# Prepare the initial score image
		self.prep_score()

	def prep_score(self):
		"""Render score onto screen"""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True,
			self.text_color,self.settings.bg_color)
		self.score_image.set_colorkey(self.settings.bg_color)

		# Display score at top right corner of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 5

	def show_score(self):
		"""Show score onto the screen"""
		self.screen.blit(self.score_image,self.score_rect)
