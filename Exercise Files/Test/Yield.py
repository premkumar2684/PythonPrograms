def genfun():
    yield 1
    yield 2
    yield "prem"
def returnfun():
    return 1
    return 2
for value in genfun():
    print(value)   

print(returnfun())   