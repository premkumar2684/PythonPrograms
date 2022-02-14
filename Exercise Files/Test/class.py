from typing import final


class person:
    
    def __init__(self,name):
        self.name=name
          
            
    def sayhi(self):
        print("Hi "+self.name)  
    def sayhiwithID(self):
        print("Hi"+self.name+"with"+self.ID)
class normalperson(person):
   def sayhi(self):
        return super().sayhi()

p = person('prem')
p.sayhi()      

np = normalperson('test')
np.sayhi() 

#multiple inheritance
class A():
    def Amethod():
        print("print A")
class B():
    def Amethod():
        print("print B")
class c(A,B):
    pass
         