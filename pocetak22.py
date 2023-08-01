#72
# def removeSpecial(specChar,testStr):
#     return specChar * testStr.count(specChar)
# print(removeSpecial("g","google"))
#73
# def countChars(testStr):
#     resultDict = {"lowercase":0,"uppercase":0,"specialChars":0,"numericalVals":0}
#     for i in testStr:
#         if i.islower():
#             resultDict["lowercase"] += 1
#         elif i.isupper():
#             resultDict["uppercase"] += 1
#         elif i.isnumeric():
#             resultDict["numericalVals"] += 1
#         else:
#             resultDict["specialChars"] += 1
#     return resultDict
# print(countChars("Pthon@123EeEExercies#$"))
#74
# def containsAll(str1,str2):
#     for i in str1:
#         if i not in str2:
#             return False
#     return True
# class mySolution():
#     def __init__(self,testStr1,testStr2) -> None:
#         self.testStr1 = testStr1
#         self.testStr2 = testStr2
#     def Solve(self):
#         result = ""
#         index = 0
#         for i in range(len(self.testStr1)):
#             if self.testStr1[i] in self.testStr2:
#                 index = i
#                 break
#         for i in range(index,len(self.testStr1)):
#             if containsAll(self.testStr2,result):
#                 return result
#             else:
#                 result += self.testStr1[i]
#         return None
# p1 = mySolution("PRWSOERIUSFK","OSU")
# print(p1.Solve())
#75
# def getKey(myDict,myValue):
#     for i,j in myDict.items():
#         if j == myValue:
#             return i

# def containsAll(str1,str2):
#     for i in str1:
#         if i not in str2:
#             return False
#     return True
# def mySolution(testStr1):
#     thisDict = dict()
#     miniStr = ''.join(list(set(testStr1)))
#     result = ""
#     for i in range(0,len(testStr1)):
#         for j in range(i,len(testStr1)):
#             if containsAll(miniStr,result):
#                 thisDict[result] = len(result)
#                 result = ""
#             else:
#                 result += testStr1[j]
#         result = ''
#     return getKey(thisDict,min(thisDict.values()))
# print(mySolution("asdaewsqgtwwsa"))
#76
# def countSubStr(str1,k):
#     resultList = []
#     result = ""
#     for i in range(len(str1)):
#         for j in range(i,len(str1)):
#             if len(set(result)) == k:
#                 resultList.append(result)
#                 result = ""
#             else:
#                 result += str1[j] 
#         result = ""
#     return resultList
# print(countSubStr("asdjhfuuuudnekjwenasd13c",4))
#77
# from itertools import combinations
# def countSubStrings(str1):
#     resultList = []
#     for i in range(1,len(str1)):
#         resultList.append([j for j in combinations(str1,i)])
#     return resultList
# print(countSubStrings("abdeg"))
#78
# import string
# def countAlphabet(str1):
#     count = 0
#     for i in range(len(str1)):
#         if str1[i].lower() == string.ascii_lowercase[i]:
#             count += 1
#     return count
# print(countAlphabet("xbcefg"))
#79
# def getKey(myDict,myValue):
#     for  i,j in myDict.items():
#         if j == myValue:
#             return i
# def findMinAndMax(str1):
#     resultDict = {}
#     for i in str1.split(" "):
#         resultDict[i] = len(i)
#     return [getKey(resultDict,min(resultDict.values())),getKey(resultDict,max(resultDict.values()))]
# print(findMinAndMax("Write a Java program to sort an array of given integers using Quick sort Algorithm."))
#80
# from itertools import combinations
# def findAll(testStr):
#     result = 0
#     n = len(testStr)
#     for i in range(n):
#         for j in range(i,n):
#             if(testStr[i] == testStr[j]):
#                 result += 1 
#     return result
# print(findAll("abca"))
#81
# import re
# def findSub(str1,str2):
#     print(re.search(str1,str2).span()[0])
# findSub("sub","adsubu")
#82
# import textwrap
# print(textwrap.fill("The quick brown fox jumps over lazy dog",10))
#83
# print(bin(2)[2:],oct(10)[2:],hex(15)[2:])
#84
# testStr = "pYTHON eXERCISES"
# print(testStr.swapcase())
#85
# print(int(bytearray([111, 12, 45, 67, 109]),16))
#86
# class mySolution():
#     def __init__(self,testStr,specChar) -> None:
#         self.testStr = testStr
#         self.specChar = specChar
#     def Solve(self):
#         return self.testStr.replace(self.specChar,"")
# p1 = mySolution("Delete all occurrences of a specified character in a given string","a")
# print(p1.Solve())
#87
# def commonValues(str1,str2):
#     return "".join(list(set(str1).intersection(set(str2))))
# print(commonValues("Python3","Python2.7"))
#88
# def  myCheck(testStr):
#     capitalCheck = 0
#     lowerCheck = 0
#     minLength = 5
#     numCheck = 0
#     if len(testStr) < minLength:
#         return "Not valid string"
#     for i in testStr:
#         if i.isupper():
#             capitalCheck = 1
#         elif i.islower():
#             lowerCheck = 1
#         elif i.isnumeric():
#             numCheck = 1
#     if numCheck and lowerCheck and capitalCheck:
#         return "Valid string"
#     else:
#         return "Not valid string"
# print(myCheck("Wr3e"))
#89
# def removeUnwanted(testStr):
#     newStr = ""
#     for i in testStr:
#         if i.isalpha():
#             newStr += i 
#     return newStr
# print(removeUnwanted("Pyt!hon#Ex#$ercises"))
#90
# print(' '.join(list(set('Python Exercises Practice Solution Exercises'.split(" "))))) 
#91
# ourList = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# print(','.join([str(i) for i in ourList]))
#92
# import difflib
# def string_similarity(str1, str2):
#     result =  difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
#     return result.ratio()   
#93
# testStr = "red 12 black 45 green"
# for i in testStr.split(" "):
#     if i.isnumeric():
#         print(i)
#94
# def hex_to_rgb(hex):
#   return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)) 
#95
# def rgb_to_hex(rgb):
#     return "".join([str(hex(i)[2:].upper()) for i in rgb])
# print(rgb_to_hex((255, 165, 1)))
#96
# import camelcase
# print(camelcase.CamelCase("foobaa"))
#97
# from re import sub

