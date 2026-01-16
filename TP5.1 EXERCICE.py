"""
Par Camille Voisin
commencé le 6 janvier 2026
TP5.1 Exercice de classe
Idée : un monster truck qui saute au dessu de bus scolaires
"""


import arcade

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 680


def main():
    points_rect = [50, 75, 100, 75]
    #le sol et le ciel provient des exemples de la théorie
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "TP5 Arcade")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()
    arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 2.26, arcade.color.FLATTERY)

    y = SCREEN_HEIGHT / 2
    arcade.draw.draw_line(SCREEN_WIDTH - 175, y - 35, 500, SCREEN_HEIGHT - 300,
                          arcade.color.ROMAN_SILVER, 10)
    arcade.draw.draw_line(500,SCREEN_HEIGHT - 301, 610, y - 37,
                          arcade.color.COCONUT, 7)
    arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 285, SCREEN_HEIGHT / 2.26, arcade.color.JET)

    arcade.draw.draw_triangle_filled(600, y,
                                     600, y - 40,
                                     700, y - 40,
                                     arcade.color.ROMAN_SILVER)
    arcade.draw_circle_filled(650, y + 1, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(545, y + 46, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(650, y + 1, 10, arcade.color.BATTLESHIP_GREY)
    arcade.draw_circle_filled(545, y + 46, 10, arcade.color.BATTLESHIP_GREY)
    arcade.draw_polygon_filled([[573, y + 41], [630, y + 16],[630, y + 46], [573, y + 71]], arcade.color.BLUE_VIOLET)
    arcade.draw_ellipse_outline(650, y + 1, 40, 40, arcade.color.BLACK_OLIVE, 3)
    arcade.draw_ellipse_outline(545, y + 46, 40, 40, arcade.color.BLACK_OLIVE, 3)

    arcade.draw.draw_arc_outline(530,y + 26, 100,100,arcade.color.BLUE_VIOLET, 20, 85, 7, 355)
    arcade.draw.draw_arc_outline(658,y - 18, 100,100,arcade.color.BLUE_VIOLET, 80, 145, 7, 15)
    #y +21
    arcade.draw_polygon_filled([[645, y + 19], [653, y + 21],[653, y + 32], [645, y + 30]], arcade.color.EERIE_BLACK)
    arcade.draw_polygon_filled([[548, y + 63], [556, y + 60],[558, y + 70], [550, y + 71]], arcade.color.EERIE_BLACK)
    arcade.draw_point(25, 25, arcade.color.BLACK, 7)
    arcade.draw_text("TP5 Par Camille Voisin 404", 30, 19, arcade.color.GOLD)
    arcade.draw_triangle_filled(526, y + 76, 555, y + 85, 585, y + 66, arcade.color.BLUE_VIOLET)
    arcade.draw_triangle_filled(552, y + 73, 574, y + 70, 574, y + 54, arcade.color.BLUE_VIOLET)
    arcade.draw_triangle_filled(630, y + 18, 630, y + 46, 645, y + 46, arcade.color.BLUE_VIOLET)
    arcade.draw_triangle_filled(634, y + 25, 644, y + 46, 680, y + 46, arcade.color.BLUE_VIOLET)
    arcade.draw_triangle_filled(650, y + 32, 679, y + 46, 685, y + 25, arcade.color.BLUE_VIOLET)
    arcade.draw_line(575, y + 78, 678, y + 46, arcade.color.BLACK, 4)
    arcade.draw_polygon_filled([[556, y + 83], [585, y + 65], [630, y + 46], [679, y + 45]], arcade.color.GOLD)
    arcade.draw_line(575, y + 78, 630, y + 90, arcade.color.BLACK, 3)
    arcade.draw_line(630, y + 90, 677, y + 76, arcade.color.BLACK, 3)
    arcade.draw_line(677, y + 76, 678, y + 46, arcade.color.BLACK, 3)
    arcade.draw_line(556, y + 84, 575, y + 78, arcade.color.BLUE_VIOLET, 3)
    arcade.finish_render()
    arcade.run()

main()