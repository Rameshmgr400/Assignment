# Class Car

class Car:
    b = 'BMW'
    a = 'Audi'
    m= 'Mercedes'
    def bmw(self):
        a = 'randomcar'
        print(f'Hello, Its Me {self.b}!')
    def audi(self):
        print(f'Hello, Its Me {self.a}!')
    def mercedes(self):
        print(f'Hello, Its Me {self.m}!')
    def tesla(self):
        print(f'Hello, Its Me Tesla!')
obj = Car()
obj.bmw()
obj.audi()
obj.mercedes()
obj.tesla()


#Clas Person

class Person:    
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Ramesh')
p.say_hi()

q = Person('Dhan Bahadur')
q.say_hi()
