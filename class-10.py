# == :- if operator 1 is equal to operater 2
# != :- if operator 1 is not equal to operater 2

a = 20

if(a != 20):
    print("True")
else:
    print("False")

first = True
second = False

if(first and second):
    print("1st Line")
    
if(first or second):
    print("2nd Line")

# A = 1, 2 , 3
# B = 3, 4, 5
# A U B = 1 2 3 4 5
# A intersection B = 3

def function1():
    print("Hi")

# This function will print Hi since hello is not yet defined
function1()

def function1():
    print("Hello")

marks = 10
marks = 20
marks = 30
print(marks)
marks = 40
print(marks)