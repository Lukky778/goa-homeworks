#1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"მანქანა: {self.brand} {self.model}, გამოშვების წელი: {self.year}")


#2
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def is_passing(self):
        return self.grade > 5


#3
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")


#4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


#5
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"სათაური: {self.title}, ავტორი: {self.author}, წელი: {self.year}")
