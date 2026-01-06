"""
TP5.1 THÉORIE
Le 11 décembre 2025
Par Camille Voisin
"""

import arcade

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 680


def main():
    #le sol et le ciel
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()
    arcade.draw.draw_lrbt_rectangle_filled(
        0,
        SCREEN_WIDTH,
        0,
        SCREEN_HEIGHT / 2.26,
        arcade.csscolor.DARK_GREEN)
    #position du tronc
    r = arcade.rect.XYWH(200, SCREEN_HEIGHT / 2 - 20, 30, 60)
    #un tronc arbre
    arcade.draw.draw_rect_filled(r, arcade.csscolor.BROWN)
    #l'arche/les feuilles
    arcade.draw.draw_arc_filled(200, SCREEN_HEIGHT / 2, 60, 100, arcade.csscolor.FOREST_GREEN,
                                0, 180)
    #position du tronc du 2e arbre
    r = arcade.rect.XYWH(275, SCREEN_HEIGHT / 2 - 20, 30, 60)
    #un tronc
    arcade.draw.draw_rect_filled(r, arcade.csscolor.BROWN)
    #un oval/les feuilles
    arcade.draw.draw_ellipse_filled(275, SCREEN_HEIGHT / 2 + 20, 50, 75, arcade.csscolor.FOREST_GREEN)

    #position du rectangle
    r = arcade.rect.XYWH(350, SCREEN_HEIGHT / 2 - 20, 30, 60)
    #tronc
    arcade.draw.draw_rect_filled(r, arcade.csscolor.BROWN)
    #cercle/feuilles
    arcade.draw.draw_circle_filled(350, SCREEN_HEIGHT / 2 + 20, 35, arcade.csscolor.FOREST_GREEN)

    #position
    r = arcade.rect.XYWH(425, SCREEN_HEIGHT / 2 - 20, 30, 60)
    #tronc
    arcade.draw.draw_rect_filled(r, arcade.csscolor.BROWN)
    #faire un triangle
    y = SCREEN_HEIGHT / 2 + 20
    arcade.draw.draw_triangle_filled(425, y + 40,
                                     400, y - 20,
                                     450, y - 20,
                                     arcade.color.FOREST_GREEN)

    #une ligne
    arcade.draw.draw_line(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 110, SCREEN_WIDTH, SCREEN_HEIGHT - 110,
                          arcade.color.BANANA_YELLOW, 10)
    #une ligne avec des points precis
    points = [(700, 300), (750, 600), (345, 675)]
    arcade.draw.draw_line_strip(points, arcade.color.BUFF, 10)
    # Voici un tuple avec trois valeurs: un chiffre entier, une booléenne
    # ainsi qu'une liste qui contient deux string.
    #un_tuple = (23, True, ["a", "b"])

    #une autre ligne avec plus de points
    line_list = [(139, 556), (720, 512), (773, 704), (710, 596)]
    arcade.draw.draw_lines(line_list, arcade.color.FOREST_GREEN, 10)


    arcade.finish_render()
    arcade.run()


main()


