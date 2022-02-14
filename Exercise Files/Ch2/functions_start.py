#
# Example file for working with functions
#

# define a basic function


# function that takes arguments
#from _typeshed import ReadOnlyBuffer


def power(num,x=1):
    result = 1
    for i in range(x):
        result=result*num
    return result



# function that returns a value


# function with default value for an argument


#function with variable number of arguments

def mult_add(*args):
    result =0
    str="Prem"
    print(len(str))
    print(len(args))
    for i in args:
        if(i==12):
            continue
        result=result+i
    return result    


print(power(2))
print(power(2,3))
print(mult_add(2,3,12,5))



