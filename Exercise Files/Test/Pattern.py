rows=5
for i in range(rows+1):
    for j in range(i):
        print("*",end='')
    print('')
print("I am done")

for i in range(rows,0,-1):
    for j in range(i):
        print("*",end='')
    print('')
print("I am done too")

str = "premprem"
count =0
for i in str:
    if i=='p':
        count = count+1
print(count)    