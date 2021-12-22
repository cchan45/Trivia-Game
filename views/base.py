from abc import ABC, abstractmethod

import pygame
import pygame.font


class PygameView(ABC):
    """Abstract class for a basic Pygame view"""

    def __init__(self, window):
        """Constructor receives a window (where everything will be displayed)"""
        self.window = window

    def render_text_surface(self, text, colour=(0,0,0)):
        """Utility function to render a text surface"""
        arial = pygame.font.SysFont("arial", 24)
        text_surface = arial.render(text, True, colour)

        return text_surface

    @abstractmethod
    def draw(self):
        """Child classes MUST implement the draw method"""
        raise NotImplementedError

    def update(self):
        """Update the screen"""
        pygame.display.flip()
