#1
def opposite(number):
    return -number

print(opposite(1))   
print(opposite(-34)) 
print(opposite(0)) 


#2 
def repeat_str(n, s):
    return s * n


print(repeat_str(6, "I"))      
print(repeat_str(5, "Hello"))  
print(repeat_str(0, "World"))


#3
def greet():
    return "hello world!"

print(greet())



#4
def count_sheeps(sheep):
  # TODO May the force be with you
  return sheep.count(True)

#5
def no_space(x):
    return x.replace(" ", "")


#6
def litres(time):
    return int(time * 0.5)
