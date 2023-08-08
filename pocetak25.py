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
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3],[13, 15, 17]]
def checkSubset(input_list1, input_list2): 
    return all(map(input_list1.__contains__, input_list2))
