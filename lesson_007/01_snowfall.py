# -*- coding: utf-8 -*-
from typing import List, Any
import random

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    sd.resolution = (1200, 800)

    # color = sd.background_color
    # x = 0
    # y = 0
    # length = 200

    def __init__(self):
        self.x = random.randint(0, sd.resolution[0])
        self.y = sd.resolution[1] + 50
        self.color = sd.random_color()
        self.length = random.randint(10, 30)
        self.point = sd.get_point(self.x, self.y)
        self.flakes = list()
        # self.flake = Snowflake()

    def get_snow(self):
        sd.snowflake(center=self.point, length=self.length, color=self.color)

    def clear_previous_picture(self):
        sd.snowflake(center=self.point, length=self.length, color=sd.background_color)

    def move(self):
        self.y -= random.randint(5, 100)
        self.x = random.randint(self.x-30, self.x+30)
        self.point = sd.get_point(self.x, self.y)
        sd.snowflake(center=self.point, length=self.length, color=sd.background_color)

    def draw(self):
        sd.snowflake(center=self.point, length=self.length, color=sd.random_color())

    def can_fall(self):
        if self.y < 0:
            self.y = sd.resolution[1]

    # def get_flakes(self):
    #     for i in range(40):
    #         self.flake = Snowflake()
    #         flakes.append(flake)

# TODO здесь ваш код


flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     flake.can_fall()
#     # if flake.__init__().y == -50:
#     #     flake.__init__().y = sd.resolution[1]
#     # if not flake.can_fall():
#     #     break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


flakes = list()

for i in range(40):
    flake = Snowflake()
    flakes.append(flake)
print(flakes)


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = Snowflake().get_flakes(count = 20)  # создать список снежинок
#
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        flake.can_fall()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     # fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     # if fallen_flakes:
#     #     append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
sd.pause()
