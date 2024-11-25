
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'o', 'u']


vowels = ['a', 'e', 'i', 'o', 'u']


vowel_count = 0
for letter in letters:
    if letter in vowels:
        vowel_count += 1

print("ხმოვნების რაოდენობა: " + str(vowel_count))


numbers = []


for i in range(1, 101):
    if i % 5 == 0 or i % 3 == 0:
        numbers.append(i)

print("5-ისა და 3-ის ჯერადები: " + str(numbers))



elements = ['a', '1', 'b', '2', 'c', '3', 'd', '4']

combined_str = ''.join(elements)

print("წარმოდგენილი სტრინგი: " + combined_str)


n = 6  

for i in range(n):
    print(" " * i + "*" * (n - i))

for i in range(1, n):
    print(" " * (n - i - 1) + "*" * (i + 1))



age = int(input("მეთქი რამდენი წლის ხარ? "))

if age > 12:
    print("შენ არ ხარ 12 წლის")
else:
    print("შენ ხარ " + str(age) + " წლის!")
