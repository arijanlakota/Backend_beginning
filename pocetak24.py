#1 list exercises
# myList = [1,2,3,4]
# print(sum(myList))
#2
# myList = [1,2,3,4]
# def multiply(a):
#     result = 1
#     for i in a:
#         result *= i
#     return result
# print(multiply(myList))
#3
# myList = [1,2,3,4]
# print(max(myList))
#4
# myList = [1,2,3,4]
# print(min(myList))
# 5 def check(testList):
#     count = 0
#     for i in testList:
#         if len(i)>=2 and  i[0] == i[-1]:
#             count += 1
#     return count
# print(check(['abc', 'xyz', 'aba', '1221']))
#6
# myList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(sorted(myList,key=lambda x:x[-1]))
# 7.myList = [1,1,3,4,4,2,2,6,4,1]
# print(list(set(myList)))
#8.
# myList = []
# if not(len(list)):
#     print("list is empty")
# else:
#     print("list is not empty")
#9
# myList = [1,2,3,4]
# myList2 = myList.copy()
# myList2.append(5)
# print(myList2,myList)
# 10 myList = ['2o2','213123','wqeqw','213','24123','dkjfksh']
# n = 3
# for i in myList:
#     if len(i) > n:
#         print(i)
#11
# def myFunc(list1,list2):
#     for i in list1:
#         if i in list2:
#             return True
#     return False
# print(myFunc([1,2,3],[4,5]))
#12
# colorList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# newList = []
# for i in range(len(colorList)):
#     if i == 0 or i == 4 or i == 5:
#         continue
#     else:
#         newList.append(colorList[i])
# print(newList)
#13
# import numpy as np
# arr = np.full((3,4,6),'*')
# print(arr)
#14
# myList = [1,2,3,4,5,6]
# print(len([i for i in myList if i %2 != 0]))
#15
# import random
# myList = [1,2,3,4]
# random.shuffle(myList)
# print(myList)
#16
# myList = [i**2 for i in range(1,31)]
# print(myList[:5],myList[-5:])
#17
# def isPrime(a):
#     if a <=1:
#         return False
#     for i in range(2,int(a/2)):
#         if a % i == 0:
#             return False
#     return True
# def allPrime(testList):
#     for i in testList:
#         if not isPrime(i):
#             return False
#     return True
# print(allPrime([2,2,5,7]))
#18
# from itertools import permutations
# myList = [1,2,3,4]
# print([i for i in permutations(myList)])
#19
# myList = [1,2,3,4]
# myList2 = [0,1,2,3]
# for i,j in zip(myList,myList2):
#     print(i - j)
#20
# for i,j in enumerate([1,2,3,4]):
#     print(i,j)
#21
# list_of_chars = ['a','b','c']
# print("".join(list_of_chars))
#22
# myList = [1,2,3,4,5,6]
# specifiedItem = 5
# print(myList.index(specifiedItem))
#23
# shallowList = [[2,6,1],[3,4,5],[2,5]]
# newList = []
# for i in shallowList:
#     for j in i:
#         newList.append(j)
#24
# list1 = [1,2,3,4]
# list2 = [5,6,7]
# print(list1+list2)
#25
# import random
# myList = [1,2,3,4,5]
# print(random.choice(myList))
#26
# myList = [1,2,3,4]
# listA = [10,10,0,0,10]
# listB = [10,10,10,0,0]
# def shifht(list1,shifthNum):
#     newList = []
#     for i in range(len(list1)):
#         newList.append(list1[i - shifthNum])
#     return newList
# def check(testList,testList2):
#     for i in range(len(testList)):
#         if shifht(testList,i) == testList2:
#             return True
#     return False
# print(check(listA,listB))
#27
# myList = [1,2,3,4]
# myList.remove(min(myList))
# print(min(myList))
#28
# myList = [1,2,3,4]
# myList.remove(max(myList))
# print(max(myList))
#29
# myList = [1,1,2,3,4,5,6,6,4,3]
# for i,j in enumerate(map(lambda x:myList.count(x),myList)):
#     if j == 1:
#         print(myList[i])
#30
# myList = [1,1,2,3,4,5,6,6,4,3]
# for i in set(myList):
#     print(i,myList.count(i))
# #31
# myList = [10,20,30,40,50,60,70,77,754,12,0,32,55]
# for i in myList:
#     if i > 21 and i < 56:
#         print(i)
#32
# myList = [1,2,3,[3,4],2,5,5]
# def check(testList):
#     for i in testList:
#         if type(i) == list:
#             return True
#     return False
# print(check(myList))
#33
# from itertools import combinations
# myList = [1,2,3,4]
# for i in range(len(myList)):
#     print([j for j in combinations(myList,i)])
#34
# def Eratosten(a):
#     testList = [i for i in range(2,a)]
#     for i in range(len(testList) + 1):
#         for j in range(i+1,len(testList)):
#             if testList[j] % testList[i] == 0:
#                 testList.remove(testList[j])
#     return testList
# print(Eratosten(90))
#35
# n = 5
# myList = ['p','q']
# newList = []
# for i in range(1,n+1):
#     for j in myList:
#         newList.append(j + str(i))
# print(newList)
#36
# x = 100
# print(format(id(x),'x'))
#37
# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# print(set(list1).intersection(set(list2)))
#38
# def shifht(list1,shifthNum):
#     newList = []
#     for i in range(len(list1)):
#         newList.append(list1[i - shifthNum])
#     return newList
# print(shifth(myList,1))
#39
# integerList = [11,33,50]
# print(''.join([str(i) for i in integerList]))
#40
# newList = []
# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
# from itertools import groupby
# from operator import itemgetter
# for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
#     print(letter)
#     for word in words:
#         print(word)
#41
# obj = {}
# for i in range(1, 21):
#     obj[str(i)] = []
# print(obj)
#42
# list1 = ['a','b','c','d','e']
# list2 = ['c','d','e','f','g']
# print(set(list1) - set(list2))
# print(set(list2) - set(list1))
#43
# myList = [1,2,3,4]
# a,b,c,d = myList
# print(a,b,c,d)
#44
# l = [[5*i + j for j in range(1,6)] for i in range(5)]
#45
# pair1 = (1,2)
# pair2 = (3,4)
#46
# myList = [1,2,3,4,5]
# for i in myList:
#     if i  % 2:
#         print(i)
#47
# myList = [1,2,3,4]
# newList = []
# for i in myList:
#     newList.append('*')
#     newList.append(i)
# print(newList)
#48
# nestedList = [[1,2],[2,3],[5,6],[1,0],[9,7]]
# for i in nestedList:
#     print(i,end="\n")
#49
# list1 = ["Black", "Red", "Maroon", "Yellow"] 
# list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# newList = []
# for i,j in zip(list1,list2):
#     newList.append({'colorName':i,"colorCode":j})
# print(newList)
#50
# myList = [{'key':{'subkey':1}},{'key':{'subkey':10}},{'key':{'subkey':5}},{'key':{'subkey':0}}]
# print(sorted(myList,key=lambda x:x['key']['subkey']))
#51
# myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# def list_slice(S, step):
#     return [myList[i::step] for i in range(step)]
# print(list_slice(myList,3))
#52
# list1 = ["red", "orange", "green", "blue", "white"]
# list2 = ["black", "yellow", "green", "blue"]
# print(set(list1) - set(list2))
# print(set(list2) - set(list1))
#53
# import itertools
# c = itertools.count()
#54
# list1 = [[1,2],[3,4,5],[6,7,8,9]]
# for i in list1:
#     list1[0].extend(i)
# print(list1[0])
#55
# myList = [{'key1':5,'key2':3},{'key1':10,'key2':7}]
# for i in myList:
#     del i['key1']
# print(myList)
#56
# someStr = "asdasdasddad"
# print(list(someStr))
#57
# def check(testList,testItem):
#     for i in testList:
#         if i != testItem:
#             return False
#     return True
# print(check(['blue','blue'],'blue'))
#58

