#1
def repeat_str(repeat, string):
    return string * repeat

#2
def make_upper_case(s):
    return s.upper()

#3
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)


#4
class MyCat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"კატა: {self.name}"


#5
class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


#6
class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} წლის"

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_age(self):
        return f"{self.age} წლისაა"
