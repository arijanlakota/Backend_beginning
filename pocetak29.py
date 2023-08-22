#220
# def crateDict(funcList,f):
#     resultDict = dict()
#     resultList = [*map(f,funcList)]
#     for i in range(len(resultList)):
#         resultDict[funcList[i]] = resultList[i]
#     return resultDict
# print(crateDict([1, 2, 3], lambda x: x * x))
#221
# import random
# testList = [1, 2, 3, 4, 5, 6]
# random.shuffle(testList)
# print(testList)
#222
def getKey(myValue,myDict):
    for i,j in myDict.items():
        if j == myValue:
            return i
# def difference_by(a, b, fn):
#   _b = set(map(fn, b))
#   return [item for item in a if fn(item) not in _b]
#223
# testList = [1, 2, 2, 3, 4, 4, 5]
# print(list(set(testList)))
#224
# from collections import Counter
# def filter_unique(lst):
#   return [item for item, count in Counter(lst).items() if count > 1] 
# print(filter_unique([1, 2, 2, 3, 4, 4, 5]))
#225
# users = {
#   'freddy': {
#     'name': {
#       'first': 'Fateh',
#       'last': 'Harwood' 
#     },
#     'postIds': [1, 2, 3]
#   }
# }
# testList = ['freddy', 'name', 'last']
# for i in testList:
#     value = users[i]
#226
# from math import floor
# def mySolution(a,b,f):
#     newList1 = [*map(f,a)]
#     newList2 = [*map(f,b)]
#     return [e for e in newList1 if e in newList2]
# print(mySolution([2.1, 1.2], [2.3, 3.4],floor))
#227
# class mySolution():
#     def __init__(self,a,b,f) -> None:
#         self.a = a
#         self.b = b
#         self.f = f
#     def Solve(self):
#         newList = self.a + self.b
#         newDict  = dict(zip(newList,[*map(self.f,newList)]))
#         resultList = [i for i in set([*map(self.f,self.a)]).symmetric_difference(set([*map(self.f,self.a)]))]
#         finalList = [getKey(i,newDict) for i in resultList]
#         return resultList
# from math import floor
# p1 = mySolution([2.1, 1.2], [2.3, 3.4], floor)
# print(p1.Solve())
#228
# def union_by_el(x, y, fn):
#   _x = set(map(fn, x))
#   return list(set(x + [item for item in y if fn(item) not in _x])) 
#229
# def checking(testList,testFunc):
#     for i in testList:
#         if testFunc(i):
#             return i
# print(checking([1, 2, 3, 4], lambda n: n % 2 == 1))
#230
# def find_index_of_all(lst, fn):
#   return [i for i, x in enumerate(lst) if fn(x)]
#231
# def mySolution(filterList,filterFunc):
#     l1 = [x for x, flag in zip(filterList, filterFunc) if flag]
#     l2 = [x for x, flag in zip(filterList, filterFunc) if not flag]
#     return [l1,l2]
# print(mySolution(['red', 'green', 'blue', 'pink'], [True, True, False, True]))
#232
# from math import ceil
# def chunk_list(lst, size):
#   return list(
#     map(lambda x: lst[x * size:x * size + size],
#       list(range(ceil(len(lst) / size)))))
#233
# from math import ceil
# def chunk_list_into_n(nums, n):
#   size = ceil(len(nums) / n)
#   return list(
#     map(lambda x: nums[x * size:x * size + size],
#     list(range(n)))
#234
# def digitize(n):
#   return list(map(int, str(n)))
# print(int('123'))
#235
# def find_last_index(lst, fn):
#   return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))
#236
# def filterOut(testList):
#     check1 = testList[0] % 2
#     check2 = len(testList) % 2
#     if check1 and check2:
#         return [i for i in testList if not i % 2]
#     else:
#         return [i for i in testList if i % 2]
# print(filterOut([1, 2, 3, 4, 5, 6, 7]))
#237
# def mySolution(dictList,specKey):
#     return [i[specKey] for i in dictList]
# simpsons = [
#   { 'name': 'Areeba', 'age': 8 },
#   { 'name': 'Zachariah', 'age': 36 },
#   { 'name': 'Caspar', 'age': 34 },
#   { 'name': 'Presley', 'age': 10 }
# ]
# print(mySolution(simpsons,"age"))
#238
# class mySolution():
#     def __init__(self,testList,fn) -> None:
#         self.testList = testList
#         self.fn = fn
#     def Solve(self):
#         newList = list(map(self.fn,self.testList))
#         return sum(newList) / len(newList)
# p1 = mySolution([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }],lambda x:x['n'])
# print(p1.Solve())
#239
# def find(lst, fn):
#   return next(x for x in lst if fn(x)) 
#240
# def find_last(lst, fn):
#   return next(x for x in lst[::-1] if fn(x))
#241
# def findCounter(testList):
#     newDict = dict()
#     for i in testList:
#         if i not in newDict.keys():
#             newDict[i] = testList.count(i)
#     return newDict
# print(findCounter(['a', 'b', 'f', 'a', 'c', 'e', 'a', 'a', 'b', 'e', 'f']))
#242
# def dif_with_duplicates(a,b):
#     symDif = set(a).symmetric_difference(set(b))
#     newList = a + b
#     resultList = list()
#     for i in symDif:
#         for _ in range(newList.count(i)):
#             resultList.append(i)
#     return resultList
# print(dif_with_duplicates([10, 20, 30], [10, 20, 40]))
    
