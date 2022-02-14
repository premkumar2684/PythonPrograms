#
# Example file for working with classes
#


class simple():
    def sum(self,x,y):
        return (x+y)
class advance(simple):
    def inverse(self,x,y):
        sum= simple.sum(self,x,y)
        return(1/sum)

def main():
    a =simple()
    print(a.sum(10,20))
    c = advance()
    print(c.inverse(10,20))
   


if __name__ == "__main__":
    main()
        