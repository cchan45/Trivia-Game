import pygame

from .base import PygameView


class DifficultyView(PygameView):
    """Main view for the game - draws a shapes with corresponding difficulties  """
    def __init__(self, window):
        super().__init__(window)

    def draw(self):
        self.window.fill((50, 50, 50))
        text = self.render_text_surface("Difficulty Settings", (255,255,255))
        self.window.blit(text, (25,25))

        text = self.render_text_surface("Green is for EASY", (0, 255, 0))
        self.window.blit(text, (25,60))

        text = self.render_text_surface("Red is for MEDIUM", (255, 0, 0))
        self.window.blit(text, (25,95))

        text = self.render_text_surface("Violet is for HARD", (238, 130, 238))
        self.window.blit(text, (25,130))

        pygame.draw.rect(self.window, (0, 255, 0), (100, 200, 50, 50)) #green = easy
        pygame.draw.rect(self.window, (255, 0, 0), (200, 200, 50, 50)) #red = medium
        pygame.draw.rect(self.window, (238, 130, 238), (300, 200, 50, 50)) #violet = hard
