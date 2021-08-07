def sum():
    result = 10 + 20
    print("Sum of 2 number is " + str(result))

def substract():
    result = 20 - 10
    print("Substract of 2 number is " + str(result))

def pattern1():
    for x in range(5):  # 0 1 2 3 4
        for y in range(x): # 0 1 2 3 4
            print("# " , end='')
        print("\n") 