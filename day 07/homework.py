age = int(input("15 "))


is_valid_age = 13 < age < 19


print("13 ზე მეტი და 19 ზე ნაკლები" * is_valid_age or "1")


score = int(input("ნუგზარ, რა ნიშანი მიიღეთ საკონტროლოზე (1-10)? "))


is_A = score >= 9
is_B = 8 <= score < 9
is_C = 7 <= score < 8
is_D = 6 <= score < 7
is_F = score < 6


print("Is A: " + str(is_A))
print("Is B: " + str(is_B))
print("Is C: " + str(is_C))
print("Is D: " + str(is_D))
print("Is F: " + str(is_F))


true_value = True
false_value = False


print("True and True: " + str(true_value and true_value))
print("True and False: " + str(true_value and false_value))
print("False and True: " + str(false_value and true_value))
print("False and False: " + str(false_value and false_value))

print("True or True: " + str(true_value or true_value))
print("True or False: " + str(true_value or false_value))
print("False or True: " + str(false_value or true_value))
print("False or False: " + str(false_value or false_value))

print("Not True: " + str(not true_value))
print("Not False: " + str(not false_value))


num1 = 7
num2 = 5


print("num1 == num2:", num1 == num2)
print("num1 < num2:", num1 < num2)
print("num1 > num2:", num1 > num2)
print("num1 <= num2:", num1 <= num2)
print("num1 >= num2:", num1 >= num2)
print("num1 != num2:", num1 != num2)


a = 10
b = 5
c = 7

is_a_greatest = a > b and a > c
is_b_middle = (b > a and b < c) or (b < a and b > c)
is_c_least = c < a and c < b

print("is_a_greatest:", is_a_greatest)
print("is_b_middle:", is_b_middle)
print("is_c_least:", is_c_least)


score = 85

is_pass = score >= 50
is_high_pass = 75 < score < 90
is_perfect = score == 100
is_failing = score < 50


print("is_pass:", is_pass)
print("is_high_pass:", is_high_pass)
print("is_perfect:", is_perfect)
print("is_failing:", is_failing)



P = True  
Q = False  


P_and_not_Q = P and not Q  
not_P_and_Q = not P and Q  
P_xor_Q = (P and not Q) or (not P and Q)  


print("P_and_not_Q:", P_and_not_Q)
print("not_P_and_Q:", not_P_and_Q)
print("P_xor_Q:", P_xor_Q)
