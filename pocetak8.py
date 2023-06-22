# class myClass():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = myClass("John",36)
# print(p1.name)
# print(p1.age)
        

# class mySolution():
#     def __init__(self,testArr) -> None:
#         self.testArr = testArr
#     def myFunc(self):
#         for i in self.testArr:
#             if("," in i):
#                 print(i.replace(",","."))
# p1 = mySolution(["101","102,2","104.4"])
# p1.myFunc()



# class mySol():
#     def __init__(self,testArr) -> None:
#         self.testArr = testArr
#     def myFunc(self):
#         return sum(self.testArr) / len(self.testArr)

# p1 = mySol([4, -5, 17, -9, 14, 108, -9])

# print(p1.myFunc())


def getValue(testDict,a):
    for x in testDict.keys():
        if(testDict[x] == a):
            return x




# def mySolution(testArr):
#     thisDict = {}
#     maxLen = 0
#     for i in testArr:
#         if(maxLen < len(set(i))):
#             maxLen = len(set(i))
#         thisDict[i] = len(set(i))
#     return getValue(thisDict,maxLen)
# print(mySolution(['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']))



# def mySolution(testArr):
#     listIn = []
#     for i in testArr:
#         if(i*(-1) in testArr):
#             listIn.append(testArr.index(i))
#     return listIn


# print(mySolution([1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]))



# class mySolution():
#     def __init__(self,testArr) -> None:
#         self.testArr = testArr
#     def myFunc(self):
#         suma = 0
#         maxLen = 0
#         testDict = {}
#         for i in self.testArr:
#             for j  in i:
#                 suma += len(j)
#             testDict[suma] = i
#             if(maxLen < suma):
#                 maxLen = suma
#             suma = 0
#         return testDict[maxLen]
    
# p1 = mySolution([['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']])
# print(p1.myFunc())
            



# def mySolution(testArr):
#     newList = []
#     for i in testArr:
#         newList.append((i - min(testArr))/(max(testArr) - min(testArr)))
#     return newList

# print(mySolution([18.5, 17.0, 18.0, 19.0, 18.0]))


# def mySolution(test):
#     newList = []
#     for i in range(len(test)):
#         if test[i] == "Y":continue
#         if(test[i].isupper and test[i] in ["A","E","I","O","U"] and i % 2 == 0) :
#             newList.append(i)
#     return newList



# print(mySolution("AEIOUYW"))


# class parentClass():
#     def __init__(self,name,age) -> None:
#         self.fname = name
#         self.old = age
#     def printname(self):
#         print(self.fname + " " + self.old)
# class childClass(parentClass):
#     def __init__(self, name, age,nesto) -> None:
#         super().__init__(name, age)
#         self.nestoDif = nesto
    

# p1 = childClass("ja","brate","nesto")
# p1.printname()
        

# def mySolution(testArr,k):
#     suma = 0
#     for i in range(k):
#         if len(str(testArr[i])) > 2:
#             suma += testArr[i]
#     return suma


# print(mySolution([114, 215, -117, 119, 14, 108, -9, 12, 76],5))


class parentClass():
    def __init__(self,testArr,k) -> None:
        self.testArr = testArr
        self.k = k
    def myFunc(self):
        suma = 0
        for i in range(self.k):
            if len(str(self.testArr[i])) > 2:
                suma += self.testArr[i]
        return suma
    
class childClass(parentClass):
    def __init__(self, testArr, k) -> None:
        super().__init__(testArr, k)
p1 = childClass([114, 215, -117, 119, 14, 108, -9, 12, 76],5)
print(p1.myFunc())

        
        

            


        

    