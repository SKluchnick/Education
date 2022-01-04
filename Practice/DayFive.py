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
    def model (self , value):
        self.varifyInt(value)
        self.__model = value


car = Car(1, 'blue', "BMV")
print(car.color)
print(car.model)
print(car.YearsOfProduct)
