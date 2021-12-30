# Напишите класс Unit, реализуйте в нем атрибуты "имя", "здоровье", "атака", "защита". Обеспечьте передачу
# в "имя" только строчных данных, в "здоровье", "атака", "защита" - только числовых

class Unit:

    def __init__(self, name: str, health: int, attack: int, save: int):
        if not isinstance(name, str):
            print(f' must be str but you write {type(name)}')
            return
        self.name = name
        if not isinstance(health, int):
            print(f' must be int but you write {type(health)}')
            return
        self.health = health
        if not isinstance(attack, int):
            print(f' must be int but you write {type(attack)}')
            return
        self.attack = attack
        if not isinstance(save, int):
            print(f' must be int but you write {type(save)}')
            return
        self.save = save

    def print_info(self):
        print(self.save, self.health, self.attack, self.name)


unit1 = Unit("1", 2, 3, 4)
unit1.print_info()


class UnitSecond:

    def __init__(self, name: str, health: int, attack: int, save: int):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__save = save

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if isinstance(val, str):
            self.__name = val
        else:
            return

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, val):
        if isinstance(val, int):
            self.__name = val
        else:
            return

    @property
    def attack(self):
        return self.__attack

    @health.setter
    def attack(self, val):
        if isinstance(val, int):
            self.__name = val
        else:
            return

    @property
    def save(self):
        return self.__save

    @health.setter
    def save(self, val):
        if isinstance(val, int):
            self.__name = val
        else:
            return


unitsecond = UnitSecond(1, 2, 3, 4)
# unitsecond.name = 25
print(unitsecond.name)
unitsecond.name = 11
print(unitsecond.name)
