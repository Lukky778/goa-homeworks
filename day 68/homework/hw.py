#1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

#2
class Car:
    def drive(self):
        print("The car is driving")
    
    def stop(self):
        print("The car has stopped")
        
        
#3
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    
#4
class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def introduce(self):
        print(f"My name is {self.name}, I study {self.subject} and my grade is {self.grade}.")



#5
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")