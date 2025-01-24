my_set = {1, 2, 3}

my_set.add(4)
print("After add:", my_set)

my_set.update([5, 6, 7])
print("After update:", my_set)

my_set.remove(7)
print("After remove:", my_set)

my_set.discard(8)
print("After discard:", my_set)

popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After pop:", my_set)

my_set.clear()
print("After clear:", my_set)

my_info = {
    "name": "John",
    "surname": "Doe",
    "age": 30,
    "city": "Tbilisi"
}
print("Keys:", my_info.keys())

print("Values:", my_info.values())

def AddToDatabase(name, surname, age):
    database = {}
    database["name"] = name
    database["surname"] = surname
    database["age"] = age
    return database

db_entry = AddToDatabase("Jane", "Smith", 25)
print("Database entry:", db_entry)
