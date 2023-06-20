import math
def isPandigFirst(a):
    if("".join(sorted(list(str(a)[:9]))) == "123456789"):
        return True
def isPandigLast(a):
    if("".join(sorted(list(str(a)[-1:-10:-1]))) == "123456789"):
        return a
lista = []
# for i in range(1,10000000):
#     if(isPandigFirst(i) and isPandigLast):
#         print(i)
newlista = [x for x in range(1,100000) if isPandigFirst ]
print(newlista)


