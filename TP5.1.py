"""
TP5.1 - Python Arcade
By Camille Voisin
Started : December 4 2025
Finished : December 9 2025
"""

import arcade
import random as rd
import time

from pyglet.event import EVENT_HANDLE_STATE


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

        self.ballpos = []
        for a in range(20):
            self.ballpos.append([rd.randint(50, 500), rd.randint(50, 500), rd.randint(5, 50),
                                 (rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))])
    def on_draw(self):
        """
                    C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
                    de votre jeu à l'écran.
                    """

        self.clear()

        for i in self.ballpos:
            arcade.draw_circle_filled(i[0], i[1], i[2], i[3])


    def on_update(self, delta_time: float) -> bool | None:
        pass

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        print(f'Touche = {symbol}')




def main():

    window = MyGame(640, 480, "Drawing Example")

    arcade.run()

main()

