giorgi_list = ["vaja", "daviti", "daviti2", True, 12]
res = ""

for index in range(5):
    res += str(giorgi_list[index]) 

print(res)  


rows = 5  

for i in range(1, rows+1):
  
    print(" " * (rows - i) + "*" * (2 * i - 1))

numbers = [9, 5, 94, 711, 52, 96, 71, 8]
smallest = numbers[0]  


responses = []

for i in range(5):
    answer = input(f"შეიყვანეთ პასუხი {i+1}-ზე: ")
    responses.append(answer)


for i in range(5):
    print(f"პასუხი {i+1}: {responses[i]}")



for num in numbers:
    if num < smallest: 
        smallest = num

print("ყველაზე პატარა ციფრი არის:", smallest)


import random

numbers = [9, 5, 94, 711, 52, 96, 71, 8]
random_item = numbers[random.randint(0, len(numbers) - 1)]

print("შემთხვევითი ელემენტი არის:", random_item)
