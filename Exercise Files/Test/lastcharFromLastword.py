#How to print last charaster from last element from list
l=['prem','Jash','teju']
lastword = l[len(l)-1]
lastchar=lastword[len(lastword)-1]
print(lastchar)
#Python program to Find the first non-repeating character from given string
str ="hello"
dct={}
for i in str:
    if i in dct:
        dct[i]+=1
    else:
        dct[i]=1
print(dct)
for i in dct:
    if dct[i]==1:
        print(i)
        break
    
