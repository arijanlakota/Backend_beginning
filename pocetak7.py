# def isPalindrome(testStr):
#     results = []
#     for i in range(len(testStr)):
#         if(testStr[i] == "".join(list(reversed(testStr[i])))):
#             results.append(True)
#         else:
#             results.append(False)
#     return results
# print(isPalindrome(['palindrome', 'madamimadam', '', 'foo', 'eyes']))


# def prefixStart(a):
#     pref,testList = a[0]
#     lista = []
#     for i in testList:
#         if i.startswith(pref):
#             lista.append(i)
#     return lista

# print(prefixStart([("do",('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]))



# def findLength(a):
#     results  = []
#     for i in a:
#         results.append(len(i))
#     return results
# print(findLength(['cat', 'car', 'fear', 'center']))


# def findLongest(a):
#     # lenStr = ""
#     # lenNum = 0
#     # for i in a:
#     #     if(lenNum < len(i)):
#     #         lenNum = len(i)
#     #         lenStr = i
#     # return lenStr

# print(findLongest(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']))

# def unEvenMatrix(a,target):
#     targetIndex = []
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             if a[i][j] == target:
#                 targetIndex.append([i,j])
#     return targetIndex
# print(unEvenMatrix([[1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]],19))




# def splitString(a):
#     stringList = []
#     if " " in a:
#         stringList = a.split(" ")
#     elif "," in a:
#         stringList = a.split(",")
#     else:
#         for i in range(len(a)):
#             if(i % 2 == 1):
#                 stringList.append(a[i])
#     return stringList

# print(splitString("abcd"))




# def whatHappening(a):
#     directGo = 0
#     if(a[0] == a[1]):
#         print("akskdjlkjasd")
#     elif(a[0] > a[1]):
#         directGo = 1
#     else:
#         directGo = 0
#     if directGo == 1:
#         for i in range(len(a) - 1):
#             if(a[i] <= a[i+1]):
#                 directGo = -1
#     elif directGo == 0:
#         for i in range(len(a) - 1):
#             if(a[i] >= a[i+1]):
#                 directGo = -1
#     if directGo==1:
#         print("decreasing")
#     elif directGo==0:
#         print("increasing")
#     else:
#         print("askldjalkdj")


# def isIsolated(a):
#     if(a[-2] == " "):
#         return True
#     return False

# for i in ["can t","cat","mon t","mot"]:
#     print(isIsolated(i))




# def asciiSum(a):
#     suma = 0
#     for i in a:
#         if(i.isupper()):
#             suma += ord(i)
#     return suma


# print(asciiSum("JavaScript"))




# def isDecreasing(a):
#     listDecrease = []
#     for i in range(1,len(a)):
#         if a[i] < a[i - 1]:
#             listDecrease.append(i)
#     return listDecrease


# print(isDecreasing([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]))


# def maxList(a):
#     newList = []
#     newList.append(a[0])
#     for i in range(1,len(a)):
#         if(a[i] > newList[i-1]):
#             newList.append(a[i])
#         else:
#             newList.append(newList[i-1])
#     return newList
# print(maxList([1, 19, 5, 15, 5, 25, 5]))



# def binart(a,b):
#     return bin(int(a,2)^int(b,2))
# print(binart('0001', '1011'))

    
    

