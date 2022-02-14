def ndigit(number):
    if (number>=1000):
        print(4)
    elif (number>=100):
        print(3)
    elif (number>=10):
        print(2)
    else:
        print(1)
def ternary(x,y):
    max=x if (x>y) else y
    print(max)
def otherway(x,y):
    max=y
    if (x>y):
        max=x
    print(max)
if __name__ == "__main__":
    #ndigit(1999)
    ternary(9,2)
    otherway(2,9)     