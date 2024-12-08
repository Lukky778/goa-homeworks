age = int(input(" რამდენი წლის ხართ? "))
print("თქვენ ბავშვები ხართ." * (age < 18))
print("თქვენ ზრდასრულები ხართ." * (18 <= age < 65))
print("თქვენ სიბერეში ხართ." * (age >= 65))


celsius = float(input("შეიტანეთ ტემპერატურა ცელსიუსში: "))
fahrenheit = (celsius * 9/5) + 32
print("ტემპერატურა ფარენჰაიტში არის:", fahrenheit)


print(5 > 3)   
print(5 < 3)   
print(5 == 5) 


print(True and False)  
print(True or False)   
print(not True)        


height = 5  

for i in range(1, height + 1):
    print('*' * i)



user_age = 20  
is_twenty = user_age == 20
print(is_twenty)  
