from .base import PygameView


class EndView(PygameView):
    """View when the game is over and display the user's score """

    def __init__(self, view, score):
        super().__init__(view)
        self.score = score

    def draw(self):
        self.window.fill((255, 255, 255))
        text = self.render_text_surface("Game ended.")
        self.window.blit(text, (200, 40))

        text = self.render_text_surface(f"Your score was {self.score}.")
        self.window.blit(text, (200, 300))
