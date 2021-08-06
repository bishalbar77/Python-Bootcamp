'''
What are the disadvantages in using Python :-
1. Speed - Python is slower than C or C++.
2. Memory Consumption - Python is not a good choice for memory intensive tasks.
3. Runtime Errors - Error handling is not that great in Python
'''
# Floating Number :- Written with a decimal point dividing the integer
import random
marks = 10
divide = marks/3 # Decimal/Floating variable
print(divide)

for x in range(5):  # 0 1 2 3 4
    for y in range(x): # 0 1 2 3 4
        print("# " , end='')
    print("\n")  # Line break \n escape characters
for x in range(5):  # 0 1 2 3 4
    for y in range(5-x):  # 5 4 3 2 1
        print("# " , end='')
    print("\n")  # Line break \n escape characters

print("Manoj\tVasantarao")

def pattern1():
    for x in range(5):  # 0 1 2 3 4
        for y in range(x): # 0 1 2 3 4
            print("# " , end='')
        print("\n") 
    
def pattern2(): # Function defination
    for x in range(5):  # 0 1 2 3 4
        for y in range(5-x):  # 5 4 3 2 1
            print("# " , end='')
        print("\n") 

pattern1() # Function call
pattern2() # Function call

marks = 10
marks = 50 
marks = 450 
print(marks)

# Write a program to print pattern with random number of # on each line
def randomPattern():
    for x in range(10):  
        for y in range(random.randint(5,15)):  
            print("# " , end='')
        print("\n") 

randomPattern()