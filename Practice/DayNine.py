#TODO Создайте класс Человек (англ. Human). У человека должно быть поле “имя” (англ.
# name). На это поле в классе должен быть конструктор, get и set методы. Также, у
# Человека должен быть метод printInfo(), который выводит в консоль информацию
# о человеке в формате: “Этот человек с именем ИМЯ”.

#TODO Затем, создайте класс Студент (англ. Student), который наследуется от класса
# Человек. У студента есть дополнительное строковое поле - название его учебной
# группы. Для этого поля тоже необходимо создать геттер и сеттер. Конструктор в
# классе Студент должен принимать на вход два аргумента - имя и название учебной
# группы. Метод printInfo() в классе Студент должен быть переопределен таким
# образом, чтобы формат выводимого в консоль сообщения был таким:
# “Этот человек с именем ИМЯ”
# “Этот студент с именем ИМЯ”
# (должно выводиться именно две строки - необходимо использовать ключевое слово
# super)


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

class Teacher(Human):

