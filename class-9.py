'''
Local variable / Global variable
'''
# Global variable
result = 100

def multiplication():
    # Local variable
    result = 100 * 5
    # print(result)

def sum():
    # Local variable
    global result # there exist a global variable called as result
    result = 100 + 20
    
def substract():
    # Local variable
    result = 100 - 10
    # print(result)

# Combine all the function call under one function
def calculation():
    sum()
    multiplication()
    substract()

# Call the combined functions by one function
calculation()
print(result)