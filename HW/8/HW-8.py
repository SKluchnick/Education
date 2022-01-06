class Person:
    pass

p1 = Person()
p1.name = 'Bob'
p1.sername = 'Bobov'
p1.placeOfBirth = 'Germany'

p2 = Person()
p2.name = 'Bob2'
p2.sername = 'Bobov2'
p2.placeOfBirth = 'Ukraine'

print(p2.name)
print(p1.name)
print(f'{p2.name} {p1.name}')

# TODO _______________________________________

class Person:
    pass

    def print_info(self):
        print(f'{self.name} {self.sername} {self.sername} {self.placeOfBirth}')

p1 = Person()
p1.name = 'Bob'
p1.sername = 'Bobov'
p1.placeOfBirth = 'Germany'

p2 = Person()
p2.name = 'Don'
p2.sername = 'Donov'
p2.placeOfBirth = 'Ukraine'

p1.print_info()
p2.print_info()

Person.print_info(p1)
Person.print_info(p2)

# TODO _______________________________________
class Person:
    pass

    def print_info(self, n: int):
        for i in range(n):
            print(f'{self.name} {self.sername} {self.sername} {self.placeOfBirth}')

    def calculate_of_year(self, current_year: int):
        return current_year - self.dateOfBirth


p1 = Person()
p1.name = 'Bob'
p1.sername = 'Bobov'
p1.placeOfBirth = 'Germany'
p1.dateOfBirth = 1995

print(p1.calculate_of_year(2021))
Person.print_info(p1, 3)

# TODO _______________________________________
class Person:
    def __init__(self, name, surname, placeOfBirth, dateOfBirth):
        self.name = name
        self.sername = surname
        self.placeOfBirth = placeOfBirth
        self.dateOfBirth = dateOfBirth

    def print_info(self, n: int):
        for i in range(n):
            print(f'{self.name} {self.sername} {self.sername} {self.placeOfBirth} {self.dateOfBirth}')

    def calculate_of_year(self, current_year: int):
        return current_year - self.dateOfBirth



person1 = Person('Bob', 'Bobov', 'Germany', 1995)

person1.print_info(2)
print(person1.calculate_of_year(2000))

# TODO _______________________________________

class Person:
    some_num = 25

    def __init__(self, name, surname, placeOfBirth, dateOfBirth):
        self.name = name
        self.sername = surname
        self.placeOfBirth = placeOfBirth
        self.dateOfBirth = dateOfBirth

    def print_info(self, n: int):
        for i in range(n):
            print(f'{self.name} {self.sername} {self.sername} {self.placeOfBirth} {self.dateOfBirth}')

    def calculate_of_year(self, current_year: int):
        return current_year - self.dateOfBirth
#
#
#
person1 = Person('Bob', 'Bobov', 'Germany', 1995)

person1.print_info(2)
print(person1.calculate_of_year(2000))

print (person1.some_num)
print(Person.some_num)

person1.some_num = 456
print (person1.some_num)

# TODO _______________________________________
class Circle:

    PI = 3.14


    def __init__(self, radius: int):
        self.radius = radius

    def get_perimetr(self):
        return self.radius * 2 * self.PI

    def get_aria(self):
        return self.PI * self.radius ** 2


circle1 = Circle(5)
print(circle1.get_perimetr())
print(circle1.get_aria())

circle2 = Circle(15)
print(circle2.get_perimetr())
print(circle2.get_aria())

# TODO _______________________________________

class Person:

    People_count = 0

    def __init__(self, name, surname, placeOfBirth, dateOfBirth):
        self.name = name
        self.sername = surname
        self.placeOfBirth = placeOfBirth
        self.dateOfBirth = dateOfBirth

        Person.People_count += 1

    def print_info(self, n: int):
        for i in range(n):
            print(f'{self.name} {self.sername} {self.sername} {self.placeOfBirth} {self.dateOfBirth}')

    def calculate_of_year(self, current_year: int):
        return current_year - self.dateOfBirth
#
#
#
# person1 = Person('Bob', 'Bobov', 'Germany', 1995)
# print(Person.People_count)
#
# person2 = Person('Bob', 'Bobov', 'Germany', 1995)
# print(Person.People_count)

# TODO _______________________________________
# TODO _______________________________________
# TODO _______________________________________
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print('Person created')

    def say_hello(self):
        print(f'{self.name} {self.age} hello bro ')


# person1 = Person('Bob', 15)
# person1.say_hello()


class Student(Person):




    def __init__(self, name, age , averGrade):
        super().__init__(name, age)
        # print("hello")
        self.averGrade = averGrade

    def study(self):
        print(f' {self.name}  studies')

    def say_hello(self):
        # super().say_hello()
        print('super().say_hello()')


class Teacher(Person):
    pass

    def teach(self):
        print(f' {self.name}  teaches')

#
teacher1 = Teacher('Kate', 35)
# teacher1.say_hello()
# teacher1.teach()

student1 = Student('Mike', 25 , 14)
student1.say_hello()
# student1.study()
# student1.say_hello()





def introduce(p):
    print('Now person ')
    p.say_hello




    people_array = [Student('Mike', 25 , 14)]

    for person1 in people_array:
        introduce(person1)