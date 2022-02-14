def LargeSmall():
    lst =[]
    n= int(input('how many numbers'))
    for i in range(n):
        number = int(input('Enter the number:'))
        lst.append(number)
    print(max(lst))
    print(min(lst))
    lst.sort()
    print(lst) 
    
LargeSmall()