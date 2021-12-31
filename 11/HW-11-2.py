# * Допишите класс Unit:
# добавьте метод hit, который принимает обьект класса Unit, и наносит ему повреждения.
# удары юнита должны только уменьшать здоровье атакуемого юнита! на величину собственной атаки минус защита атакуемого юнита.
# добавьте проверку на здоровье таким образом, чтобы здоровье нельзя было
# установить < 0 (например у юнита осталось 5 здоровья а его ударили на 10)

class Unit:

    def __init__(self, name: str, health: int, attack: int, save: int):
        if not isinstance(name, str):
            print(f' must be str but you write {type(name)}')
            return
        self.name = name
        if not isinstance(health, int) :
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

    def hit(self):
        if self.health - (abs(self.save - self.attack)) < 0:
            self.health = 0
            return self.health
        return self.health - (abs(self.save - self.attack))



# self, name: str, health: int, attack: int, save: int
unit1 = Unit("1", 5, 2, 4)
unit1.print_info()

res = unit1.hit()
print(res)
