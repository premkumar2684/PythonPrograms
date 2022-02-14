number = [1,2,3]
doubleNo= []

for i in number:
    doubleNo.append(i*2)

print(doubleNo)    

def double(x):
    return x*2

doubleList = list(map(double,number))
print(doubleList)

