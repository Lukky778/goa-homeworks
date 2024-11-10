
name = input("თქვენი სახელი: ")


result = ""


i = 0
while i < len(name):
    result += name[i] + " "
    i += 1


print("სახელი სფეისებით:", result.strip())


start = int(input("შეიყვანეთ დიაპაზონის დასაწყისი: "))
end = int(input("შეიყვანეთ დიაპაზონის ბოლო: "))

i = start
while i <= end:
    if i % 2 == 0 and i % 3 == 0:
        print(f"ეს ციფრები არის 3-ისა და 2-ის ჯერადები: {i}")
    else:
        print(f"{i} არ არის 3-ისა და 2-ის ჯერადები")
    i += 1


result = 0
i = 0


while i < 5:
    number = float(input(f"შეიყვანეთ ციფრი #{i + 1}: "))
    result += number
    i += 1


average = result / 5
print(f"საშუალო არითმეტიკული: {average}")


i = -100
while i <= 100:
    if i > 0:
        print(i)
    i += 1

number = int(input("შეიყვანეთ დადებითი ციფრი: "))

while number >= 0:
    number = int(input("შეიყვანეთ დადებითი ციფრი: "))

print("თქვენი ციფრი უარყოფითი იყო. პროგრამა დასრულდა.")


# boss level


for i in range(1, 11):

    print("*" * i, end="")

    print(" " * (10 - i) * 2, end="")

    print("*" * i)
