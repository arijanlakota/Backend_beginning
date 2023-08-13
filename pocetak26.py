#141
# myList = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
# print([i for i in myList if len(i)])
#142
# nestedList = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# n = 1
# suma = 0
# for i in range(len(nestedList)):
#     suma += nestedList[i][n-1]
# print(suma)
#143
# from collections import Counter
# testList = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# for i in testList:
#     print(dict(Counter(i)))
#144
# n = 1
# testList = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
# for i in range(len(testList)):
#     print(testList[i][n-1])
#145
# from random import choice
# exceptList = [2,9,10]
# print(choice(list(set(range(1,10)) - set(exceptList))))
#146
# testsList = [10, 2, 56]
# def sumDigits(funcList):
#     suma = 0
#     for i in ''.join(map(str,funcList)):
#         suma += int(i)
#     return suma
# print(sumDigits(testsList))
#147
# from random import shuffle
# list1 = [1, 2, 7, 8, 3, 7]
# list2 =  [4, 3, 8, 9, 4, 3, 8, 9]
# def randomCombine(l1,l2):
#     combinedList = l1 + l2
#     shuffle(combinedList)
#     return combinedList
# print(randomCombine(list1,list2))
#148
# colorList = ['red', 'green', 'blue', 'white', 'black', 'orange']
# exceptList = ['white','orange']
# print([i for i in colorList if i not in exceptList])
#149
# from itertools import permutations
# colorList = ['orange', 'red', 'green', 'blue']
# for i in range(len(colorList)):
#     print(*permutations(colorList,i))
#150
# list_to_reverse = [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]
# print(list_to_reverse[::-1])
#151

# testList = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
# print((max(testList[3:9]),min(testList[3:9])))
#152
# import heapq
# list1 = [1, 3, 5, 7, 9, 11]
# list2 = [0, 2, 4, 6, 8, 10]
# combinedList = list1+list2
# print(list(heapq.merge(list1,list2)))
#153




    