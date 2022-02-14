def nonrepeating():
    str ="premlpremk"
    dct = {}
    lst = []
    for i in str:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
            lst.append(i)
    print(dct)
    print(lst)
    for i in lst:
        if dct[i] == 1:
            return i
    return None 

print(nonrepeating())


