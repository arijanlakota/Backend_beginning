# def newSolution(testStr,shifth):
#     newStr = ""
#     for i in testStr:
#         newStr += chr(ord(i) + shifth)
#     return newStr

# print(newSolution("Ascii character table",1))
    

# def mySolution(n):
#     newList = []
#     for i in range(1,n):
#         if "5" in str(i) and (i % 9 == 0 or i % 15 == 0):
#             newList.append([i,str(i).index("5")])
#     return newList
# print(mySolution(50))

# def helpFunction(helpStr):
#     helpList = []
#     for i in helpStr:
#         helpList.append(ord(i))
#     helpList.sort()
#     helpStr = ""
#     for i in helpList:
#         helpStr += chr(i)
#     return helpStr

# class ascOrder():
#     def __init__(self,testStr) -> None:
#         self.testStr = testStr
#     def Solve(self):
#         inputStr = self.testStr.split(" ")
#         newList = []
#         for i in inputStr:
#             newList.append(helpFunction(i)) 
#         return " ".join(newList)
                
        
# p1 = ascOrder("maltos won")
# print(p1.Solve())

# def bankSolution(bankList):
#     newList = []
#     for i in bankList:
#         balance = 0
#         for j in i:
#             balance += j
#             if balance < 0:
#                 newList.append(balance)
#                 break
#     return newList
# print(bankSolution([[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]))
          
# def mySolution(seperator,testArr):
#     return [x for x in str(seperator).join([str(i) for i in testArr])]
# print(mySolution(6,[12,-7,3,-89,14,88,-78,-1,2,7]))


# def findSolution(testArr):
#     for i in range(len(testArr)):
#         for j in range(len(testArr)):
#             if j == i:
#                 continue
#             for z in range(len(testArr)):
#                 if z == j or z == i:
#                     continue
#                 if testArr[i] + testArr[j] + testArr[z] == 0:
#                     return [i,j,z]
# print(findSolution([1, 2, 3, 4, 5, 6, -7]))


# def findSolution(testStr):
#     subStr = ""
#     for i in range(2,len(testStr)):
#         if testStr[i - 2].lower() not in ["a","e","i","o","u"] and testStr[i].lower() not in ["a","e","i","o","u"] and testStr[i - 1] in ["a","e","i","o","u"]:
#             subStr += testStr[i - 2] + testStr[i-1] + testStr[i]
#             break
#     return subStr
# print(findSolution("Sandwhich"))


# def builtString(testDict):
#     newStr = ""
#     for i in testDict.keys():
#         for j in range(testDict[i]):
#             newStr += i
#             newStr += " "
#     return newStr

# print(builtString({'f': 1, 'o': 2}))
            
# class myOrder():
#     def __init__(self,testArr) -> None:
#         self.testArr = testArr
#     def Solve(self):
#         if (self.testArr[0] + self.testArr[len(self.testArr) - 1]) % 2:
#             newList = sorted(self.testArr)
#         else:
#             newList = sorted(self.testArr, reverse=True)
#         return newList
# p1 = myOrder([2,7,4])
# print(p1.Solve())


def isPrime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

# def mySolution(testList):
#     max = -1000000
#     for i in range(len(testList)):
#         if max < testList[i] and isPrime(testList[i]):
#             max = testList[i]
#     return [testList.index(max),sum([int(i) for i in str(max).split(" ")])]
# print(mySolution([3, 7, 4]))


# def GPA(gpaList):
#     newList = []
#     for i in gpaList:
#         if i < 1.4:
#             newList.append("F")
#         elif i < 1.7:
#             newList.append("C-")
#         elif i < 2.0:
#             newList.append("C")
#         elif i < 2.4:
#             newList.append("C+")
#         elif i < 2.7:
#             newList.append("B-")
#         elif i < 3.0:
#             newList.append("B")
#         elif i < 3.4:
#             newList.append("B+")
#         elif i < 3.7:
#             newList.append("A-")
#         elif i < 4.0:
#             newList.append("A")
#         else:
#             newList.append("A+")
#     return newList
# print(GPA([5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]))

# def findIt(findList):
#     negList = [i  for i in findList if i < 0]
#     posList = [i  for i in findList if i > 0]
#     if posList == []:
#         posList.append(0)
#     if negList == []:
#         negList.append(0)
#     return [max(negList),min(posList)]
# print(findIt([]))

# from math import ceil
# def mySolution(testArr):
#     newList = []
#     squareSum = 0
#     for i in testArr:
#         squareSum += ceil(i) ** 2
#         newList.append(squareSum)
#     return newList
# print(mySolution([2.6, 3.5, 6.7, 2.3, 5.6]))

# def mySolution(a,b):
#     suma = 0
#     for i in range(min(a,b),max(a,b)):
#         suma += i
#     return bin(round(suma / (max(a,b) - min(a,b))))
# print(mySolution(4,7))

# def findIt(testArr):
#     newList = []
#     count = 0
#     for i in testArr:
#         if list(str(i)) == sorted(list(str(i))):
#             for j in str(i):
#                 if int(j) % 2 == 0:
#                     count = 1
#             if count == 0:
#                 newList.append(i)
#         count = 0

#     return newList

# print(findIt([11, 31, 40, 68, 77, 93, 48, 1, 57]))
# def mySolution(testArr):
#     for i in range(1,len(testArr)):
#         if testArr[i - 1] == testArr[i]:
#             return [i-1,i]
#     return None
        
# print(mySolution("Unhappy"))

# def mySolution(testList):
#     return sorted(testList)

# print(mySolution([11, 31, 40, 68, 77, 93, 48, 1, 57]))

# def mySolution(testStr):
#     newStr = ""
#     newList = []
#     for i in testStr:
#         for j in i:
#             if j.lower() in ["a","e","i","o","u"] or (j == "y" and i.index(j) == len(i) - 1):
#                 newStr += j
#         newList.append(newStr)
#         newStr = ""
#     return newList

# print(mySolution(['ably', 'abruptly', 'abecedary', 'apparently', 'acknowledgedly']))

# def mySolution(testStr):
#     newStr = ""
#     for i in range(1,len(testStr)):
#         if testStr[i - 1] == "[" and testStr[i] == "]":
#             newStr += "[]"
#         else:
#             newStr = ''
#     return "[" + newStr + ']'
# print(mySolution("]][][[]]]"))

# def mySolution(evenNum,oddNum):
#     newStr = "2"*evenNum + "3"*oddNum
#     return newStr
# print(mySolution(2,7))

# def Prime3(a):
#     for i in range(2,a):
#         for j in range(2,a):
#             for z in range(2,a):
#                 if(isPrime(i) and isPrime(j) and isPrime(z)):
#                     if i*j*z == a:
#                         return [i,j,z]
#     return []
# lista = []
# for i in range(2,50):
#     if Prime3(i) != []:
#         lista.append(Prime3(i))
# print(lista)

# def findIt(n):
#     newList = []
#     for i in range(10**(n - 1),10**n - 1):
#         if str(i)[0] == "2" or str(i)[len(str(i))-1] == "2":
#             newList.append(i)
#     return newList


# print(findIt(2))


# def findPalindrom(testStr):
#     if len(testStr) % 2 == 0:
#         beg = testStr[:int(len(testStr)/2)]
#         end = "".join(reversed(list(beg)))
#         testStr = beg + end
#     else:
#         beg = testStr[:int(len(testStr)/2)]
#         end = "".join(reversed(list(beg)))
#         testStr = beg + end
#     return testStr
# print(findPalindrom("cat"))

