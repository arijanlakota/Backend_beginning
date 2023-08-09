# 72 newList = []
# testlist = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# for i in testlist:
#     if type(i) == list:
#         newList.extend(i)
#     else:
#         newList.append(i)
# print(newList)
#73
# testList = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# print(list(set(testList)))
#74
# from collections import Counter
# testList = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# newList = []
# print(Counter(testList))
# for i,j in Counter(testList).items():
#     if j > 1:
#         newList.append([i]*j)
#     else:
#         newList.append(i)
# print(newList)
#75
# from collections import Counter
# testList = [1, 1, 2, 3, 4, 4.3, 5, 1]
# def listCounter(funcList):
#     resultList = []
#     for i in range(len(funcList)):
#         num = funcList[i]
#         count = 0
#         for j in range(i,len(funcList)):
#             if num == funcList[j]:
#                 count += 1
#             else:
#                 resultList.append([count,num])
#                 break
#     return resultList
# print(listCounter(testList))
#76
# def listCounter(funcList):
#     resultList = []
#     for i in range(len(funcList)):
#         num = funcList[i]
#         count = 0
#         for j in range(i,len(funcList)):
#             if num == funcList[j]:
#                 count += 1
#             else:
#                 if count == 1:
                    #resultList.append(num)
#                 resultList.append([count,num])
#                 break
#     return resultList
#77
# testList = [[2, 1], 2, 3, [2, 4], 5, 1]
# def decode(funcList):
#     resultList = []
#     for i in testList:
#         if type(i) == list:
#             resultList.extend([i[1]] * i[0])
#         else:
#             resultList.append(i)
#     return resultList
# print(decode(testList))
#78
# testList = [1, 1, 2, 3, 4, 4, 5, 1]
# def mySplit(funcList,firstPartLen):
#     return (funcList[:firstPartLen],funcList[firstPartLen:])
# print(mySplit(testList,3))
#79
# testList = [1, 1, 2, 3, 4, 4, 5, 1]
# testList.pop(2)
# print(testList)
#80
# testList = [1, 1, 2, 3, 4, 4, 5, 1]
# testList.insert(2,12)
# print(testList)
#81
# import random
# testList = [1, 1, 2, 3, 4, 4, 5, 1]
# print(random.choices(k=3,population=testList))
#82
# from itertools import combinations
# testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(*combinations(testList,2))
#83
# testList = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# newList = [round(i) for i in testList]
# print(sum(newList) * len(newList))
#84
# testList = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# print(min(testList,key=lambda x:round(x)))
# print(max(testList,key=lambda x:round(x)))
# print(*sorted([round(i)*5 for i in list(set(testList))]))
#85
# from numpy import zeros
# testList = zeros((2,2),dtype=int)
# print(testList)
#86
# nums = []
# for i in range(3):
#     nums.append([])
#     for j in range(1, 4):
#         nums[i].append(j)
#87
# def createMatrix(lenRows,lenColumn):
#     resultMatrix = []
#     for i in range(lenRows):
#         resultMatrix.append([])
#         for j in range(lenColumn):
#             resultMatrix[i].append(int(input()))
#     return resultMatrix
# def sumOfColumns(funcMatrix):
#     count = 0
#     for i in range(len(funcMatrix)):
#         for j in range(len(funcMatrix[i])):
#             count += funcMatrix[j][i]
#         yield count
#         count = 0
# print(*sumOfColumns(createMatrix(2,2)))
#88
# size = int(input("size of matrix: "))
# matrix = [[0]*size for i in range(size)]
# for i in range(len(matrix)):
#     lines = list(map(int,input().split()))
#     for j in range(len(matrix[i])):
#         matrix[i][j] = lines[j]
# suma = 0
# for i in range(size):
#     for j in range(size):
#         if i == j:
#             suma += matrix[i][j]
# print(suma)
#89
# list1 = [[1, 3], [5, 7], [9, 11]]
# list2 = [[2, 4], [6, 8], [10, 12, 14]]
# for i,j in zip(list1,list2):
#     i.extend(j)
# print(list1) 
#90
# list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# print(len(list1))   
#91
# def findIt(funcList):
#     return min(funcList,key=lambda x : len(x)),max(funcList,key=lambda x:len(x))
# print(findIt([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))
#92
# list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# list2 = [[1, 3],[13, 15, 17]]
# def checkSubset(input_list1, input_list2): 
#     return all(map(input_list1.__contains__, input_list2))
#93
# def countSublist(funcList,el):
#     count = 0 
#     for i in funcList:
#         if el in i:
#             count += 1
#     return count
# print(countSublist([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1))
#94
# from collections import Counter
# list1 = [1,2,3,4,4]
# testList = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# print(dict(Counter(map(str,testList))))
#95
# testList = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# print(sorted(testList,key=lambda x:len(x)))
#96?
#97
# a = range(13,18)
# newList = []
# testList = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# for i in testList:
#     if len(set(i) - set(a)) > 0:
#         continue
#     newList.append(i)
# print(newList)
#98
# import random
# testList = ['Python', 'list', 'exercises', 'practice', 'solution']
# def myFunc(x):
#      a = list(x)
#      random.shuffle(a)
#      return "".join(a)
# print([i for i in map(myFunc,testList)])
#99
# testList = ['Python', 3, 2, 4, 5, 'version']
# def myFunc(funcList):
#     newList =[]
#     for i in funcList:
#         if type(i) == str:
#             continue
#         newList.append(i)
#     return min(newList),max(newList)
# print(myFunc(testList))
#100
# list1 = [[1, 1, 3, 4, 5, 6, 7],
# [0, 1, 2, 3, 4, 5, 7],
# [0, 1, 2, 3, 4, 5, 7]]
# class listSolution():
#     def __init__(self,testList) -> None:
#         self.testList = testList
#     def Solve(self):
#         newList = []
#         a = len(self.testList)
#         b = len(self.testList[0])
#         for i in range(max(a,b)):
#             for j in range(min(a,b)):
#                 newList.append(self.testList[j][i]) 
#             if len(set(newList)) == 1:
#                 yield (newList[0])
#             newList.clear()

