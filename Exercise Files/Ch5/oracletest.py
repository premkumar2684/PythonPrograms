

dct = {"walking":50,"Aerobics":90,"Zumba":38,"Running":60}
outdct= {}
#lst =[]
#for i in dct:
#    lst.append(dct[i])
#lst.sort()
#max=max(lst)
sortedvalue = sorted(dct.values())
max=max(sortedvalue)

for i in dct:
   if dct[i]==max:
        print(dct[i])
        print(i)
        outdct[i]=dct[i]
#dct.popitem()
print(outdct)
print(dct)
