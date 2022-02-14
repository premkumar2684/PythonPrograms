import re
dct ={}
str = "I am Prem and i am from karnataka"
strlower = str.casefold()
print(strlower)
words = re.split("\W",strlower)

print(words)
for i in words:
    if i in dct:
        dct[i]+=1
        dct.pop(i)
    else:
        dct[i]=1
print(dct)
print(dct.values())
itr =iter(dct)

for i in itr:
    print(i)
s=set(dct.keys())
print(s)      


print("----------------")

dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
print(dict)
temp = []
res = {}
for key, val in dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
print(temp)
print(res)        