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
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14159 * radius * radius  

circle = Circle(10)
    
#4
class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def introduce(self):
        return f"My name is {self.name}, I study {self.subject} and my grade is {self.grade}."
    
#5
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. Balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount <= 0:
            return "Withdraw amount must be positive."
        else:
            self.balance -= amount
            return f"Withdrew {amount}. Balance: {self.balance}"