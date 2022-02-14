class A:
    def __init__(self):
        print('A')
        

class B(A):
    def __init__(self):
        print('B')
        super().__init__()

class X:
    def __init__(self):
        print('X')
        

class Forward(B, X):
    def __init__(self):
        print('Forward')
        super().__init__()

class Backward(X, B):
    def __init__(self):
        print('Backward')
        super().__init__()

bw= Backward()    
fw=Forward()    