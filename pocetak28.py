#183
# testList = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# newList = list()
# for i in testList:
#     newList.extend(list(set(i)))
# print(list(set(newList)))
#184
# testList = ['Sum all the items in a list', 'Find the second smallest number in a list']
# myStr = " ".join(testList)
# newList = myStr.split(" ")
# myTuple = list()
# resultList = []
# for i in range(1,len(newList)):
#     myTuple.append(newList[i-1])
#     myTuple.append(newList[i])
#     resultList.append(tuple(myTuple))
#     myTuple.clear()
# print(len(resultList))
#185
# def binaryList(num):
#     return [int(i) for i in list(bin(num))[2:]]
# print(binaryList(8))
#186nums[6:10], nums[1:3] = nums[1:3], nums[6:10]
#187
# myList = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# print([*map(' '.join,myList)])
#188
# n = 1
# testList = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
# print(sorted(testList,key=lambda x:x[n-1]))
#189
# testList = [1, 2, 3, 4, 5, 6, 7]
# newList = [testList[-1]] + testList[1:-1] + [testList[0]]
# print(newList)
#190
# def myMultiply(l1,l2):
#     mulList = list()
#     for i in range(len(l1)):
#         for j in range(len(l2)):
#             mulList.append(l1[i]* l2[j])
#     return sorted(mulList,reverse=True)
# def maximumNums(f1,f2,num):
#     return myMultiply(f1,f2)[:num]
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [3, 6, 8, 9, 10, 6]
# print(maximumNums(list1,list2,4))
#191
# list1 = [2, 3, 5, 8, 7, 2, 3]
# list2 = [4, 3, 9, 0, 4, 3, 9]
# list3 = [2, 1, 5, 6, 5, 5, 4]
# def findMinimum(*args):
#     args = min([*map(min,list(args))])
#     return args
# print(findMinimum(list1,list2,list3))
#192
# testList = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
# def removeStr(funcTuple):
#     return tuple([i for i in funcTuple if isinstance(i,int)])
# print([*map(removeStr,testList)])
#193
# import numpy as np
# testList = [[1, 2], [2, 4]]
# newArr = np.array(testList)
# print(newArr.shape)
#194
# testList = [[1], [2, 4, 4], [1, 2], [4]]
# newNum = max([*map(lambda x:len(x),testList)])
# for i in testList:
#     while len(i) < newNum:
#         i.append(0)
# newList = []
# suma = 0
# for i in range(min(newNum,len(testList))):
#     for j in range(max(newNum,len(testList))):
#         suma += testList[j][i]
#     newList.append(suma)
#     suma = 0
# print(newList)
#195
# testList = ['red', 'green', 'white', 'black']
# for i,j in enumerate(testList):
#     print(len(testList)-i-1,testList[len(testList)-i-1])
#196
# sp_element = 'white'
# testList = ['red', 'green', 'white', 'black', 'orange']
# testList.remove(sp_element)
# testList.append(sp_element)
# print(testList)
#197
# n = 1
# testList = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# count = 0
# suma = 0
# newList = []
# while n <= max([*map(len,testList)]):
#     for i in testList:
#         try:
#             suma += i[n-1]
#             count += 1 
#         except IndexError:
#             continue
#     newList.append(suma/count)
#     suma = 0
#     count = 0
#     n += 1
# print(newList)
#198
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = [7, 8, 5, 2, 10, 12]
# indexList = []
# for i in l1:
#     if i in l2:
#         indexList.append(l1.index(i))
# print(indexList)
#199
# students =  [u'S001', u'S002', u'S003', u'S004']
# print([str(i) for i in students])
#200
# testList = [1, 2, 3, 4, 5, 6]
# newList = []
# for i in range(1,len(testList)):
#     newList.append([testList[i-1],testList[i]])
# print(newList)
#201
# myStr = "https://www.w3resource.net"
# checkList = ['.com', '.edu', '.tv']
# def mySolution(funcStr,check):
#     for i in check:
#         if i in funcStr:
#             return True
#     return False
# print(mySolution(myStr,checkList))
#202
# testList = [1, None, 5, 4, None, 0, None, None]
# print([i for i in range(len(testList)) if testList[i] == None])
#203
# testList = ['1', '2', '3', '4', '5', '6', '7', '8']
# newList = []
# for i in range(1,len(testList)):
#     newList.append(testList[i-1] + testList[i])
# print(newList)
#204
# testList = [1234, 122, 2984, 19372, 100] 
# temp = str(testList[0])[0]
# print(all(x[0] == temp for x in map(str,testList)))
#205
# testList = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
# print([i for i in range(len(testList)) if testList[i] > 3000])
#206
# testList = ['abc ', ' ', ' ', 'sdfds ', ' ', ' ', 'sdfds ', 'huy']
# print([i.strip() for i in testList])
#207
# l1 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# l2 = [('red', 'green'), ('orange', 'pink')]
# for i in l1:
#     if i in l2:
#         print(i)
#208
# testList = [1, 2, 3, 4, 5, 6, 7]
# newList = []
# for i in range(1,len(testList)):
#     newList.append((testList[i-1] + testList[i])/2)
# print(newList)
#209
# newList=resultList  = []
# counts = []
# count = 0
# testList = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
# for i in testList:
#     if i != 0:
#         count += 1
#     else:
#         if count == 0:
#             continue
#         counts.append(count)
#         count = 0
#         continue
# myCount = 0
# for j in testList:
#     if j != 0:
#         myCount+=1
#         newList.append(j)
#     if myCount == c:
#         resultList.append(newList)
#         newList.clear()
# print(resultList)
#210
# def test(lst):
#     result = []
#     ele_val = 0
#     for digit in lst:
#         if digit == 0:
#             if ele_val != 0:
#                 result.append(ele_val)
#                 ele_val = 0
#         else:
#             ele_val += digit 
#     if ele_val>0:
#         result.append(ele_val) 
#     return result
#211
# sp_elemet = 'Ricky Rivera'
# testList = ['Ricky Rivera', 98, 'Math', 90, 'Science']
# testList.remove(sp_elemet)
#212
# testList = [34.67, 12, -94.89, 'Python', 0, 'C#']
# print([i for i in testList if isinstance(i,int)])
#213
# testList = [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
# n = 2
# testList = sorted([i for i in testList if i < 0])[:n]
# print(sum(testList))
#214
# def myOrder(ord,num):
#     r = bool()
#     if ord == 'asd':
#         r = False
#     elif ord == 'dec':
#         r = True
#     return int("".join([*map(str,sorted([*map(int,list(str(num)))],reverse=r))]))
# print(myOrder("dec",134543))
#215
# def merge_lists(*args, fill_value = None):
#   max_length = max([len(lst) for lst in args])
#   result = []
#   for i in range(max_length):
#     result.append([
#       args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
#     ])
#216
# from collections import defaultdict
# def count_by(lst, fn = lambda x: x):
#   count = defaultdict(int)
#   for val in map(fn, lst):
#     count[val] += 1
#   return dict(count)
# from math import floor
#217
# def myFilter(funcList,fn = lambda x:x):
#     return [
#     [x for x in funcList if fn(x)],
#     [x for x in funcList if not fn(x)]
#   ]
# print(myFilter(['red', 'green', 'black', 'white'], lambda x: x[0] == 'w'))
#218
# l1 = ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
# l2 = [3, 2, 6, 4, 1, 5]
# newList = sorted([(i,j) for i,j in zip(l1,l2)],key=lambda x:x[1])
# resultList = [i[0] for i in newList]
# print(resultList)
#219
# def unfold(fn, seed):
#   def fn_generator(val):
#     while True: 
#       val = fn(val[1])
#       if val == False: break
#       yield val[0]
#   return [i for i in fn_generator([None, seed])]
# f = lambda n: False if n > 40 else [-n, n + 10]
# a lot to reconsider here
#220
