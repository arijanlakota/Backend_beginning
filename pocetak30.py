#243
# def myAll(fn,myList):
#     return all(fn(x) for x in myList)
# print(myAll(lambda x: x > 1,[4, 2, 3]))
#244
# def myRange(fNum,lNum,step):
#     if step == 1:
#         raise ValueError
#     return  [i for i in range(fNum,lNum+1,step)]
# print(myRange(1,6,2))
#245
# class mySolution():
#     def __init__(self,*args) -> None:
#         self.args = [*args]
#     def Solve(self):
#         m = ""
#         for i in self.args:
#             if len(i) > len(m):
#                 m = i
#         return m
# p1 = mySolution([1, 2, 3], [1, 2], [1, 2, 3, 4, 5])
# print(p1.Solve())
#246
# def check(myList,fn):
#     return any(map(fn,myList))
# print(check([0, 1, 2, 0], lambda x: x >= 2))
#247
# def mySolution(x,y):
#     _y = set(y)
#     return [item for item in x if item not in _y]
#248
# def myMax(myList,fn):
#     return max(map(fn,myList))
# print(myMax([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))
#249
# def myMax(myList,fn):
#     return min(map(fn,myList))
#250
# def myMax(myList,fn):
#     return sum(map(fn,myList))
#251
# def fillValue(myValue,myLen):
#     return [myValue] * myLen
# print(fillValue(0,7))
#252
# def mySort(funcList,n):
#     funcList = sorted(funcList,reverse=True)
#     return funcList[:n]
# print(mySort([-2, -3, -1, -2, -4, 0, -5],3))
#253
# def mySort(funcList,n):
#     funcList = sorted(funcList,reverse=False)
#     return funcList[:n]
# print(mySort([-2, -3, -1, -2, -4, 0, -5],3))
#254
# def calculateWeight(nums,weight):
#     sum_w = sum(weight)
#     sum_n = 0
#     for i,j in zip(nums,weight):
#         sum_n += i*j
#     return sum_n / sum_w
# print(calculateWeight([10, 50, 40],[2, 5, 3]))
#255
# newList = []
# def deepFlatten(funcList):
#     for i in funcList:
#         if isinstance(i,list):
#             deepFlatten(i)
#         else:
#             newList.append(i)
#     return newList
# print(deepFlatten([[[1, 2, 3], [4, 5]], 6]))
    


