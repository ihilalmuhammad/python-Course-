# function to add two numbers
def add_numbers(a, b):
    c = a + b
    print("addition result is:", c )
 
add_numbers(2,3)

# "Now let’s write a grade checker function."def grade_checker(grade):

def grade_checker(score):
    if score >= 90:
        return "Grade: A"
    elif score >= 80:
        return "Grade: B"
    elif score >= 70:
        return "Grade: C"
    elif score >= 60:
        return "Grade: D"
    else:
        return "Grade: F"

score = int(input("Enter your score: "))
print(grade_checker(score))