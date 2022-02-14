# its way to combine map and filter functionality

number = [1,2,3,4,5,6]

doubledUsingMap = list(map(lambda x: x*2,number))
#even = list(filter(lambda x: x%2==0,number))

doubledUsingList = [x*2 for x in number]
#print(doubledUsingMap)
evenUsingList = [x for x in number if x%2==0]
print(doubledUsingList)
print(evenUsingList)

square = [i*i for i in range(1,10)]
print(square)