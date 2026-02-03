"""
Par Camille Voisin
commencé le 6 janvier 2026
TP5.1 Exercice de classe
Idée : un monster truck qui saute au dessu de bus scolaires
"""


import arcade
import random as rd

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 680


def main():
    #le sol et le ciel proviennent des exemples de la théorie
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "TP5 Arcade")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()
    arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 2.26, arcade.color.FLATTERY)

    y = SCREEN_HEIGHT / 2
    x = 425
    y_bus = y - 39

    #le saut
    arcade.draw.draw_line(SCREEN_WIDTH - 175, y - 35, 500, SCREEN_HEIGHT - 300,
                          arcade.color.ROMAN_SILVER, 10)
    arcade.draw.draw_line(500,SCREEN_HEIGHT - 301, 610, y - 37,
                          arcade.color.COCONUT, 7)
    arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 285, SCREEN_HEIGHT / 2.26, arcade.color.JET)

    arcade.draw.draw_triangle_filled(600, y,
                                     600, y - 40,
                                     700, y - 40,
                                     arcade.color.ROMAN_SILVER)
    #la voiture
    arcade.draw_circle_filled(650, y + 1, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(545, y + 46, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(650, y + 1, 10, arcade.color.BATTLESHIP_GREY)
    arcade.draw_circle_filled(545, y + 46, 10, arcade.color.BATTLESHIP_GREY)
    arcade.draw_polygon_filled([[573, y + 41], [630, y + 16],[630, y + 46], [573, y + 71]], arcade.color.BLUE_VIOLET)
    arcade.draw_ellipse_outline(650, y + 1, 40, 40, arcade.color.BLACK_OLIVE, 3)
    arcade.draw_ellipse_outline(545, y + 46, 40, 40, arcade.color.BLACK_OLIVE, 3)

    arcade.draw.draw_arc_outline(530,y + 26, 100,100,arcade.color.BLUE_VIOLET, 20, 85, 7, 355)
    arcade.draw.draw_arc_outline(658,y - 18, 100,100,arcade.color.BLUE_VIOLET, 80, 145, 7, 15)
    arcade.draw_polygon_filled([[645, y + 19], [653, y + 21],[653, y + 32], [645, y + 30]], arcade.color.EERIE_BLACK)
    arcade.draw_polygon_filled([[548, y + 63], [556, y + 60],[558, y + 70], [550, y + 71]], arcade.color.EERIE_BLACK)
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
    #bus
    for i in range(4):
        arcade.draw_lrbt_rectangle_filled(x + 25,x + 50, y_bus, y + 25, arcade.color.GOLD)
        arcade.draw_lrbt_rectangle_filled(x,x + 25, y_bus, y, arcade.color.GOLD)
        arcade.draw_lrbt_rectangle_filled(x + 50,x + 75, y_bus, y, arcade.color.GOLD)
        arcade.draw_circle_filled(x + 25, y_bus + 39, 25, arcade.color.GOLD)
        arcade.draw_circle_filled(x + 50, y_bus + 39, 25, arcade.color.GOLD)
        arcade.draw_line(x, y_bus, x, y_bus + 39, arcade.color.BLACK, 2)
        arcade.draw_line(x + 75, y_bus, x + 75, y_bus + 39, arcade.color.BLACK, 2)
        arcade.draw_line(x + 25, y_bus + 64, x + 50, y_bus + 64, arcade.color.BLACK, 2)
        arcade.draw_arc_outline(x + 25, y_bus + 39, 48, 48, arcade.color.BLACK, 90, 180, 4)
        arcade.draw_arc_outline(x + 50, y_bus + 39, 48, 48, arcade.color.BLACK, 90, 180, 4, 90)
        arcade.draw_arc_outline(x + 43, y_bus + 39 - 20, 24, 24, arcade.color.BLACK, 90, 180, 4, 90)
        arcade.draw_arc_outline(x + 32, y_bus + 19, 24, 24, arcade.color.BLACK, 90, 180, 4)
        arcade.draw_line(x + 32, y_bus + 31, x + 43, y_bus + 31, arcade.color.BLACK, 2)
        arcade.draw_line(x + 20, y_bus + 19, x + 20, y_bus, arcade.color.BLACK, 2)
        arcade.draw_line(x + 55, y_bus + 19, x + 55, y_bus, arcade.color.BLACK, 2)
        arcade.draw_circle_filled(x + 17, y_bus + 52, 6, arcade.color.RED)
        arcade.draw_circle_filled(x + 58, y_bus + 52, 6, arcade.color.RED)
        arcade.draw_text("BUS", x + 24, y_bus + 49, arcade.color.BLACK)
        arcade.draw_polygon_filled([[x + 15, y_bus + 44], [x + 15, y_bus + 31], [x + 60, y_bus + 31], [x + 60, y_bus + 44]], arcade.color.SKY_BLUE)
        arcade.draw_line(x + 15, y_bus + 44, x + 60, y_bus + 44, arcade.color.BLACK, 2)
        arcade.draw_line(x + 15, y_bus + 44, x + 15, y_bus + 31, arcade.color.BLACK, 2)
        arcade.draw_line(x + 60, y_bus + 44, x + 60, y_bus + 31, arcade.color.BLACK, 2)
        arcade.draw_line(x + 15, y_bus + 31, x + 60, y_bus + 31, arcade.color.BLACK, 2)
        x -= 100
    #nuages
    for i in range(10):
        coos_x_nuage = rd.randint(100, 850)
        coos_y_nuage = rd.randint(450, 600)
        arcade.draw_circle_filled(coos_x_nuage, coos_y_nuage, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(coos_x_nuage + 25, coos_y_nuage, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(coos_x_nuage + 12, coos_y_nuage + 25, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(coos_x_nuage - 25, coos_y_nuage, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(coos_x_nuage - 12, coos_y_nuage + 25, 25, arcade.color.WHITE)
    #soleil
    arcade.draw_circle_filled(0, 680, 75, arcade.color.YELLOW)
    #details dans le sol
    for i in range(100):
        arcade.draw_circle_filled(rd.randint(0, 840), rd.randint(0, 284), 2, arcade.color.GRAY)
    for i in range(100):
        arcade.draw_circle_filled(rd.randint(0, 840), rd.randint(0, 284), 2, arcade.color.BISTRE)

    #l'arrivée
    arcade.draw_line(0, y + 35, 100, y + 35, arcade.color.ROMAN_SILVER, 10)
    arcade.draw_line(0, y - 40, 99, y + 38, arcade.color.ROMAN_SILVER, 10)

    #Le texte
    arcade.draw_point(25, 25, arcade.color.BLACK, 7)
    arcade.draw_text("TP5 Par Camille Voisin 404", 30, 19, arcade.color.GOLD)


    arcade.finish_render()
    arcade.run()

main()
