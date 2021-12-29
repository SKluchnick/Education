class Animal:

    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')


class Dog(Animal):

    def __init__(self, name: str, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f'{self.name} is barking')


class Cat(Animal):

    def meow(self):
        print(f'{self.name} says Meow')


class Frog(Animal):

    def eat(self):
        # super().eat()
        print(f'Frog {self.name} is eating')


dog = Dog('dog', 'big')
cat = Cat('cat')
frog = Frog('frog')

frog.eat()
cat.meow()
dog.bark()