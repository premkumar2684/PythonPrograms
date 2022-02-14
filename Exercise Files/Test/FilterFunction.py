number = [0,1,2,3,4,5,6]
EvenList= []

for i in number:
    if(i%2==0):
        EvenList.append(i)

print(EvenList)   

def evenmethod(x):
    return x%2==0

EvenList2 =list(filter(evenmethod,number))  
print(EvenList2) 