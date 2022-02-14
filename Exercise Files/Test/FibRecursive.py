n=10
def fibrecursive(num):
    if num<=1:
        return num
    else:
        return fibrecursive(num-1) + fibrecursive(num-2)


for i in range(n):
    print(fibrecursive(i))