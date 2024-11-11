for i in range(1, 50, 2):
    print(i)
    
    i = 1
while i < 50:
    print(i)
    i += 2
    
    
    size = 5  
for i in range(size):
    print('*' * size)
    
    size = 5
i = 0
while i < size:
    print('*' * size)
    i += 1
    
    width = 8
height = 4
for i in range(height):
    print('*' * width)
    
    width = 8
height = 4
i = 0
while i < height:
    print('*' * width)
    i += 1
    
    for num1 in range(3):
        for num in range(3):  
            print("num1:", num1, "num:", num)
            
            
            
            print("სარეგისტრაციო ფორმა")

username = ""
password = ""
confirm_password = ""

while True:
    username = input("შეიყვანეთ მომხმარებლის სახელი: ")
    if len(username) < 3:
        print("მომხმარებლის სახელი უნდა იყოს მინიმუმ 3 სიმბოლო.")
        continue

    password = input("შეიყვანეთ პაროლი: ")
    if len(password) < 6:
        print("პაროლი უნდა იყოს მინიმუმ 6 სიმბოლო.")
        continue

    confirm_password = input("გაიმეორეთ პაროლი: ")
    if password != confirm_password:
        print("პაროლები არ ემთხვევა. სცადეთ ხელახლა.")
        continue

    print("რეგისტრაცია წარმატებით დასრულდა!")
    break