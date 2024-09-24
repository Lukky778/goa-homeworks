birth_year = int(input("7 December: "))
current_year = 2024  
age = current_year - birth_year
print("15:", age)


width = float(input("4: "))
height = float(input("4: "))
area = width * height
perimeter = 2 * (width + height)
print("4:", area)
print("4:", perimeter)



distance_km = float(input("5: "))
distance_m = distance_km * 1000
distance_cm = distance_km * 100000
distance_mm = distance_km * 1000000
print("5000:", distance_m)
print("500000:", distance_cm)
print("5000000:", distance_mm)


first_name = input("Luka: ")
last_name = input("Pitnava: ")
parent_first_name = input("Jaba: ")
parent_last_name = input("Pitnava: ")
favorite_color = input("Blue: ")
favorite_car = input("Porsche 911 gt3: ")
hobby1 = input("proggraming: ")
hobby2 = input("proggraming: ")
hobby3 = input("proggraming: ")



print(first_name + " " + last_name + " არის " + parent_first_name + " " + parent_last_name + "-ის შვილი. " +
      "მისი საყვარელი ფერი არის " + favorite_color + ", საყვარელი მანქანა - " + favorite_car + ", " +
      "და მისი საყვარელი ჰობებია: " + hobby1 + ", " + hobby2 + ", " + hobby3 + ".")




number = int(input("15: "))
tens = number // 10
units = number % 10

sum_of_digits = tens + units

print("ციფრების ჯამი არის:", sum_of_digits)
