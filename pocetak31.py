#list advanced
#1
# testList = [*range(10,81,10)]
# def reverseAt(funcList,num1,num2):
#     return funcList[:num1] + [*reversed(funcList[num1:num2+1])] + funcList[num2+1:]
# print(testList)
# print(reverseAt(testList,2,4))
#2
# def findLength(funcList):
#     countList = list()
#     count = 1
#     for i in range(1,len(funcList)):
#         if funcList[i-1] < funcList[i]:
#             count+=1
#         else:
#             countList.append(count)
#             count = 1
#     return max(countList)
# print(findLength([-1,-2,-3,-4,-5,-11,-12,-13]))
#3
# testList = [1, 2, 3, 4]
# from itertools import permutations
# def allPermutations(funcList):
#     n = len(funcList)
#     return [list(i) for i in permutations(funcList,n)]
# print(allPermutations(testList))
#4
# def findSmallest(funcList,k):
#     return sorted(funcList)[k-1]
# print(findSmallest([1, 2, 4, 3, 5, 4, 6, 9, 2, 1],9))
#5
# def findSmallest(funcList,k):
#     return sorted(funcList,reverse=True)[k-1]
# print(findSmallest([1, 2, 4, 3, 5, 4, 6, 9, 2, 1],9))
#6
# def isPalindrome(funcList):
#     n = len(funcList)
#     if all(funcList[i] == funcList[n-1-i] for i in range(n)):
#         return True
#     return False
# print(isPalindrome(['Red', 'Green', 'Red']))
#7
# def myFunction(list1,list2):
#     return {'intersection':set(list1).intersection(set(list2)),
#             'union': set(list1).union(set(list2))
#             }
# print(myFunction([1,2,3,4,5],[3,4,5,6,7,8]))
#8
# def perserveOrder(funcList):
#     newList = list()
#     for i in funcList:
#         if i not in newList:
#             newList.append(i)
#         else:
#             continue
#     return newList
# print(perserveOrder([1,2,4,3,5,4,6,9,2,1]))
#9
# def maxFindSub_sequence(funcList):
#     subSequence = list()
#     newList = []
#     for i in funcList:
#         if i >= 0:
#             newList.append(i)
#         else:
#             subSequence.append(sum(newList))
#             newList.clear()
#     subSequence.append(sum(newList))
#     return max(subSequence)
# print(maxFindSub_sequence([1, 2, 3]))
#10
# def maxFindSub_sequence(funcList):
#     subSequence = []
#     newList = []
#     for i in funcList:
#         if i <= 0:
#             newList.append(i)
#         else:
#             subSequence.append(newList)
#             print(subSequence)
#             newList.clear()
#     subSequence.append(newList)
#     # return min(subSequence,key=lambda x:sum(x))
# maxFindSub_sequence([2, 4, -3, -5, -4, 6, 9, 2])
#11
# def findCommon(list1,list2):
#     subSequence = []
#     newList = []
#     for i,j in enumerate(list1):
#         try (list2[i] != 10000):
#             if list2[i] == j:
#                 newList.append(j)
#             else:
#                 subSequence.append(newList)
#                 newList.clear()
#         except IndexError:
#             continue
#     subSequence.append(newList)
#     return max(subSequence,key=lambda x:len(x))
# print(findCommon([1, 2, 3, 4, 5, 6, 7, 8],[6, 7, 5, 6, 7, 8]))
#12
# def findNonRepeted(funcList):
#     for i in funcList:
#         if funcList.count(i) == 1:
#             return i       
# print(findNonRepeted([1, 2, 3, 1, 2, 4, 5, 6, 7, 8]))
#13
# from collections import OrderedDict
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         else:
#             self.cache.move_to_end(key)
#             return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         self.cache[key] = value
#         self.cache.move_to_end(key)
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)
#14
# def mySort(funcList,key):
#     return sorted(funcList,key=lambda x:x[key])
# print(mySort())
#15
# def findPairs(funcList,value):
#     newList = []
#     for i in range(len(funcList)):
#         for j in range(len(funcList)):
#             if i == j:
#                 continue
#             if funcList[i] + funcList[j] == value:
#                 if [*reversed([funcList[i],funcList[j]])] not in newList:
#                     newList.append([funcList[i],funcList[j]])
#     return newList
# print(findPairs([1,2,3,4,5,6,7,8,9],10))
            









            


