# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer
    
class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest
    
class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'
    
    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
    
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 50
        self._attack = 50
        self._color = 'чёрный'
    
    def question(self):
        x = randint(50, 100)
        y = randint(50, 100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
    
class Сunning(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 75
        self._color = 'хитрый'

    def question(self):
        x = randint(1, 5)
        self.__quest = 'Спорим не угадаешь!(4)'
        self.set_answer(x)
        return self.__quest

class Easy(Troll):
    def __Prime(self, x):
        i = 2
        while i * i <= x:
            if x % i == 0:
                return 0
            i += 1
        return 1
    
    def __init__(self):
        self._health = 50
        self._attack = 75
        self._color = 'Хацкер'

    def question(self):
        x = randint(11231, 1010203)
        self.__quest = 'Это число ' + str(x) + ' простое? Мне для взлома нужно...(да: 1 нет: 0)'
        self.set_answer(self.__Prime(x))
        return self.__quest

class Ridiculing(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 1000
        self._color = 'Скоморох'

    def __decr(self, x):
        result = []
        for i in range(1, x+1):
            if x % i == 0:
                result.insert(str[i])
        return ",".join(result)

    def question(self):
        x = randint(1000, 5000)
        self.__quest = 'А мне на множетели разложи, и отсортируй!!!' + str(x) + 'типо так: 7,3,2,kek(42)'
        self.set_answer(self.__decr(x))
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon, Сunning, Easy, Ridiculing]
