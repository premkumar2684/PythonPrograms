number = [0,1,2,3,4,5]
doublenumber= list(map(lambda x:x*2,number))
print(doublenumber)
evennumber = list(filter(lambda x:x%2==0,number))
print(evennumber)

def createmulti(a):
    return lambda x:x*a

double = createmulti(3)
print(double(2))