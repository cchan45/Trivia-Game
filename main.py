import pygame
import time

from controllers import DifficultyController, End, QuestionController
from views import DifficultyView, EndView, QuestionView
from models import Game, Question

def main():
    """Main program"""

    # Initialize pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((1000, 400))
    score = 0

    # Create the game view and controller
    game_view = DifficultyView(window)
    choose_dificulty = DifficultyController(game_view)
    # Allows the user to pick a difficulty and starts the game after 10 secs
    difficulty = choose_dificulty.run()

    #display the choices for questions after user chooses a shape (difficulty) 
    gameclass = Game(difficulty)

    for question in gameclass.questions:
        gettime = time.time()
        question_view = QuestionView(window, question)
        q_controller = QuestionController(question_view, question, difficulty,gettime)
        q_controller.run(stop_after=10)
        score += q_controller.score

    # Create the end view and controller, and run it
    end_view = EndView(window, score=score)
    end = End(end_view)
    end.run()

if __name__ == "__main__":
    main()
