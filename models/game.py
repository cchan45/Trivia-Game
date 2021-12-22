import requests
from .question import Question

class Game:
    def __init__(self, difficulty, num=10):
        stuff = requests.get("https://opentdb.com/api.php?amount=" + str(num) + "&type=multiple&category=9&difficulty=" + difficulty).json()
        self.questions = [
            Question(
                elem["question"],
                elem["correct_answer"],
                elem["incorrect_answers"],
            )
            for elem in stuff["results"]
        ]
