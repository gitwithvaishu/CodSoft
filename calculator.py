def add(a,b):
    c=a+b
    return c

def subtarct(a,b):
    c=a-b
    return c

def multiply(a,b):
    c=a*b
    return c

def divide(a,b):
    if b==0:
        print("\nWe cannot divide the number by zero")
        b=int(input("\nAgain Enter the second number(b!=0):"))
        c=a/b
    else:
        c=a/b
    return c

print("Welcome to Calculator\n")
print("Please enter two numbers to perform operations. You can use these two numbers for all operations\n")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
while True:
    print("\nOperations:\n1.Addition\n2.Subtraction\n3.Multipplication\n4.Division\n5.Exit")
    choice=int(input("\nEnter your choice:"))
    match choice:
        case 1:
            print(f"\nThe addition of {a} and {b} is {add(a,b)} ")
        case 2:
            print(f"\nThe subtraction of {a} and {b} is {subtarct(a,b)} ")
        case 3:
            print(f"\nThe multiplication of {a} and {b} is {multiply(a,b)} ")
        case 4:
            print(f"\nThe diivsion of {a} and {b} is {divide(a,b)} ")
        case 5:
            exit()
        case _:
            print("\nInvalid choice")
