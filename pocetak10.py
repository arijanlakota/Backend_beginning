# def isPalindrome(a):
#     newList = []
#     for i in range(1,a):
#         if(str(i) == ''.join(reversed(str(i))) and i%2 == 0):
#             newList.append(i)
#     return newList
# print(isPalindrome(50))


# def mySolution(testList):
#     newList = []
#     minValue = 100000000
#     minIndex = 100000000
#     for i in range(len(testList)):
#         if(testList[i]%2 == 0 and minValue>testList[i] and minIndex > i):
#             minValue = testList[i]
#             minIndex = i
#     if(minValue == 100000000 and minIndex == 100000000):
#         return newList
#     newList.append(minValue)
#     newList.append(minIndex)
#     return newList

# print(mySolution([1, 9, 4, 6, 10, 11, 14, 8]))



# import mymodule
# mymodule.drzavaDuradiNesto("aksdmak")



# import platform
# x = dir(platform)
# print(x)


# def myFilter(a):
#     suma = int(str(a)[:2])
#     for i in str(a)[2:]:
#         suma += int(i)
#     if(suma > 0):
#         return a
# for i in [1, 7, -4, 4, -9, 2]:
#     print(myFilter(i))
# import json
# x = json.loads("""
#                {
#     "fruit": "Apple",
#     "size": "Large",
#     "color": "Red"
# }""")
# print(x["color"])

class mySolution():
    def __init__(self,testList) -> None:
        self.testList = testList
    def Solve(self):
        newList = []
        for i in range(1,len(self.testList)):
            if(self.testList[i - 1] > self.testList[i]):
                newList.append(i - 1)
                newList.append(i)
        return newList
class childClass(mySolution):
    def __init__(self, testList) -> None:
        super().__init__(testList)
p1 = childClass([-3, -2, -3, 0, 2, 3, 4])
print(p1.Solve())


        



