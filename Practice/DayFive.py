# Задачи:
# 1. Создать класс Автомобиль (англ. Car), с полями “Год выпуска”, “Цвет”, “Модель”.
# Создать get и set методы для каждого поля. Создать экземпляр класса Автомобиль,
# задать сеттером каждое поле, вывести в консоль значение каждого поля геттером.
# Созданный вами класс должен отвечать принципам инкапсуляции.

class Car:

    def __init__(self, yearsOfProduct: int, color: str, model: str):
        self.varifyInt(yearsOfProduct)
        self.varifyStr(color)
        self.varifyStr(model)
        self.__yearsOfProduct = yearsOfProduct
        self.__color = color
        self.__model = model

    @classmethod
    def varifyStr(cls, value):
        if not isinstance(value, str):
            raise TypeError("Must be str")

    @classmethod
    def varifyInt(cls, value):
        if not isinstance(value, int):
            raise TypeError("Must be int")

    @property
    def YearsOfProduct(self):
        return self.__yearsOfProduct

    @YearsOfProduct.setter
    def YearsOfProduct(self, value):
        self.varifyInt(value)
        self.__yearsOfProduct = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.varifyStr(value)
        self.__color = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.varifyInt(value)
        self.__model = value


car = Car(1, 'blue', "BMV")
print(car.color)
print(car.model)
print(car.YearsOfProduct)


#
# Задачи:
# 2. Создать класс Мотоцикл (англ. Motorbike), с полями “Год выпуска”, “Цвет”,
# “Модель”. Создать экземпляр класса Мотоцикл, с помощью конструктора (сеттеры не
# использовать). Придерживаться принципов инкапсуляции и использовать ключевое
# слово this. Геттером получить год выпуска, цвет, модель, вывести значения в
# консоль

class Bike:

    def __init__(self, yearsOfProduct: int, color: str, model: str):
        if not isinstance(yearsOfProduct, int) or not isinstance(color,str) or not isinstance(model,str):
            raise TypeError ('(yearsOfProduct, int) (color,str) (model,str)')
        self.__yearsOfProduct = yearsOfProduct
        self.__color = color
        self.__model = model



    @property
    def YearsOfProduct(self):
        return self.__yearsOfProduct


    @property
    def color(self):
        return self.__color



    @property
    def model(self):
        return self.__model



bike = Bike(1, 'blue', "BMV")
print(bike.color)
print(bike.model)
print(bike.YearsOfProduct)

