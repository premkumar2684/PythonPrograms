def smallest():
    lst = [2,3,4,6,2,1,7]
    cars =['prem','list']
    cars.sort()
    print(cars)
    lstsort= []
    lst.sort()
    print(lst)
    
    smallest =1
    #if lst[0]>1:
     #   print(smallest)
    for i in range(len(lst)):
        if lst[i]==smallest:
            smallest+=1
    print(smallest)    
smallest()

def smallestnumber():
    n= int(input("enter how many numbers"))
    ln=[]
    
    for i in range(0,n):
        element=int(input("Enter the element"))
        ln.append(element)
    #print(ln)
    print(min(ln))
#smallestnumber()    
