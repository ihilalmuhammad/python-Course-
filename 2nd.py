# "Alice" string
# "Bob"
# 3647 integer
# 383 
# 4.5 float
# True/False boolean

# Variables
name = "Alice"
age = 23
height = 5.5
is_student = True

print("My name is " + name + ", I am " + str(age) + " years old, my height is " + str(height) + " feet, and it is " + str(is_student) + " that I am a student.")

# list 
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
fruits.append("orange")
numbers.remove(3)
print(fruits)
print(numbers)


# dictionary 
Student = {
    "name" : "alice",
    "age" :23,
    "height" : 5.5,
    "sex" : "male",
    "semester" : "python",
    "is_student" : True,
}
print(Student["semester"])

# operators

x = 10
y = 5
print("Addition:", x + y)
print("Subtraction:", x - y)    
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)
print("Floor Division:", x // y)
# comparison operators
print("Is x equal to y?", x == y)
print("Is x not equal to y?", x != y)
print("Is x greater than y?", x > y)
print("Is x less than y?", x < y)
