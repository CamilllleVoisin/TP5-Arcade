"""
Par Camille Voisin
commencé le 6 janvier 2026
TP5.1 Exercice de classe
"""


import arcade

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 680

def main():
    #le sol et le ciel provient des exemples de la théorie
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()
    arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 2.26,
        arcade.color.FLATTERY)

    y = SCREEN_HEIGHT / 2
    arcade.draw.draw_line(SCREEN_WIDTH - 175, y - 35, 500, SCREEN_HEIGHT - 300,
                          arcade.color.COCONUT, 10)
    arcade.draw.draw_line(500,SCREEN_HEIGHT - 301, 610, y - 37,
                          arcade.color.ROMAN_SILVER, 7)
    arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 285, SCREEN_HEIGHT / 2.26, arcade.color.JET)

    arcade.draw.draw_triangle_filled(600, y,
                                     600, y - 40,
                                     700, y - 40,
                                     arcade.color.ROMAN_SILVER)

    arcade.finish_render()
    arcade.run()

main()