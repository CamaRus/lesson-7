# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def cat_food(self):
        self.house.bowl += 50
        self.house.money -= 50

    def cleaning(self):
        self.house.mud -= 100
        self.fullness -= 20

    def find_a_cat(self, cat):
        self.cat = cat
        cprint('{} нашел кота'.format(self.name), color='cyan')

    def act(self):
        if self.cat.fullness <= 0:
            cprint('{} умер...'.format(self.cat.name), color='red')
            return
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.bowl == 0:
            self.cat_food()
        elif self.house.mud >= 100 :
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.bowl = 0       #миска для еды
        self.mud = 0        #количество грязи

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, в миске осталось {}, количество грязи {}'.format(
            self.food, self.money, self.bowl, self.mud)

class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def eat(self):
        cprint('{} поел'.format(self.name), color='yellow')
        self.fullness += 20
        self.house.bowl -= 10

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='yellow')
        self.fullness -= 10

    def tear_wallpaper(self):
        cprint('{} драл обои'.format(self.name), color='yellow')
        self.fullness -= 10
        self.house.mud += 5

    def act(self):
        if self.fullness < 20:
            self.eat()
        elif self.fullness >= 50:
            self.sleep()
        else:
            self.tear_wallpaper()



# citizens = [
#     Man(name='Бивис'),
#     Man(name='Батхед'),
#     Man(name='Кенни'),
# ]


my_sweet_home = House()
Garfield = Cat(name='Гарфилд')
Jon = Man(name='Джон')

Jon.go_to_the_house(house=my_sweet_home)
Jon.find_a_cat(cat=Garfield)
Garfield.go_to_the_house(house=my_sweet_home)


# for citisen in citizens:
#     citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    Jon.act()
    Garfield.act()
    print('--- в конце дня ---')
    print(Jon)
    print(Garfield)
    print(my_sweet_home)



# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
