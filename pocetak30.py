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
#256
# from itertools import combinations
# def myTuples(funcList):
#     resultList = list()
#     for i in range(len(funcList)):
#         resultList.extend(combinations(funcList,i))
#     resultList.append(tuple(funcList))
#     return resultList
# print(myTuples([1, 2, 3, 4]))
#257
# def isSame(test1,test2):
#     return all(x in test2 for x in test1) and all(x in test2 for x in test1)
# print(isSame([1, 2, 4],[2, 4, 1]))
#258
# def flatKeys(funcDict):
#     return funcDict.keys()
#259
# def check(funcList,fn):
#     return any(fn(x) for x in funcList)
#260
# def test_includes_all(nums, lsts):
#   for x in lsts:
#     if x not in nums:
#       return False
#261
# class mySolution():
#     def __init__(self,funcList) -> None:
#         self.funcList = funcList
#     def Solve(self):
#         return sorted(self.funcList,key=lambda x:self.funcList.count(x))[-1]
# p1 = mySolution([1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3])
# print(p1.Solve())
#262
# def myReshape(funcList,n):
#     return funcList[n:] + funcList[:n]
# print(myReshape([4, 5, 6, 7, 8, 1, 2, 3],2))
#263 ?
#264
# def create_two_dimensional(funcList):
#     a,b = len(funcList),len(funcList[0])
#     newList = []
#     result = []
#     for i in range(min(a,b)):
#         for j in range(max(a,b)):
#             newList.append(funcList[j][i])
#         result.append(tuple(newList))
#         newList.clear()
#     return result
# print(create_two_dimensional([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
#265
# def fibonachi(n):
#     generate = [0,1]
#     for i in range(1,n):
#         generate.append(generate[i-1] + generate[i])
#     return generate
# print(fibonachi(5))
#266
# def cast(myValue):
#     print(type(myValue))
#     print(list(myValue))
# cast({1: 'Red', 2: 'Green', 3: 'Black'})
#267
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr.cumsum())
# testList = [1, 2, 3, 4]
# newList = []
# resultList = []
# for i in range(len(testList)):
#     newList.append(testList[i])
#     resultList.append(sum(newList))
# print(resultList)
#268
# def myFunc(testList,n,side="left"):
#     if side == 'left':
#         return testList[n:]
#     elif side == 'right':
#         return testList[:n]
# print(myFunc([1,2,3,4,5,6],3,side='right'))
#269
# def every_nth(nums, nth):
#   return nums[nth - 1::nth]
#270
# def is_contained_in(l1, l2):
#   for x in set(l1):
#     if l1.count(x) > l2.count(x):
#       return False
#   return True
#271
# def ifDuplicate(funcList):
#     return all(funcList.count(x) > 1 for x in funcList)
#272
# def generateSequence(num1,num2):
#     return [i for i in range(num1,num2+1,num1)]
# print(generateSequence(5,25))
#273
# def divideList(funcList):
#     for i in range(1,len(funcList)-1):
#         if sum(funcList[:i]) == sum(funcList[i+1:]):
#             return funcList[i]
# print(divideList([-4, 0, 6, 1, 0, 2]))
#274
# testList = ["Red", "Green", "Blue", "White"]
# def countLower(funcList):
#     count = 0
#     for i in "".join(funcList):
#         if i.islower():
#             count += 1
#     return count
# print(countLower(testList))
#275
# def oddSum(testList):
#     newList = []
#     for i in testList:
#         newList.append(sum(testList) - i)
#     return newList
# print(oddSum([1,2,3]))
#276
# def largest_odd(testList):
#     return max(testList,key=lambda x: x % 2)
# print(largest_odd([0, 9, 2, 4, 5, 6]))
#277
# def gaps(testList):
#     testList.sort()
#     maxGap = max(abs(a-b) for a,b in zip(testList[:-1],testList[1:]))
#     minGap = min(abs(a-b) for a,b in zip(testList[:-1],testList[1:]))
#     print(maxGap,minGap)
# gaps([1, 2 ,9, 0, 4, 6])
#278
# def test(nums):
#     max_num = max(nums)
#     min_num = min(nums)
#     return (max_num+min_num)*(max_num-min_num+1)//2 - sum(nums)
#279
# def myFunc(testStr,specNum):
#     count = 0
#     newList = list()
#     for i in testStr:
#         if i.lower() in ['a','e','i','o','u']:
#             count += 1
#             newList.append(i)
#         if count == specNum:
#             return ''.join(newList)
#     return "n is less than number of vowels present in the string."
# print(myFunc("Python Exercises", 3))
#280
# newList = []
# nums = [1, 2, 3, 4, 5]
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if abs(nums[i] - nums[j]) == 3:
#             newList.append([nums[i],nums[j]])
# print(newList[::2])

    



    


