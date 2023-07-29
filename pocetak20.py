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
# testStr = "asdkjaskld"
# temp = testStr[0]
# testStr = testStr[-1] + testStr[1:-1] + temp
# print(testStr)
#11
# testStr = "amvdfoksdofkds"
# oddStr = ""
# for i in range(len(testStr)):
#     if i % 2:
#         oddStr += testStr[i]
# print(oddStr)
#12
# testStr = "I love cooking love cooking I"
# keysVal = testStr.split(" ")
# for i in keysVal:
#     print(i,testStr.count(i))
#13
# testStr = "skdk"
# print(testStr.upper())
# print(testStr.lower())
#14
# testStr = 'red, white, black, red, green, black'
# colorArr = testStr.split(',')
# print(",".join(sorted(list(set(colorArr)))))
#15
# def addTags(charTag,testStr):
#     return "<%s>%s<%s>" % (charTag,testStr,charTag)
# print(addTags('b',"Python Nesto"))
#16
# def insert_string_middle(aroundStr,testStr):
#     return aroundStr[:int(len(aroundStr)/2)] + testStr +aroundStr[int(len(aroundStr)/2):] 
# print(insert_string_middle("[[]]","Python"))
#17
# def lastTwo(testStr):
#     return 4 * testStr[-2:]
# print(lastTwo("nesto"))
#18
# def firstThree(testStr):
#     print(testStr[:3])
# print(firstThree("python"))
#19
# def partOfString(testStr,specChar):
#     returnStr = ""
#     for i in testStr:
#         if i != specChar:
#             returnStr += i
#         else:
#             break
#     return returnStr
# print(partOfString("https://www.w3resource.com/python-exercises","-"))
#20
# def reverseString(testStr):
#     if not(len(testStr) % 4):
#         return testStr[::-1]
# print(reverseString("lajn"))
#21
# def allUpper(testStr):
#     count = 0
#     for i in testStr[:4]:
#         if i.isupper():
#             count += 1
#     if count >= 2:
#         return testStr.upper()
#     return testStr
# print(allUpper("PYnekte"))
#22
# def lexicographi_sort(s):
#     return sorted(sorted(s), key=str.upper)
# print(lexicographi_sort("djsfksd"))
#23
# testStr = """alskd; 
#       lksajdlkasjd 
#       lksajdlksad 
#       lkjaslkdsakldj 
#       lsakd"""
# print(testStr.replace('\n',""))
#24
# def itStart(specChar,testStr):
#     if testStr.startswith(specChar):
#         return True
#     return False
# if itStart("P","Ptyhon"):
#     print("works")
#25
# import string
# def cesearCipher(testStr,shifth):
#     newStr = ""
#     for i in range(len(testStr)):
#         newIndex = list(string.ascii_lowercase).index(testStr[i]) - shifth
#         newStr += string.ascii_lowercase[newIndex]
#     return newStr
# print(cesearCipher("de",3))
#26
# import textwrap
# sample_text = '''
#     Python is a widely used high-level, general-purpose, interpreted,
#     dynamic programming language. Its design philosophy emphasizes
#     code readability, and its syntax allows programmers to express
#     concepts in fewer lines of code than possible in languages such
#     as C++ or Java.
#     '''
# print(textwrap.dedent(sample_text))
#27
# import textwrap
# sample_text = '''
#   Python is a widely used high-level, general-purpose, interpreted,
#   dynamic programming language. Its design philosophy emphasizes
#   code readability, and its syntax allows programmers to express
#   concepts in fewer lines of code than possible in languages such
#   as C++ or Java.
#   '''
# print(textwrap.fill(sample_text, width=50))
#28
# sample_text = '''
#   Python is a widely used high-level, general-purpose, interpreted,
#   dynamic programming language. Its design philosophy emphasizes
#   code readability, and its syntax allows programmers to express
#   concepts in fewer lines of code than possible in languages such
#   as C++ or Java.
#   '''
# import textwrap
# testWithPrefix = textwrap.indent(sample_text,"nesto")
# print(testWithPrefix)
#29
# sample_text = '''
#   Python is a widely used high-level, general-purpose, interpreted,
#   dynamic programming language. Its design philosophy emphasizes
#   code readability, and its syntax allows programmers to express
#   concepts in fewer lines of code than possible in languages such
#   as C++ or Java.
#   '''
# import textwrap
# text1 =  textwrap.dedent(sample_text).strip()
# print(textwrap.fill(text1,
#                     initial_indent='',
#                     subsequent_indent=' ' * 4,
#                     width=80,
#                     ))
#30
# import decimal
# decimal.getcontext().prec = 2
# decimal.getcontext().rounding = decimal.ROUND_FLOOR
# num1 = 123.575
# print(decimal.Decimal(num1))
# num1 = 123.34234234
# print("rounded number {:.2f}".format(num1))
#31
# num1 = -1.12323334
# print("rounded number {:-.2f}".format(num1))
#32
# num1 = -12.34234234
# num2 = 60.3424234
# print("without decimals {:.0f}".format(num1))
# print("without decimals {:.0f}".format(num2))
#33
# num1 = 3
# print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(num1))
#34
# num1 = 3
# print("Formatted Number(right padding, width 2): "+"{:*<2d}".format(num1))
#35
# num1 = 1230000000
# print("Formatted Number(comma seperator, width 2): "+"{:,}".format(num1))
#36
# num1 = 1
# print("Formatted Number(comma seperator, width 2): "+"{:.2%}".format(num1))
#37
# num1 = 125
# print("formatted number with left align {:> 10}".format(num1))
# print("formatted number with left align {:< 10}".format(num1))
# print("formatted number with left align {:^ 10}".format(num1))
#38
# testStr = "dlkf;lsdkf dl dl"
# print(testStr.count("dl"))
#39
# testStr = "kdjfklsdfj"
# print(testStr[::-1])
#40
# testStr = "string with more words"
# print(" ".join([i[::-1] for i in testStr.split(" ")]))
# print(testStr.split(" ")[::-1])
#41
# testStr = "kaKsndKdnsKds"
# a = testStr.strip('K')
# print(a)
#42
# testStr = 'thequickbrownfoxjumpsoverthelazydog'
# class mySolution():
#     def __init__(self,myStr) -> None:
#         self.myStr = myStr
#         self.countedLetter = {}
#     def Solve(self):
#         for i  in testStr:
#             if i not in self.countedLetter.keys():
#                 if testStr.count(i) == 1:
#                     continue
#                 self.countedLetter[i] = testStr.count(i)
#         return self.countedLetter
# p1 = mySolution(testStr)
# print(p1.Solve())
#43
# area = 123.3423423
# volume = 123.342342
# print("the area is {0:.{1}f} cm\u00b2".format(area,2))
# print("the area is {0:.{1}f} cm\u00b3".format(volume,2))
#44
# testStr = "w3resource"
# for i,j in enumerate(testStr):
#     print("current charater {0} at position {1}".format(j,i))
#45
# import string
# testStr = 'thequickbrownfoxjumpsoverthelazydog'
# if(sorted(list(set(testStr)))) == list(string.ascii_lowercase):
#     print(True)
#46
# testStr = 'the quick brown fox jumps over the lazy dog'
# print(testStr.split(" "))
#47
# def lowerSome(testStr,n):
#     print(testStr[:n].lower() + testStr[n:])
# lowerSome("AJDsadsa",3)
#48
# testStr = "32.054,23"
# newStr = ""
# for i in testStr:
#     if i == '.':
#         newStr += ','
#     elif i ==',':
#         newStr +='.'
#     else:
#         newStr += i
# print(newStr)
#49
# testStr = "text with vowels"
# for i in ['a','e','i','o','u']:
#     print(i,testStr.count(i))
#50
# str1 = "w,3,r,e,s,o,u,r,c,e"
# print(str1.rsplit(',',1))
#51
# testStr = "aksmdImaNeasdKaksd"
# for i in testStr:
#     if testStr.count(i) == 1:
#         print(i)
#         break
#52
# from itertools import product
# testStr = 'xyz'
# print([i for i in product(list(testStr),repeat=2)])
        





