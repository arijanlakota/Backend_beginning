#153
# n = 3
# testList = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
# def itOccurs(funcList,num,el):
#     count = 0
#     for i in funcList:
#         if i == el:
#             count += 1
#     if count >= num:
#         return True
#     return False
# print(itOccurs(testList,n,8))
#154
# list1 = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# list2  = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# for i in range(len(list1)):
#     list1[i].extend(list2[i])
# print(list1)
#155
# list1 = [2, 4, 7, 0, 5, 8]
# list2 = [3, 3, -1, 7]
# if len(list1) >= len(list2):
#     for i in range(len(list2)):
#         list1[i] += list2[i]
# else:
#     for i in range(len(list1)):
#         list2[i] += list1[i]
#156
# list1 = [2, 4, 7, 0, 5, 8]
# list2 = [3, 3, -1, 7]
# if len(list1) >= len(list2):
#     for i in range(len(list2)-1,0,-1):
#         list1[i] += list2[i]
# else:
#     for i in range(len(list1),0,-1):
#         list2[i] += list1[i]
# print(list1)
#157
# def conecateLists(*args):
#     newList = [*args]
#     newList = sorted(newList,key=lambda x:len(x))
#     resultList = []
#     for i in range(len(newList)):
#         for j in range(len(newList[0])):
#             try:
#                 resultList.append(newList[j][i])
#             except IndexError:
#                 continue
#     return resultList
# print(conecateLists([2, 4, 7, 0, 5, 8],[2, 5, 8],[0, 1],[3, 3, -1, 7]))
#158
# testList = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
# print(max(map(lambda x:x[1],testList)),min(map(lambda x:x[1],testList)))
#159
# list1 = [12,3]
# def addValues(funcList,val,times):
#     for i in range(times):
#         funcList.append(val)
#     return funcList
# print(addValues([[1,2,4]],[1,3,5],6))
#160
# testList = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
# count= 0
# n = 4
# newList = []
# for i in testList:
#     if count <= n:
#         if i % 2 == 0:
#             count +=1
#             continue
#         else:
#             newList.append(i)
#     else:
#         newList.append(i)
# print(newList)
#161
# def chech_is_increasing(funcList):
#     count = 0
#     for i in range(1,len(funcList)):
#         if funcList[i-1] > funcList[i]:
#             remember = i 
#             count +=1
#             break
#     funcList.pop(remember)
#     count = 1
#     for i in range(1,len(funcList)):
#         if funcList[i-1] > funcList[i]:
#             count += 1
#             break
#     if count < 2:
#         return True
#     return False
# print(chech_is_increasing([1, 2, 3, 0, 4, 5, 6]))
#162
# import re
# charList = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# print([*re.finditer('w',''.join(charList))][-1].span()[0])
#163
# numList = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
# n =73
# for i in range(len(numList)):
#     if numList[i]>80:
#         print(i)
#         break
#165
# def split_list(lst, n):
#     result = list((lst[i:i+n] for i in range(0, len(lst), n)))
#     return result
#166
# testList = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# print([i for i in testList if i != None])
#167
# testList = ['Red', 'Maroon', 'Yellow', 'Olive']
# newList = []
# for i in testList:
#     newList.append([*i])
# print(newList)
#168
# testList = [[1, 2, 5], [4, 5, 8], [7, 3, 6]]
# for i in testList:
#     print(i)
#169
# newList = list()
# testList = ['red', 'white', 'a', 'b', 'black', 'f']
# for i in testList:
#     newList.extend([*i])
# print(newList)
#170
# testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# count = 0
# n = 2
# ourRange = int(len(testList) / n)
# for i in range(ourRange):
#     testList.insert(n+count,'a')
#     count += n+1
# print(testList)
#171
# l1 = ['0', '1', '2', '3', '4']
# l2 = ['red', 'green', 'black', 'blue', 'white']
# l3 = ['100', '200', '300', '400', '500']
# newList = []
# for i,j,k in zip(l1,l2,l3):
#     newList.append(''.join([i,j,k]))
# print(newList)
#172
# testList = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# num = 3
# for i in range(num):
#     testList.pop()
# print(testList)
#173
# testList =  ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# class mySolution():
#     def __init__(self,li,hi,funcList) -> None:
#         self.li = li
#         self.hi = hi
#         self.funcList = funcList
#     def Solve(self):
#         newList = list()
#         for i in range(self.li):
#             newList.append(self.funcList[i])
#         newList.append(''.join(self.funcList[self.li:self.hi]))
#         for i in range(self.hi,len(self.funcList)):
#              newList.append(self.funcList[i])
#         return newList
# p1 = mySolution(2,4,testList)
# print(p1.Solve())
#174
# def addNums(testList,num):
#     return [i + num for i in testList]
# print(addNums([3, 8, 9, 4, 5, 0, 5, 0, 3],3))
#175
# testList = [(2, 3), (2, 4), (0, 6), (7, 1)]
# class mySolution():
#     def __init__(self,funcList) -> None:
#         self.funcList = funcList
#     def Solve(self):
#         pass
# class myChild(mySolution):
#     def __init__(self, funcList) -> None:
#         super().__init__(funcList)
#     def Solve(self):
#         n1 = [*map(lambda x:x[0],self.funcList)]
#         n2 = [*map(lambda x:x[1],self.funcList)]
#         return [max(n1),max(n2)],[min(n1),min(n2)]
# p1 = myChild(testList)
# print(p1.Solve())
#176
# def dividing_two_lists(l1,l2):
#     result = [x/y for x, y in zip(l1,l2)]
#     return result 
# nums1 = [7,2,3,4,9,2,3]
# nums2 = [9,8,2,3,3,1,2]
#177
# testList = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
# testList = [*map(set,testList)]
# print(testList[0].intersection(*testList))
#178
# ?
#179
#TO DO
# testList = [3, 40, 41, 43, 74, 9]
# testList = sorted(testList,key=lambda x:int(str(x)[0]),reverse=True)
# print(testList)
# def findThem(funcList):
#     resultList = list()
#     newList = list()
#     for i in range(1,len(funcList)):
#         if str(funcList[i-1])[0] == str(funcList[i])[0]:
#             newList.append(i-1)
#             newList.append(i)
#     return list(set(newList))[0],list(set(newList))[-1]
# myRange = findThem(testList)
# finalList = testList[:myRange[0]] + sorted(testList[myRange[0]:myRange[-1]+1],reverse=True) + testList[myRange[-1]+1:]
# print(''.join(map(str,finalList)))
#180
# def create_largest_number(lst):
#     if all(val == 0 for val in lst):
#         return '0'
#     result = ''.join(sorted((str(val) for val in lst), reverse=False,
#                       key=lambda i: i*( len(str(min(lst))) * 2 // len(i))))
#     return result
#181
# myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# class myCicle():
#     def __init__(self,funcList,cycleNum) -> None:
#         self.funcList = funcList
#         self.cycleNum = cycleNum
#     def Solve(self):
#         return [self.funcList[(self.cycleNum + i) % len(self.funcList)] for i in range(len(self.funcList))]
# p1 = myCicle(myList,3)
# print(p1.Solve())
#182
# testList = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# print(sorted(testList,key=lambda x:sum(x))[0],sorted(testList,key=lambda x:sum(x))[-1])
#183



        


            


        
            
        








    