# def myExtend(list1,list2):
#     list1.pop()
#     list1.extend(list2)
#     return list1
# print(myExtend([1,2,5,9,10],[5,6,6]))
#59
# myList = [1,2,3,4]
# n = 5
# try: 
#     print(myList[n])
# except IndexError:
#     print("the index does not exist")
#60
# x = [(4, 1), (1, 2), (6, 0)]
# print(min(x, key=lambda n: (n[1], -n[0])))
#61
# myList = list()
# for i in range(6):
#     myList.append({})
# print(myList)
#62
# [print(i,sep='  ',end="") for i in range(6)]
#63
# sampleList = [1,2,3,4]
# class mySolution():
#     def __init__(self,testList,testStr) -> None:
#         self.testStr = testStr
#         self.testList = testList
#     def Solve(self):
#         return [i for i in map(lambda x:self.testStr + str(x),self.testList)]
# p1 = mySolution(sampleList,'emp')
# print(p1.Solve())
#64
# list1 = [1,2,3,4]
# list2 = [-1,-2,-3,-4]
# for i,j in zip(list1,list2):
#     print(i,j)
#65
# testList = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# newList = [i for i in testList if i != 0
# newList.extend([0] * testList.count(0))
# print(newList)
#66
# nestedList = [[1,2,5],[6,0,7],[9,4,6,2,1],[2,3,54,6,4],[0,34,6,1,6,7]]
# print(sorted(nestedList,key=sum,reverse=True)[0])
#67
# def findValues(spec,funcList):
#     for i in funcList:
#         if i > spec:
#             yield i
# newGenerator = findValues(5,[2,3,6,8])
# print(*newGenerator)
#68
# x = [10, 20, 30]
# y = [40, 50, 60]
# x[:0] = y
# print(x)
#69
# newList = []
# nestedList =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# for i in nestedList:
#     if i not in newList:
#         newList.append(i)
# print(newList)
#70
# myList = ['aabcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# print([x for x in myList if x[0] == 'a'])
#71
# myList = [{},{1},{}]
# print(all(len(x) == 0 for x in myList))