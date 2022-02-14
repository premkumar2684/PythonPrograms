from collections import defaultdict
#dict = {1:"prem",2:"Jash"}
#print(dict[3])

def defaultvalue():
    return "not present"

d = defaultdict(defaultvalue)
d[1] = "prem"
d[2] = "Jash"
print(d[3])
def str():
    return "test"
dct = defaultdict(str)
dct[1] = "prem"
print(dct[2])

