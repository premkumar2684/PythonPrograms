import array

a= array.array('i',[1,2,3,4])

a.append(6)
a.pop(4)
print(type(a))
for i in a:
    print(i)
b = array.array('i',[1,2])
print(b.typecode)
#for i in (b):
#    print(i)   

#two dimentional array
c = [[1,10],[2,12]]
for i in c:
    for j in i:
        print(j,end=" ")
    print()

d= [1,2]
d.append(3)
for i in d:
    print(i)    
