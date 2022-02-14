L1 = [1,"prem",'10000']

emp_list=[
    {'ID':0,"name":"prem"},
    {'ID':1,"name":"Jash"}
]
print(emp_list)
print(L1[0])
L1.append("Testing")
L1.append("Testing")
L1[0]=2
print(L1)

T1=(1,"Jash",10000)
#T1[0]=0
print(T1)
D1={
    'ID':1,"Name":"Jash","Salary":1000
    }
D1['dept']="Dev"
print(D1)
print(D1['ID'])
print(D1.get('ID'))