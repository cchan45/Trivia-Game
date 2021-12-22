import pygame
import pygame.locals
import time

from .base import PygameController

class QuestionController(PygameController):
    def __init__(self, view, question, difficulty, gettime):
        super().__init__(view)
        self.question = question
        self.difficulty = difficulty
        self.gettime = gettime
        self.score = 0


    def process(self, event):
        running = super().process(event)

        if running is False:
            return False

        if self.difficulty == 'easy':
            self.difficulty = 1
        elif self.difficulty == 'medium':
            self.difficulty = 2
        elif self.difficulty == 'hard':
            self.difficulty = 3

        currenttime = time.time()
        if event.type == pygame.locals.KEYDOWN:
            elasped = currenttime - self.gettime
            if event.key == pygame.locals.K_1:
                if self.question.answer_id == 1:
                    self.score += int(self.difficulty * (2000/elasped - 19 * elasped))
            elif event.key == pygame.locals.K_2:
                if self.question.answer_id == 2:
                    self.score += int(self.difficulty * (2000/elasped - 19 * elasped))
            elif event.key == pygame.locals.K_3:
                if self.question.answer_id == 3:
                    self.score += int(self.difficulty * (2000/elasped - 19 * elasped))
            elif event.key == pygame.locals.K_4:
                if self.question.answer_id == 4:
                    self.score += int(self.difficulty * (2000/elasped - 19 * elasped))
            return False

        return True