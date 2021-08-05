# Prime number : A number which only divisible by 1 and itself

number_1 = int(input("Enter the 1st number : "))
number_2 = int(input("Enter the 2nd number : "))

# # % = Remainder
print("Remainder is "  +str(number_1 % number_2))

# # 7 : 1 - 7  => 2 3 4 5 6
# # 5 : 1 - 5 => 2 3 4
# # for varible_name in range 5

# Write a program to check whether a number is Prime or not
number = int(input("Enter a number : "))

flag = True
for x in range(2,number):
    if(number % x == 0):
        flag = False
if(flag):
    print("Prime Number")
else:
    print("Not a Prime Number")

for z in range(5):
    print(z , end = '')


# Write a program to print pattern
# * * * * *

# * * * * *

# * * * * *

# * * * * *

# * * * * *

for x in range(5):
    for y in range(5):
        print("* " , end='')
    print("\n")


# *

# * *

# * * *

# * * * *

for x in range(5):
    for y in range(x):
        print("* " , end='')
    print("\n")