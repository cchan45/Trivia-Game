import pygame.locals

from .base import PygameController

class DifficultyController(PygameController):
    """Used for selecting the difficulty of the questions"""

    def __init__(self, view):
        """Constructor - sets variables"""
        super().__init__(view)
        self.score = 0

    def process(self, event):
        """
        This method overrides the parent's.
        Its job is to do something when the user clicks in the shape.
        """

        # First call the parent method, just in case we want to exit
        running = super().process(event)

        if running is False:
            return False

        if event.type == pygame.locals.MOUSEBUTTONDOWN:
            #set difficulty from clicking the shape and exit loop
            if (event.pos[0] >= 100 and event.pos[0] <=150 and event.pos[1] >= 200 and event.pos[1] <= 250):
                difficulty = 'easy'
            elif (event.pos[0] >= 200 and event.pos[0] < 250 and event.pos[1] >= 200 and event.pos[1] <= 250):
                difficulty = 'medium'
            elif (event.pos[0] >= 300 and event.pos[0] <= 350 and event.pos[1] >= 200 and event.pos[1] <= 250):
                difficulty = 'hard'
            return difficulty

        return True