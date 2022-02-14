newtuple = ("soap", "knife", "handkerchief")
newitr = iter(newtuple)
#print(next(newitr))# printing using next method iterator(object)
#print(next(newitr))
#print(newitr.__next__()) # this is same above object.__next__()
for a in newitr:
    print(a)
newstr= "prem"
for a in newstr:
    print(a)
    