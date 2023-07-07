# class mySolution():
#     def __init__(self,testArr) -> None:
#         self.testArr = testArr
#     def Solve(self):
#         product = 1
#         for i in self.testArr:
#             product *= i % 10
#         return product
# p1 = mySolution([12,13])
# print(p1.Solve())

# def newSolution(funcArr):
#     funcArr = set(funcArr)
#     return  sorted(list(funcArr))

# print(newSolution([1, 3, 4, 10, 4, 1, 43]))


# def helpFunction(funcNum):
#     if funcNum > 10 and str(funcNum)[0] in ["1", "3", "5", "7", "9"] and str(funcNum)[len(str(funcNum)) - 1] in ["1", "3", "5", "7", "9"]:
#         return True
#     return False
# newList = []
# for i in [1, 3, 79, 10, 4, 1, 39, 62]:
#     if helpFunction(i):
#         newList.append(i)
# print(newList)
import time
a = time.time()
# from math import log 
# def mySolution(a,n):
#     return log(n,a)
# print(mySolution(3,12900700781701026662481960358450703949334417416449930858101164413445974926422638))
# b = time.time()
# print(b - a)


# class mySolution():
#     def __init__(self,testArr) -> None:
#         self.testArr= testArr
#     def Solve(self):
#         negNum = 0
#         sumNum = 0
#         for i in self.testArr:
#             if(i < 0):
#                 negNum += 1
#             sumNum += abs(i)
#         if(negNum % 2):
#             return -sumNum
#         return sumNum
# p1 = mySolution([-25, -12, -23,23,53,213,5,-23,-42,-12433242,12,-12,-764,3,7,3,-23])
# print(p1.Solve())


# def simpleSolve(a,b):
#     if(max(a,b) % 2):
#         return(max(a,b) - 1)
#     return max(a,b)
# print(simpleSolve(47,53))
    
# import re
# def checkFile(funcArr):
#     x = [i for i in funcArr if(i[-4:] in [".txt",".exe",".jpg",".png",".dll"]) 
#          and i.count(",") == 0  and len(re.findall([0-9],i)) <= 3
#         ]
#     return x
# print(checkFile(['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']))
        
# print(-sum([10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]))


# def mySolution(funcDict):
#     keyList = funcDict.keys()
#     for i in range(1,len(keyList)-1):
#         if keyList[i - 1].islower() != keyList[i].islower() and keyList[i].islower() != keyList[i + 1].islower() :
#             target = keyList[i]
            # uncomplited
def isPrime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

# def mySolution(testStr):
#     testList = testStr.split(" ")
#     newStr = ""
#     for i in testList:
#         if isPrime(len(i)):
#             newStr += i
#             newStr += " "
#     return newStr
# print(mySolution("Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."))

# def mySolution(n,k):
#     r = str(n)
#     if(k > len(str(n))):
#         return str(n)[::-1]
#     for i in range(len(str(n))):
#         r.replace(str(n)[i - k],str(n)[i])
#     return r
# print(mySolution(12345,1))
        

# class mySolution():
#     def __init__(self,testArr) -> None:
#         self.testArr = testArr
#     def Solve(self):
#         difList = []
#         difDict = {}
#         dif = 1000000
#         for i in range(len(self.testArr)):
#             for j in range(len(self.testArr)):
#                 if j == i:
#                     continue
#                 if dif > abs(self.testArr[i] - self.testArr[j]):
#                     dif = abs(self.testArr[i] - self.testArr[j])
#                     difList.append(dif)
#                     difDict[str(dif)] = str([i,j])
#         return difDict[str(min(difList))]
# p1 = mySolution([1.1, 4.25, 0.79, 1.0, 4.23]) 
# print(p1.Solve())

                    


            
        


        
        
        

            





        


    
