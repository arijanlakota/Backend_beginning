#54 string
# testStr = "abcdegba"
# for i in testStr:
#     if testStr.count(i) > 1:
#         print(i)
#     break
#55
# testStr= "string , with more words string words"
# for i in testStr.split(" "):
#     if testStr.count(i) > 1:
#         print(i)
#     break
#56
# testStr = "string , with more words string words string"
# testDict = dict()
# testList = list()
# for i in testStr.split(" "):
#     testDict[i] = testStr.count(i)
#     if testStr.count(i) not in testList:
#         testList.append(testStr.count(i))
# def getKey(myDict,myValue):
#     for x,y in myDict.items():
#         if y == myValue:
#             return x
# testList.remove(max(testList))
# print(getKey(testDict,max(testList)))
#57
# testStr = "Nikom ne dajem string"
# print(testStr.replace(" ",""))
#58
# testStr = "sfdsf dsf dsf dsf"
# print(" " * testStr.count(" ") + testStr.replace(" ",""))
#59
# testStr = "dsaf asfda sadfasf af"
# print(len(set(testStr.replace(" ",""))))
#60
# def capitalize_first_last_letters(str1):
#      str1 = result = str1.title()
#      result =  ""
#      for word in str1.split():
#         result += word[:-1] + word[-1].upper() + " "
#      return result[:-1] 
#61
# def removeDuplicate(str1):
#     result = ""
#     for i in str1:
#         if i not in list(result):
#             result += i
#     print(result)
# removeDuplicate("ssassad")
#62
# testStr = "123s342"
# result = 0
# for i in testStr:
#     if i.isnumeric():
#         result += int(i)
# print(result)
#63
# def removeZeroes(ipStr):
#     result = ""
#     for i in ipStr.split("."):
#         if '0' in i:
#             result += i.replace('0',"") + '.'
#         else:
#             result += i + '.'
#     return result
# print(removeZeroes("255.024.01.01"))
#64
# def findLength(binStr):
#     count = 0
#     countList = list()
#     for i in binStr:
#         if i == '0':
#             count += 1
#         else:
#             countList.append(count)
#             count = 0
#         countList.append(count)
#     return(max(countList))
# print(findLength('1100101100010000'))
#65
# def findSimilar(str1,str2):
#     result = []
#     for i in (str1):
#         for j in str2:
#             if i == j:
#                 result.append(i) 
#     if len(result) == 0:
#         return "there is no such latters"
#     return sorted(list(set(result)))
# print(findSimilar("anfnga","asdemog"))
#66
# import random
# def anagramStr(str1,str2):
#     result = ""
#     for i in str1:
#         if i in str2:
#             result += i
#     return result
# print(anagramStr("ja sam nesto jeo","nejesoklasm"))
#67
# from itertools import groupby
# testList = [i for i,j in groupby("xxxyyy")]
# print("".join(testList))
#68
# def madeTwo(testStr):
#     str1 = str2 = ""
#     for i in testStr:
#         if testStr.count(i) == 1:
#             str1 += i
#         else:
#             str2 += i
#     return [str1,str2]
# print(madeTwo("aabbcceffgh"))
#69
# def getValue(thisDict,thisValue):
#     for i,j in thisDict.items():
#         if j == thisValue:
#             return i
# def findLongest(str1,str2):
#     result = ""
#     resultDict = dict()
#     for i in str1:
#         result += i
#         if result not in str2:   
#             resultDict[result[:-1]] = len(result)
#             result = ""
        
#     return getValue(resultDict,max(resultDict.values()))
# print(findLongest("jakamoli","hnamolp"))
#70
# def uncommonStr(str1,str2):
#     return "".join(list(set(str1).symmetric_difference(str2)))
# print(uncommonStr("abgsaaaba","hffsasb"))
#71
# def moveSpaces(str1): 
#     no_spaces = [char for char in str1 if char!=' ']   
#     space= len(str1) - len(no_spaces)
#     result = ' '*space    
#     return result + ''.join(no_spaces)
#72

  

            






 
        
    
