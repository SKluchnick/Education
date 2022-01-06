class Human:

    def __init__(self, name):
        self.varifyStr(name)
        self.__name = name

    def varifyStr(self, value):
        if not isinstance(value, str):
            raise TypeError('Must be str')


    @property
    def name(self):
        return self.name()

    @name.setter
    def name(self, value):
        self.varifyStr(value)
        self.__name = value

    def printInfo(self):
        print(f'I am human my name is {self.__name}')

human = Human('Bob')
human.printInfo()


class Student(Human):

    def __init__(self, name , nameSubject):
        super().__init__(name)
        self.varifyStr(nameSubject)
        self.__nameSubject = nameSubject

    def printInfo(self):
        super().printInfo()
        print(f'My subject is {self.__nameSubject}')

    def varifyStr(self, value):
        if not isinstance(value, str):
            raise TypeError('Must be str')

    @property
    def nameSubject(self):
        return self.__nameSubject

    @nameSubject.setter
    def nameSubject(self, value):
        self.varifyStr(value)
        self.__nameSubject = value

student = Student('Peter','Math')
student.printInfo()

class Figure:

    def __init__(self, color):
        self.varifyStr(color)
        self.__color = color

    def area(self):
        pass

    def perimetr(self):
        pass

    def varifyStr(self, value):
        if not isinstance(value, str):
            raise TypeError('Must be str')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.varifyStr(value)
        self.__color = value



class Triangle(Figure):

    def __init__(self, x, y, z, color):
        super().__init__(color)
        self.varifyInt(x)
        self.varifyInt(y)
        self.varifyInt(z)
        self.__x = x
        self.__y = y
        self.__z = z

    def area(self):
        return self.__x + self.__z + self.__z

    def perimetr(self):
        res = self.area()
        return res * 2

    def varifyInt(self, value):
        if not isinstance(value, int):
            raise TypeError('Must be int')

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.varifyInt(value)
        self.__x = value

    @property
    def y(self):
        return self.__x

    @y.setter
    def y(self, value):
        self.varifyInt(value)
        self.__y = value

    @property
    def z(self):
        return self.__z

    @y.setter
    def z(self, value):
        self.varifyInt(value)
        self.__z = value



class Circle(Figure):

    def __init__(self, x, color):
        super().__init__(color)
        self.varifyInt(x)
        self.__x = x

    def area(self):
        return self.__x

    def perimetr(self):
        res = self.area()
        return res * 2

    def varifyInt(self, value):
        if not isinstance(value, int):
            raise TypeError('Must be int')

    @property
    def x(self):
        return self.__color

    @x.setter
    def x(self, value):
        self.varifyInt(value)
        self.__x = value


lst = [Triangle(1,1,1,'red'),Triangle(1,1,1,'blue'),Triangle(1,1,1,'red'),Circle(1,'red'),Circle(1,'blue')]

def calculateRedArea(value):
    sum = 0
    for i in value:
        if i.color == 'red':
            sum += i.area()
    return sum

res = calculateRedArea(lst)
print(res)

def calculateRedPerimeter(value):
    sum = 0
    for i in value:
        if i.color == 'red':
            sum += i.perimetr()
    return sum

res = calculateRedPerimeter(lst)
print(res)

