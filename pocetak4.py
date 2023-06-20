def isBouncy(a):
    newArg1 = int(''.join(sorted(list(str(a)))))
    newArg2 = int(''.join(sorted(list(str(a))))[::-1])
    if(a == newArg1 or a == newArg2):
        return False
    else:
        return True
# def bouncyProportion(b):
#     bouncyNum = 0
#     for i in range(1,b+1):
#         if(isBouncy(i)):
#             bouncyNum += 1
#     return (bouncyNum / b) * 100
bouncyNum = 0
for i in range(100,10000000):
    if(isBouncy(i)):
        bouncyNum += 1
    if(bouncyNum == i*99 / 100):
        print(i)
        break
    
    

    
        
        
