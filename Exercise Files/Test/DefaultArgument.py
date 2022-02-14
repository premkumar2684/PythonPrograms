def testdefaultAgrument(default_arg=2): # here default value is 2 if there is no argument passed it will be used.
    print(default_arg)
 
def inmethod():
    innum = input("enter the number")
    print(innum)

testdefaultAgrument(4)   
inmethod()
