from tkinter import W


str= "bangalore chennai hyd"
words = str.split(' ')
print(len(words))

def wordocc():
    dct= {}
    for i in str:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
    return dct   
output = [list(map(wordocc(),words))]
print(output)
     