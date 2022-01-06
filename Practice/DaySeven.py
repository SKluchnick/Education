# TODO 1. Для этого задания скопируйте класс Самолет из предыдущего дня в пакет текущего
# дня.
# В классе Самолет создать статический метод compareAirplanes, который в
# качестве аргументов принимает два объекта класса Airplane (два самолета) и выводит
# сообщение в консоль о том, какой из самолетов длиннее.

class Airplane:

    def __init__(self, producer: str, year: int, length: int, weight: int):
        self.varifyStr(producer)
        self.varifyInt(year)
        self.varifyInt(length)
        self.varifyInt(weight)
        self.__producer = producer
        self.__year = year
        self.__length = length
        self.__weight = weight
        self.__fuel = 0

    def __str__(self):
        return f'{self.__producer} {self.__year} {self.__weight} {self.weight} {self.__fuel} {self.__class__}'

    def __eq__(self, other):
        return isinstance(other, Airplane) and self.__producer == other.__producer and \
               self.__length == other.__length and self.__year == other.__year and self.__weight == other.__weight

    def __lt__(self, other):
        return isinstance(other, Airplane) and (self.__producer, self.__length, self.__year, self.__weight) < \
               (other.__producer, other.__length, other.__year, other.__weight)

    def __hash__(self):
        return hash(self.__producer, self.__length, self.__year, self.__weight)

    def compareAirplanesEq(self, other):
        if not isinstance(other, (int, Airplane)):
            raise TypeError('Must be int Airplane')
        return (self.__producer, self.__length, self.__year, self.__weight) == \
               (other.__producer, other.__length, other.__year, other.__weight)

    def compareAirplaneslt(self, other):
        if not isinstance(other, (int, Airplane)):
            raise TypeError('Must be int Airplane')
        return (self.__producer, self.__length, self.__year, self.__weight) < \
               (other.__producer, other.__length, other.__year, other.__weight)

    def varifyInt(self, value):
        if not isinstance(value, int):
            raise TypeError('Must be int')

    def varifyStr(self, value):
        if not isinstance(value, str):
            raise TypeError('Must be str')

    def fuel(self, val):
        self.varifyInt(val)
        self.__fuel += val

    @property
    def producer(self):
        return self.__producer

    @producer.setter
    def producer(self, val):
        self.varifyStr(val)
        self.__producer = val

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, val):
        self.varifyInt(val)
        self.__length = val

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, val):
        self.varifyInt(val)
        self.__weight = val


airplane = Airplane("g", 100, 20, 3)
airplane2 = Airplane("g", 10, 20, 3)
f = airplane.compareAirplaneslt(airplane2)
print(f)
airplane.fuel(1)
airplane.fuel(1)
airplane.fuel(10)
airplane.fuel(10)
print(airplane)


#TODO 2. Дворовый футбол.
# Для игры в футбол во дворе требуется 6 человек (3х3). Класс Игрок (англ. Player),
# содержит следующие поля:
# - поле “выносливость” (англ. stamina), разное для каждого экземпляра
# - константы “максимальная выносливость” (англ. MAX_STAMINA) со значением
# 100 и “минимальная выносливость” (англ. MIN_STAMINA) со значением 0,
# единые для всех экземпляров
# - статическое поле countPlayers, которое считает количество игроков на
# футбольном поле (изначально их 0, выходом на поле считается создание
# экземпляра класса, уходом - когда игрок устал).
# - геттер для поля “выносливость”
# и следующие методы:
# run() - Игрок бежит при вызове этого метода. Этот метод уменьшает выносливость
# на 1 при однократном вызове. Когда выносливость достигает 0, игроку нужен отдых и
# он уходит с поля.
# info() - выводит сообщение в зависимости от количества игроков на поле. Если
# игроков меньше 6, то выводит сообщение: “Команды неполные. На поле еще есть ...
# свободных мест”, иначе: “На поле нет свободных мест”. Грамматикой русского языка
# пренебречь, т.е. фраза “еще есть 1 свободных мест” допустима.
# Задание: Создать класс Player по вышеописанному шаблону. Экземпляр класса при
# создании должен иметь значение выносливости от 90 до 100 (генерировать внутри
# конструктора). Создать 6 игроков, вызвать метод info(). При попытке создать 7,8 …
# n игрока, количество игроков на поле меняться не должно, проверить это.
# Примените к игроку метод run(), пока он полностью не выдохнется (отрицательное
# значение выносливости не допускается). Вывести количество игроков на поле.
# По желанию: доработать метод info() так, чтобы при выводе в консоль грамматика
# русского языка учитывалась

class Player:
    __count = 0

    def __init__(self, stamina):
        self.varifyInt(stamina)
        self.stamina = stamina
        if Player.__count < 6:
            Player.__count += 1

    def __str__(self):
        return f'{self.stamina} {self.__count}'

    def varifyInt(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be int")

    def run(self):
        if self.stamina == 0:
            return
        self.stamina -= 1
        if self.stamina == 0:
            Player.__count -= 1

    @classmethod
    def info (cls):
        if cls.__count <= 6:
            print(cls.__count)
            print ('Ok')
        else:
            print ('Lol')



player = Player(10)
player2 = Player(15)
player3 = Player(15)
player4 = Player(15)
player5 = Player(15)
player6 = Player(15)


for i in range(1,12):
    player.run()

Player.info()

