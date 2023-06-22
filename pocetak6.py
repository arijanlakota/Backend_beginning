# import cProfile
# import re
# def nesto(a):
#     return a + 1
# cProfile.run('re.compile("nesto")')
# 52.import sys
# sys.stderr.write("This is an error message \n")

# 53.import os
# # os.environ["API_USER"] = "username"
# USER = os.getenv('API_USER')
# print(os.environ)

# import getpass
# print(getpass.getuser())
# testList = [19, 19, 15, 5, 3, 5, 5, 2]
# def isWorking (n):
#     if(n.count(19) == 2 and n.count(5) >= 3):
#         return "ksdjaldj"
# print(isWorking(testList))

# def test(n):
#     if(len(n) == 8 and n.count(n[4]) == 3):
#         return True
#     return False
# print(test())


# def testNum(a):
#     if(a % 34 == 4 and a > 4**4):
#         return True
#     return False

# print(testNum(854))

# def testPiles(a):
#     return [a + 2*i for i in range(a)]

# print(testPiles(17))




# def test(a):
#     if(a[-1].find(a[-2]) + 1):
#         return True
#     return False

# print(test(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']))


# def test(a):
#     for i in range(100):
#         if(a[i+1] - a[i] != 10):
#             return False
#     return True

# print(test)




# def test(a):
#     suma = 0
#     for i in a:
#         suma += i
#     if(len(a) == suma):
#         return True
#     return False

# print(test([1,1,1,1]))


# def test(a):
#     s = ""
#     commaList = []
#     wordList = []
#     for i in range(len(a)):
#         if(not(a[i] == " " or a[i] == "," )):
#             s += a[i]
#         elif(i == len(a) - 1):
#             wordList.append(s)   
#         else:
#             commaList.append(a[i])
#             if(s != ""):
#                 wordList.append(s)
#             s = ""
#     finalList = [wordList,commaList]
#     return finalList

# print(test("W3resource Python, Exercises."))

# def test(m):
#     num = 0
#     numList = []
#     if(len(m) > 20):
#         k = 21
#     else:
#         k = len(m)
#     for i in range(len(m)):
#         if(m[i] not in numList):
#             numList.append(m[i])
#     if(len(numList) != 4):
#         return False
#     for i in range(1,k):
#         if(m[i] == m[i-1]):
#             return False
#     return True


# def finalTest(a,b):
#     lista = []
#     for i in range(len(a)):
#         if a[i] < b:
#             lista.append(i)
#     return lista

# print(finalTest([0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55],100))



