class mainclass:
    __privateVariable = 2020
    __var=200
    def __privateMethod(self):
        print("I'm inside class mainclass that is this is private method")
    def insideclass(self):
        print("Private Variable: ",mainclass.__privateVariable)
        self.__privateMethod()
foo = mainclass()
foo.insideclass()
#print(foo.__privateVariable) #you can not use private members outside the class
#foo.__privateMethod()