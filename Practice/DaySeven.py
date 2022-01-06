# 1. Для этого задания скопируйте класс Самолет из предыдущего дня в пакет текущего
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
        return isinstance(other, Airplane) and (self.__producer,self.__length,self.__year,self.__weight)< \
                (other.__producer,other.__length,other.__year,other.__weight)

    def __hash__(self):
        return hash(self.__producer, self.__length, self.__year, self.__weight)

    def compareAirplanesEq(self, other):
        if not isinstance(other, (int, Airplane)):
            raise TypeError('Must be int Airplane')
        return  (self.__producer,self.__length,self.__year,self.__weight) == \
                (other.__producer,other.__length,other.__year,other.__weight)


    def compareAirplaneslt(self, other):
        if not isinstance(other, (int, Airplane)):
            raise TypeError('Must be int Airplane')
        return (self.__producer,self.__length,self.__year,self.__weight) < \
                (other.__producer,other.__length,other.__year,other.__weight)



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
f =airplane.compareAirplaneslt(airplane2)
print(f)
airplane.fuel(1)
airplane.fuel(1)
airplane.fuel(10)
airplane.fuel(10)
print(airplane)
