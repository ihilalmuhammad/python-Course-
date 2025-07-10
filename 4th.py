#if elseif else conditional statements

answer = input("what is the capital of Pakistan? ")
if answer == "islamabad":
    print("correct")
else:
    print("incorrect")


# if elif else conditional statements

score = 0
q1 = input("1)what is 2+5? ")
if q1 == "7":
    print("correct")
    score += 1

q2 = input("2)what is the capital of turkey? ")
if q2 == "ankara":
    print("correct")
    score += 1

q3 = input("3)what is the capital of Pakistan? ")
if q3 == "islamabad":
    print("correct")
    score += 1  

print(f"your score is {score}/3")

# if elif else conditional statements of  calculator
num1 = int(input("enter first number: "))
operation = input("enter operation (+, -, *, /): ")
num2 = int(input("enter second number: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("invalid operation")

