import random

# Задаstudent=None этого задания скопируйте классы Автомобиль и Мотоцикл из предыдущего дня
# в пакет текущего дня.
# В классах Автомобиль и Мотоцикл реализовать два метода:
# info() - выводит в консоль строку “Это автомобиль” (или “Это мотоцикл”),
# yearDifference() - принимает на вход число (год), и возвращает разницу между
# переданным годом и годом выпуска транспортного средства

class Car:

    def __init__(self, yearsOfProduct: int, color: str, model: str):
        self.varifyInt(yearsOfProduct)
        self.varifyStr(color)
        self.varifyStr(model)
        self.__yearsOfProduct = yearsOfProduct
        self.__color = color
        self.__model = model

    def yearDifference(self, value):
        self.varifyInt(value)
        return abs(self.__yearsOfProduct - value)

    def info(self):
        print('This is car')

    def varifyStr(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be str")

    def varifyInt(self, value):
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


car = Car(1950, 'blue', "BMV")
res = car.yearDifference(2020)
print(res)
car.info()
print(car.color)
print(car.model)
print(car.YearsOfProduct)


# 2. Создать класс Самолет (Airplane) с полями:
# - producer (изготовитель)
# - year (год выпуска)
# - length (длина)
# - weight (вес)
# - fuel (количество топлива в баке) + геттер для этого поля
# Создать конструктор в классе Самолет, принимающий в качестве аргументов значения
# четырех полей класса (значение поля “количество топлива в баке” установить равным
# 0). В конструкторе для передачи полям значений использовать ключевое слово this.
# Помимо этого, в классе необходимо реализовать метод info(), который выводит
# сообщение в следующем формате:
# “Изготовитель: … , год выпуска: … , длина: ..., вес: ..., количество топлива в баке: …”
# Также, необходимо реализовать метод fillUp(), который в качестве аргумента
# принимает число и заправляет топливный бак самолета на это значение.
# Создать новый объект класса Самолет с произвольными данными.
# Изменить год выпуска и длину с помощью сеттеров, вызвать метод fillUp() два
# раза, передав разные значения. Вызвать метод info().
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




airplane = Airplane("g", 1, 2, 3)
airplane.fuel(1)
airplane.fuel(1)
airplane.fuel(10)
airplane.fuel(10)
print(airplane)


# 3. Создать класс Teacher (Преподаватель), имеющий поля “Имя”, “Предмет”. Создать
# класс Student (Студент) с полем “Имя”.
# Каждый класс имеет конструктор (с параметрами), set и get методы по
# необходимости, а также у преподавателя есть метод evaluate (оценить студента),
# принимающий в качестве аргумента студента, и работающий следующим образом:
# внутри метода случайным образом генерируется число от 2 до 5, выводится строка:
# "Преподаватель ИМЯПРЕПОДАВАТЕЛЯ оценил студента с именем ИМЯСТУДЕНТА
# по предмету ИМЯПРЕДМЕТА на оценку ОЦЕНКА."
# Все слова, написанные большими буквами, должны быть заменены
# соответствующими значениями. ОЦЕНКА должна принимать значения "отлично”,
# "хорошо”, "удовлетворительно" или "неудовлетворительно", в зависимости от
# значения случайного числа.
# Создайте по 1 экземпляру каждого класса, у преподавателя вызовите метод оценки
# студента, передав студента в качестве аргумента метода


class Student:

    def __init__(self, name: str):
        self.varifyStr(name)
        self.__name = name


    def __str__(self):
        return f'{self.__name}  {self.__class__}'


    def varifyStr(self, value):
        if not isinstance(value, str):
            raise TypeError('Must be str')


    @property
    def producer(self):
        return self.__name

    @producer.setter
    def producer(self, val):
        self.varifyStr(val)
        self.__name = val

a = Student('g')


class Teacher:



    def __init__(self, nameT: str, subject: str):
        self.varifyStr(nameT)
        self.__nameT = nameT
        self.__subject = subject


    def __str__(self):
        return f'{self.__nameT} {self.__subject} '


    def varifyStr(self, value):
        if not isinstance(value, str):
            raise TypeError('Must be str')



    @property
    def nameT(self):
        return self.__nameT

    @nameT.setter
    def producer(self, val):
        self.varifyStr(val)
        self.__nameT = val

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, val):
        self.varifyInt(val)
        self.__length = val

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, val):
        self.varifyInt(val)
        self.__subject = val

    def evaluate (self, Student):
        rand = random.randint(1, 5)
        print(rand)
        res = ''
        if rand == 1:
            res = 'Bad'
        elif rand == 2:
            res = 'Also Bad'
        elif rand == 3:
            res = 'Not Bad'
        elif rand == 4:
            res = 'Good'
        elif rand == 5:
            res = 'Well'
        print(f'{self.__nameT} {self.__subject} {res} {Student}')


t = Teacher('Don','math')
t.evaluate(Student('Bob'))
t.evaluate(Student('Gib'))