# p1 = listSolution(list1)
# print(*p1.Solve())
#101
# testList = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# print(sorted(testList,key=lambda x:sum(x)))
#102
# testList = ['Python', 'list', 'exercises', 'practice', 'solution']
# newList = []
# n = 8
# for i in testList:
#     if len(i) == n:
#         newList.append(i)
# print(newList) 
#103
# from collections import Counter
# testlist = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# print([key for key,value in Counter(testlist).items() if value > 1])
#104
# import numpy as np
# testList = [1, 1, 3, 4, 4, 5, 6, 7]
# # newArray = np.asarray(testList)
# # print(np.diff(newArray))
# newList = []
# for i in range(1,len(testList)):
#     newList.append(testList[i] - testList[i-1])
# print(newList)
#105
# def findAvg(l1,l2):
#     return sum(l1 + l2) / len(l1 + l2)
# print(findAvg([1, 1, 3, 4, 4, 5, 6, 7],[0, 1, 2, 3, 4, 4, 5, 7, 8])) 
#106
# mixedList = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# print(len([i for i in mixedList if isinstance(i,int)]))
#107
# columNum = 2
# testList = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# for i in testList:
#     i.pop(columNum-1)
# print(testList)
#108
# testList = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# columnNum = 2
# newList = []
# for i in testList:
#     newList.append(i[columnNum-1])
# print(newList)
#109
# def myShifth(funcList,shifth,direction):
#     if direction == "left":
#         return funcList[shifth:] + funcList[:shifth]
#     elif direction == "right":
#         return funcList[:-shifth+1:-1] + funcList[:-shifth+1]
# print(myShifth([*range(1,11)],3,'right'))
#110
# from collections import Counter
# def getValue(myDict,myValue):
#     for i,j in myDict.items():
#         if j==myValue:
#             return i
# testList = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# print(getValue(Counter(testList),max(Counter(testList).values())))
#111
# myList = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# indexList = [0, 3, 5, 7, 10]
# newList = []
# for i in indexList:
#     newList.append(myList[i])
# print(newList)
#112
# testList = [1, 2, 0, 6, 8, 10, 12, 14, 16, 17]
# if testList == sorted(testList):
#     print(True)
# else:
#     print(False)
#113
# from itertools import groupby
# myDict = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
# print([dict(e) for e in {tuple(d.items()) for d in myDict}])
#114
# testList = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# n = 0
# newList = []
# for i in testList:
#     newList.append(i[n])
# print(newList)
#115
# from collections import Counter
# testList = [2, 4, 6, 8, 10, 12, 14]
# if all(x == 1 for x in Counter(testList).values()):
#     print("yes")
# else:
#     print('no')
#116
# n = 0
# testList = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# print(sorted(testList,key=lambda x:x[n]))
#117
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [2,4,6,8]
# for i in list1:
#     if i in list2:
#         list1.remove(i)
# print(list1)
#118
# testList = [2,4,6,8]
# newList = [testList[i] - testList[i - 1] for i in range(1,len(testList))]
# print(newList) 
#119
# colorList =  ['red', 'black', 'white', 'green', 'orange']
# subStr = "ack"
# def findSub(funcList,subFuc):
#     for i in funcList:
#         if subFuc in i:
#             return True
#     return False
# print(findSub(colorList,subStr))
#120
# myList = ['red', 'black', 'white', 'green', 'orange']
# print(myList[::2])
#121
# checkList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# nestedList = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# def Check(cList,nList):
#     newList = []
#     for i in range(len(nList)):
#         newList.append([])
#         for j in nList[i]:
#             if j in cList:
#                 newList[i].append(j)
#     return newList
# print(Check(checkList,nestedList))
#122
# def common_in_nested_lists(nested_list):
#     result = list(set.intersection(*map(set, nested_list)))
#     return result
#123
# testList = ['Red', 'Green', 'Blue', 'White', 'Black']
# print([*map(lambda x:x[::-1],testList)])
#124
# testList = [(2, 7), (2, 6), (1, 8), (4, 9)]
# def checkList(funcList):
#     newList = [*map(lambda x:x[0]*x[1],funcList)]
#     yield max(newList),min(newList)
# print(*checkList(testList))
#125
# testList = [10, 20, 30, 40, 20, 50, 60, 40]
# count = 1
# for i in set(testList):
#     count *= i
# print(count)
#126
# list1 =  [1, 2, 3, 4, 5, 6, 7]
# list2 = [10, 20, 30, 40, 50, 60, 70]
# list3 = [100, 200, 300, 400, 500, 600, 700]
# newList = []
# for i,j,k in zip(list1,list2,list3):
#     newList.extend([i,j,k])
# print(newList)    
#127
# list1 = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
# charList = ['#', 'color', '@']
# newList = []
# for i in list1:
#     count = 0
#     for j in charList:
#         if j in i:
#             newList.append(i.removesuffix(j))
#             count = 1
#     if count == 0:
#         newList.append(i)
# print(newList)
#128
# downRange = 8
# upRange = 10
# testList = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12] 
# print(sum(testList[downRange:upRange+1]))
#129
# nestedList = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print(*map(lambda x:x[::-1],nestedList))
#130
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# list2 = [2, 2, 3, 1, 2, 6, 7, 9]
# list3 = [2, 1, 3, 1, 2, 6, 7, 9]
# count = 0
# for i,j,k in zip(list1,list2,list3):
#     if i == j == k:
#         count += 1
# print(count)
#131
# from collections import Counter
# testList = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
# def FindIt(funcList):
#     return list(Counter(funcList).keys()),list(Counter(funcList).values())
# print(FindIt(testList))
#132
# testList = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
# print(testList.index(max(testList)),testList.index(min(testList)))
#133
# def isSame(list1,list2):
#     testList = [i for i in list1 if i in list2]
#     return any(list1.index(x) == list2.index(x) for x in testList)
# l1 = ['red', 'green', 'black', 'orange']
# l2 = ['red', 'pink', 'green', 'white', 'black']
# l3 = ['white', 'orange', 'pink', 'black']
# print(isSame(l1,l2))
#134
# l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
# l2  = [1, 1, 2, 4, 5, 6]
# diffElemnts = set(l1).symmetric_difference(set(l2))
# print([e for e in l1 if e in diffElemnts])
#135
# def pairwise(l1):
#     temp = []
#     for i in range(len(l1) - 1):
#         current_element, next_element = l1[i], l1[i + 1]
#         x = (current_element, next_element)
#         temp.append(x)
#     return temp
#136
# strList = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
# print(list(set(strList)))
#137
# list1 = [1, 3, 5, 7, 4, 1, 6, 8]
# countE = 0
# countO = 0
# newList = []
# for i in list1:
#     if i % 2 and countO != 1:
#         countO = 1
#         newList.append(i)
#     elif countE != 1 and i % 2 == 0:
#         countE = 1
#         newList.append(i)
#     if len(newList) == 2:
#         print(newList)
#         break
#138
# myList = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# def mySort(funcList):
#     intList = [i for i in funcList if isinstance(i,int)]
#     strList = [i for i in funcList if isinstance(i,str)]
#     return sorted(intList) + sorted(strList)
# print(mySort(myList))
#139
# testList = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# print(sorted(testList,key=lambda x:int(x)))
#140
# testList = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# n = 1
# for i in testList:
#     i.pop(n-1)
# print(testList)

        