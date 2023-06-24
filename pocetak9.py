# class iterClass():
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
        
# myClass= iterClass()
# myIter  = iter(myClass)
# for x in myIter:
#     print(x)


# class mySolution():
#     def __init__(self,a) -> None:
#         self.a = a
#     def solve(self):
#         maxi =  0
#         for i in range(1,int(self.a/2) + 1):
#             if self.a % i == 0 and maxi < i:
#                 maxi = i
#         return maxi
    
# p1 = mySolution(500)
# print(p1.solve())

# def sumOfDigits(n):
#     suma = 0
#     for i in str(n):
#         suma += int(i)
#     return suma
# def mySolution(testList):
#     newList = []
#     newList1 = []
#     testDict= {}
#     for i in testList:
#         testDict[str(sumOfDigits(i))] = i
#         newList.append(sumOfDigits(i))
#     newList.sort()
#     for i in newList:
#         newList1.append(testDict[str(i)])
#     return newList1
# print(mySolution([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))



# class mySolution():
#     def __init__(self,testList) -> None:
#         self.testList = testList
#     def Solve(self):
#         pass
# class realySolve(mySolution):
#     def __init__(self, testList) -> None:
#         super().__init__(testList)
#     def Solve(self):
#         suma = 0
#         boolList = []
#         for i in range(len(self.testList)):
#             for j in self.testList[i]:
#                 suma += j
#             if suma == 0:
#                 boolList.append(True)
#                 suma = 0
#             else:
#                 boolList.append(False)
#                 suma = 0
#         return boolList
    
# p1 = realySolve([[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]])
# print(p1.Solve())

        

# AEIOU => cgkqw
# def switch(a):
#     if(a == "a" or a == "A"):
#         a = 'c'
#     elif(a == 'e' or a == "E"):
#         a = 'g'
#     elif(a == 'i' or a == "I"):
#         a = 'k'
#     elif(a == 'o' or a == "O"):
#         a = 'q'
#     elif(a == 'u' or a == "U"):
#         a = 'w'
#     else:
#         return a
#     return a
# def mySolution(testStr):
#     newStr = ""
#     for i in testStr:
#         letter = switch(i)
#         if(letter.isupper()):
#             newStr += letter.lower()
#         else:
#             newStr += letter.upper()
#     return newStr
# print(mySolution("Python"))
        
numDict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four": 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" :9
}
# def getValue(testDict,a):
#     for x in testDict.keys():
#         if testDict[x] == a:
#             return x
# def mySolution(testStr):
#     testList = testStr.split(" ")
#     newList = []
#     for i in testList:
#         newList.append(numDict[i])
#     newList.sort()
#     testList.clear()
#     for i in set(newList):
#         testList.append(getValue(numDict,i))
#     return testList
# print(mySolution("six one four one two three"))

# class mySolution():
#     def __init__(self,testStr) -> None:
#         self.testStr = testStr
#     def Solve(self):
#         newList = [*set(self.testStr.lower())]
#         return newList
# p1 = mySolution("HELLO")
# print(p1.Solve())
        
# def numOfConsonatns(a):
#     consNum = 0
#     for i in a:
#         if i.upper() not in ["A","E","I","O","U"]:
#             consNum += 1
#     return consNum
# def test(testStr,k):
#     newList = []
#     for i in testStr.split(" "):
#         if numOfConsonatns(i) == k:
#             newList.append(i)
#     return newList
# print(test("This is our lovely home and don't forget that",3))
# def isPrime(a):
#     if a <= 0 or  a == 1:
#         return False
#     for i in range(2,int(a/2)):
#         if( a % i == 0):
#             return False
#     return True
# def test(testHex):
#     newList = []
#     for i in testHex:
#         newList.append(isPrime(int(i,16)))
#     return newList
# print(test("123ABCD"))