# def camel_case(s):
#   s = sub(r"(_)+", " ", s).replace(" ", "")
#   return '_'.join(s)
# print("foo baa")
#98
# class mySolution():
#     def __init__(self,testStr) -> None:
#         self.testStr = testStr
#     def Solve(self):
#         return self.testStr[0].lower() + self.testStr[1:]
# p1 = mySolution("Python")
# print(p1.Solve())
#99
# testStr = """ This
# is a
# multiline 
# string."""
# print(testStr.splitlines())
#100
# def checkDuplicate(testStr):
#     for i in testStr.split(" "):
#         for j in i:
#             if i.count(j) > 1:
#                 return False
#     return True
# print(checkDuplicate("The wait is overe."))
#101
# def sumString(str1,str2):
#     if type(str1) == str:
#         print("Error in input")
#     if type(str2) == str:
#         print("Error in input")
#     return int(str1)+int(str2)
# print(sumString('5','4'))
#102
# testStr = "String! With. Punctuation?"
# newStr = str()
# for i in testStr:
#     if i.isalpha() or i == " ":
#         newStr += i
# print(newStr)
#103
# def replaceHash(testStr):
#     newStr = str()
#     for i in testStr.split(" "):
#         if len(i) >= 5:
#             newStr += " "+len(i)*"#"
#         else:
#             newStr += " "+i
#     return newStr
# print(replaceHash("Count the lowercase letters in the said list of words:"))
#104
# testStr = "Red Green WHITE"
# newList = []
# newStr = ""
# for i in testStr.split(" "):
#     newStr = i[0].upper() + i[1:].lower()
#     newList.append(newStr)
# print(" ".join(newList))
#105
# import re
# testStr = "fully-qualified-domain@example.com"
# index = re.search("@",testStr).span()[0]
# print(testStr[:index])
#106
# class mySolution():
#     def __init__(self,testStr) -> None:
#         self.testStr = testStr
#     def Solve(self):
#         finalResult = ""
#         result = self.testStr[0]
#         for i in range(1,len(self.testStr)):
#             if self.testStr[i] not in result:
#                 result += self.testStr[i]
#             else:
#                 result = result[0]
#                 finalResult += result[0]
#                 result = ""
#         return finalResult
# p1 = mySolution("aabbbcdeffff")
# print(p1.Solve())
#107
# def countTries(str1,str2):
#     count = 0
#     for i in range(3,len(str1)):
#         for j in range(3,len(str2)):
#             print(list(str2[j-3:j]))
#             print(list(str1[i-3:i]))
#             count += 1
# countTries("Red","RedWhiteGreen")?
#108
# def newString(testStr):
#     newStr = ""
#     for i in testStr:
#         if i.lower() not in ['a','e','i','o','u']:
#             newStr += '-' + i + "-"
#         else:
#             newStr += i
#     return newStr
# print(newString("aeiou"))
#109
# def countLeapYears(testStr):
#     lowerYear,upperYaer = [int(i) for i in testStr.split('-')]
#     count = 0
#     for i in range(lowerYear,upperYaer):
#         if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
#             count += 1
#     return count
# print(countLeapYears("1981-1991"))
#110
# testStr = "PythonExercisesPracticeSolution"
# result = testStr[0]
# for i in testStr[1:]:
#     if not i.isupper():
#         result += i
#     else:
#         result += " "+i
# print(result)
#111
# import string
# testStr = "Python"
# result = ""
# for i in testStr:
#     result += " "+ str(string.ascii_lowercase.index(i.lower()))
# print(result)
#112
# str1,str2 =  "234242342341", "2432342342"
# print(str(int(str1) + int(str2)))
#113
# testStr = "Red Green Black White Pink"
# print(" ".join(sorted(testStr.split(" "),key=lambda x : ord(x[0]))))





    

        




        





    
        