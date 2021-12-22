from .base import PygameView

class QuestionView(PygameView):
    def __init__(self, window, question):
        super().__init__(window)
        self.question = question

    def draw(self):
        """ displays the question and the options on screen """
        num = 100
        self.window.fill((255, 165, 0))
        text = self.render_text_surface(self.question.question)
        self.window.blit(text, (0, 50))
        choices = self.question.get_answers()
        list_choices = choices.split("\n")
        for choice in list_choices:
            drawchoice = self.render_text_surface(choice)
            self.window.blit(drawchoice, (0, num))
            num += 50
