# def mySolution(testStr):
#     newList = []
#     subStr = ""
#     for i in range(2,len(testStr)):
#         subStr += testStr[i-2]
#         if testStr[i - 2] == ")" and testStr[i - 1] == " " and testStr[i] == "(":
#             newList.append(subStr)
#             subStr = ""
#     newList.append(subStr)
#     return [newList[i].strip() for i in range(len(newList))]
# print(mySolution("( ()) ((()()())) (()) ()"))


# def findPalindrome(testStr,a):
#     newPalindrom = (testStr + testStr[::-1])
#     if a > len(testStr):
#         if a % 2 == 0:
#             x = int(len(newPalindrom) / 2) - int((len(newPalindrom) - a)/2)
#             y = int(len(newPalindrom) / 2) + int((len(newPalindrom) - a)/2)
#             newPalindrom = newPalindrom.replace(newPalindrom[x:y],"")
#         else:
#             newPalindrom.replace(newPalindrom[int(len(newPalindrom) / 2)],"")
#             x = int(len(newPalindrom) / 2) - int((len(newPalindrom) - a)/2)
#             y = int(len(newPalindrom) / 2) + int((len(newPalindrom) - a)/2)
#             newPalindrom = newPalindrom.replace(newPalindrom[x:y],"")

#     return newPalindrom
# # print(findPalindrome("nestoa",9))
# def switch(a):
#     if a == 1:
#         return "one"
#     elif a == 2:
#         return "two"
#     elif a == 3:
#         return "three"
#     elif a == 4:
#         return "four"
#     elif a == 5:
#         return "five"
#     elif a == 6:
#         return "six"
#     elif a == 7:
#         return "seven"
#     elif a == 8:
#         return "eight"
#     elif a == 9:
#         return "nine"
# class mySolution():
#     def __init__(self,testArr) -> None:
#         self.testArr = testArr
#     def Solve(self):
#         newList = []
#         self.testArr.sort(reverse = True)
#         for i in self.testArr:
#             if len(str(i)) >= 2:
#                 continue
#             newList.append(switch(i))
#         return newList
    
# p1 = mySolution([27, 3, 8, 5, 1, 31])
# print(p1.Solve())
        

# def mySolution(testArr):
#     newList = []
#     x = 0
#     if len(testArr) % 2:
#         x = testArr[int(len(testArr) / 2)]
#         testArr.remove(x)
#     while len(testArr) != 0:
#         testArr.sort()
#         newList.append(testArr[0])
#         newList.append(testArr[len(testArr) - 1])
#         testArr.pop(0)
#         testArr.pop(len(testArr) - 1)
#     if x:
#         newList.append(x)
#     return newList
# print(mySolution([1, 2, 7, 3, 4, 5, 6]))
# def help(a):
#     count = 0
#     for i in a:
#         if i == "(":
#             count += 1
#         else:
#             break
#     return count

# class finalSolve():
#     def __init__(self,testStr) -> None:
#         self.testStr = testStr
#     def solve(self):
#         return [help(i) for i in self.testStr.split(" ")]
# p1 = finalSolve("(((((((()))))))) () (()) ((()()()))")
# print(p1.solve())
        

# def finalProblem(a):
#     return [a-6,2,2,2]
# print(finalProblem(100))