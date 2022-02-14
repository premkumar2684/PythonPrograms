# Namespace example

a=1 # a is global variable since it defined outside the method
c=10 # global varaible
def add_fun():
    b=1 # is local variable
    global a # in case if you want to use global variable which is "a" here, we need use this statement
    c=12 # local variable
    
    a=a+1
    b=b+1
    print(a)
    print(b)
    print(c) # this will print 12
add_fun()
print(c)    # this will print 10