
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

while(True):
    choice = input("Input your choice")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter the first number"))
        num2 = float(input("Enter the second number"))
        if choice=='1':
            print(add(num1,num2))
        elif choice=='2':
            print(subtract(num1,num2))  
        elif choice=='3':
            print(multiply(num1,num2))
        elif choice=='4':
            print(divide(num1,num2))      
           
    else:
        print("invalid input")
        break

