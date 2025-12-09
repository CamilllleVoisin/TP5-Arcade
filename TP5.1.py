"""
TP5.1 - Python Arcade
By Camille Voisin
Started : December 4 2025
Finished :
"""

import arcade
import random as rd

from pyglet.event import EVENT_HANDLE_STATE

color_list = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)
        self.x_pos = rd.randint(50, 500)
        self.y_pos = rd.randint(50, 500)
        self.rayon = rd.randint(10, 100)
    def on_draw(self):
        """
                    C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
                    de votre jeu à l'écran.
                    """

        self.clear()

        for i in range(20):
            color = rd.choice(color_list)
            arcade.draw_circle_filled(self.x_pos, self.y_pos, self.rayon, color)

    def on_update(self, delta_time: float) -> bool | None:
        pass

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        print(f'Touche = {symbol}')


def main():

    window = MyGame(640, 480, "Drawing Example")

    arcade.run()

main()