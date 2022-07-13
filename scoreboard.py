import pygame.font
from pygame.sprite import Group

from lifecounter import Lifeboat

class Scoreboard:
	"""A class to report scoring information"""

	def __init__(self,ai_game):
		"""Initialize scorekeeping attributes"""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats


		# Font setting for scoring information
		self.text_color = (235, 223, 12)
		self.font = pygame.font.SysFont('lucidaconsole',48)
		self.level_font = pygame.font.SysFont('lucidaconsole',32)

		# Prepare the initial score image
		self.prep_score()
		self.prep_highscore()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""Render score onto screen"""
		score_str = "{:,}".format(int(self.stats.score))
		self.score_image = self.font.render(score_str, True,
			self.text_color,self.settings.bg_color)
		self.score_image.set_colorkey(self.settings.bg_color)

		# Display score at top right corner of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 5

	def prep_highscore(self):
		"""Turn the high score into a rendered image"""
		highscore = int(self.stats.highscore)
		highscore_str = "Highscore:"+"{:,}".format(highscore)
		self.highscore_image = self.font.render(highscore_str, True,
				self.text_color, self.settings.bg_color)
		self.highscore_image.set_colorkey(self.settings.bg_color)

		# Center highscore on the top center of the screen
		self.highscore_rect = self.highscore_image.get_rect()
		self.highscore_rect.centerx = self.screen_rect.centerx
		self.highscore_rect.top = self.score_rect.top

	def prep_level(self):
		"""Turn level into a rendered image. What else you think moron?"""
		level_str = str(self.stats.level)
		self.level_image = self.level_font.render(level_str, True,
				self.text_color,self.settings.bg_color)
		self.level_image.set_colorkey(self.settings.bg_color)

		# Postition level below the score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom +10

	def prep_ships(self):
		"""Show how many ships are left"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Lifeboat(self.ai_game)
			ship.rect.x = 10 + ship_number * (ship.rect.width + 10)
			ship.rect.y = 10
			self.ships.add(ship)

	def show_score(self):
		"""Show score, level, and lives left on the screen"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.highscore_image,self.highscore_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.ships.draw(self.screen)

	def check_highscore(self):
		"""Check to see if there is a new highscore and then update it"""
		if self.stats.score > self.stats.highscore:
			with open("highscore.txt",'w') as f:
				f.write(str(self.stats.score))
			self.stats.highscore = self.stats.score
			self.prep_highscore()
