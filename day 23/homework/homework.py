list_of_names = ["დავით", "გიორგი", "ნიკა", "დავით", "თეა", "დავით"]

name_to_count = "დავით"
count = list_of_names.count(name_to_count)

print(name_to_count + " მეორდება " + str(count) + " ჯერ.")

numbers = [1, 2, 3, 4, 5]


numbers.reverse()

print("გადატრიალებული სია:", numbers)


list_of_numbers = [1, 2, 3]

repeated_list = list_of_numbers * len(list_of_numbers)

print("გადამოწმებული სია:", repeated_list)


insert_arr = ["Python", "Java", "C++"]


insert_arr.insert(1, "დავით")

print("განახლებული სია:", insert_arr)


list_of_items = ["apple", "banana", "orange", "banana", "kiwi"]


count_banana = list_of_items.count("banana")
print("'banana' რაოდენობა სიაში: " + str(count_banana))
list_of_items.remove("banana")

print("განახლებული სია:", list_of_items)
