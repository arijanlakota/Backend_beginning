# f = open("demofile.txt","rt")
# print(f.read(5))
# f = open("demofile.txt", "r")
# for x in f:
#   print(x)
# f.close()

# f = open("demofile2.txt", "a")
# f.write("nesto novo")
# f.close()
# f = open("demofile2.txt","r")
# print(f.read())


# import os
# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("file does not exist")





# class mySolution():
#     def __init__(self,testArr) -> None:
#         self.testArr = testArr
#     def Solved(self):
#         newList = []
#         for i in self.testArr:
#             if(len(i) % 2 == 0):
#                 newList.append(i)
#         return newList
# class myNewSolution(mySolution):
#     def __init__(self, testArr) -> None:
#         super().__init__(testArr)
# p1 = myNewSolution(['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!'])
# print(p1.Solved())

# import re
# def mySolution(funcArr):
#     newList = []
#     for i in funcArr:
#         if re.findall('[^a-zA-Z]',i):
#             i = "".join(reversed(list(i)))
#             newList.append(i)
#         else:
#             i = i.swapcase()
#             newList.append(i)
#     return newList


# print(mySolution(['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']))

