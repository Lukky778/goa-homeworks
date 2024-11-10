age = int(input("რამდენი წლის ხართ? "))
for i in range(age):
    print("საიტერაციო ცვლადი: " + str(i))

celsius = float(input("მიუთითეთ ტემპერატურა ცელსიუსში: "))
fahrenheit = (celsius * 9/5) + 32
print("ტემპერატურა ფარენჰეიტში: " + str(fahrenheit) + "°F")


print(5 > 3)


print(10 <= 10)

print(7 != 2)

print(True and False)

print(True or False)

print(not True)

rows = 5
for i in range(1, rows + 1):
    print('*' * i)

age = int(input("რამდენი წლის ხართ? "))
if age == 20:
    print(True)
else:
    print(False)
