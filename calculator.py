user = input("What calc do you want to do?\n Choices: \n - Addition\n - Subtraction\n - Multiplication\n - Division\n")


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

x = int(input("First number: "))
y = int(input("Second number: "))

match user:
    case "Addition" | "addition":
        print(add(x,y))
    case "Subtraction" | "subtraction":
        print(subtract(x,y))
    case "Multiplication" | "multiplication":
        print(multiply(x,y))
    case "Division" | "division":
        print(divide(x,y))
    case _:
        print("Not a valid choice")
