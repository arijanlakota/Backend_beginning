# python string
#1
# testStr = "sasadasd"
# print(len(testStr))
#2
# testStr =  'google.com'
# thisDict = {}
# for i in testStr:
#     thisDict[i] = testStr.count(i)
# print(thisDict)
#3
# testStr = 'w3resource'
# print(testStr[:2] + testStr[-2:])
#4
# testStr = 'restart'
# testStr1 = testStr[0] + testStr[1:].replace('r','$')
# print(testStr1)
#5
# str1 = "abc"
# str2 = "xyz"
# str3 = str2[:2]+ str1[2:] + " "+ str1[:2]+ str2[2:]
# print(str3)
#6
# def changeStr(testStr):
#     if len(testStr) >= 3:
#         if testStr.endswith("ing"):
#             testStr += 'ly'
#         else:
#             estStr += 'ing'
#     return testStr
#7
# import re
# testStr = 'The lyrics is not that poor!'
# notIndex  = re.search("not",testStr).span()
# poorIndex = re.search("poor",testStr).span()
# if notIndex[0] < poorIndex[0]:
#     print(testStr.replace(testStr[notIndex[0]:poorIndex[1]],"good"))
#8
# arr = ["PHP","Exercies","Backend"]
# thisDict = {}
# for i in arr:
#     thisDict[i] = len(i)
# for a,b in thisDict.items():
#     if b == max(thisDict.values()):
#         print(a,b)
#9
# testStr = "aksjaskdasd"
# n = 4
# testStr = testStr[:n] + testStr[n+1:]
# print(testStr)
#10
testStr = "asdkjaskld"
temp = testStr[0]
testStr = testStr[-1] + testStr[1:-1] + temp