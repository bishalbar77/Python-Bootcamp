# Arthematic operations with string
name = "RUTUJA"

print(name * 2)
print(name + str(3))

# Marks | Grade
# 90 > Excellent
# 70 > Very Good
# 40 > Good
# 40 < Fail

marks = int(input("Please enter your marks between 0 - 100 : "))

# Nested Looping
# User have passsed or not
if(marks < 40):
    print("You have failed")
# If user passed the exam so what grade should he/she get
else:
    if(marks > 90): 
        print("Your performance was Excellent!")
    elif(marks > 70):
        print("Your performance was Very Good!")
    else:
        print("Your performance was Good!")

# If else if ladder
if(marks > 90):
    print("Your performance was Excellent!")
elif(marks > 70):
    print("Your performance was Very Good!")
elif(marks > 40):
    print("Your performance was Good!")
else:
    print("You have Failed!")

# Looping statements
# Factorial :- The factorial of a number is the function that multiplies the number by every natural number below it.
# Factorial of 3 = 3 * 2 * 1
#              4 = 4 * 3 * 2 * 1
#              5 = 5 * 4 * 3 * 2 * 1
#              6 = 6 * 5 * 4 * 3 * 2 * 1

number = int(input("Enter a number : "))

factorial = 1
while(number > 1):
    factorial = factorial * number      # 1 * 5 * 4 * 3 * 2
    number = number - 1                 # 5 - 1 - 1 -1 -1 
print("Factorial of the number is " + str(factorial))