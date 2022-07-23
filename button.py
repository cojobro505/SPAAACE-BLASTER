import pygame.font

from install_compatibility import *

class Button:

	def __init__(self,aigame,msg):
		"""Initialize button attributes"""
		self.screen = aigame.screen
		self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load(resource_path('images/start button.png'))
		self.rect = self.image.get_rect()

		# center it.
		self.rect.center = self.screen_rect.center

	def draw_button(self):
		self.screen.blit(self.image,self.rect)