#1
# for i in range(1500,2701):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)
#2
# c = 60
# f = c * 9/5 + 32
# print(f)
#3
# n = int(input("Take a guess between 1-9: "))
# while n != 6:
#     n = int(input("Take a guess between 1-9: "))
# print("Well done")
#4
# for i in range(2):
#     for j in range(5):
#         if i == 0:
#             print('* ' * j,end="")
#         else:
#             print('* ' * (5-j),end="")
#5
# testStr = input('input word: ')
# print(testStr[::-1])
#6
# testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# countOdd = 0
# countEven = 0
# for i in testList:
#     if i % 2:
#         countOdd += 1
#     else:
#         countEven +=1
# print(countOdd,countEven)
#7
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# [print(type(i)) for i in datalist]
#8
# for i in range(7):
#     if i == 3 or i == 6:
#         continue
#     print(i)
#9
# def fibonachi():
#     generate = [0,1]
#     for i in range(1,100):
#         generate.append(generate[i-1]+generate[i])
#         if generate[i] > 50:
#             break
#     return generate
# print(fibonachi())
#10
# for i in range(0,51):
#     word = ""
#     if i % 3 == 0:
#         word += 'fizz'
#     if i % 5 == 0:
#         word += 'buzz'
#     if word == '':
#         word = i
#     print(word)
#     word = ""
#11
# m = 10
# n = 6
# for i in range(m):
#     for j in range(n):
#         print(i*j,end=" ")
#     print()
#12
# lines = []
# while True:
#     l = input()
#     if l:
#         lines.append(l.upper())
#     else:
#         break
# for l in lines:
#     print(l)
#13
# testList = ['0100','0011','1010','1001','1100','1001']
# for i in testList:
#    if int(i,2) % 5 == 0:
#       print(i)
#14
# class mySolution():
#     def __init__(self,classList) -> None:
#         self.classList = classList
#     def Solve(self):
#         countLetters = 0
#         countNumbers = 0
#         for i in self.classList:
#             if i.isnumeric():
#                 countNumbers+=1
#             elif i.isalpha():
#                 countLetters+=1
#         return countLetters,countNumbers
# p1 = mySolution('Python 3.2')
# print(p1.Solve())
#15
# import re
# def checkValid(password):
#     if re.search('[a-z]',password) and re.search('[A-Z]',password) and re.search('[0-9]',password):
#         if 6 <= len(password) <= 16:
#             return True
#     return False
# print(checkValid('passwordW3r@100a'))
#16
# def isEven(a):
#     return all(int(i) % 2 == 0 for i in str(a))
# for i in range(100,401):
#     if isEven(i):
#         print(i,end=",")
#17
# result_str="";    
# for row in range(0,7):    
#     for column in range(0,7):     
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
#             result_str=result_str+"*"    
#         else:      
#             result_str=result_str+" "    
#     result_str=result_str+"\n"    
# print(result_str);
#18
# ===================================================== # empty letters
#31
# humanEars = int(input())
# if humanEars <= 2:
#     print(humanEars*10.5)
# else:
#     print(21 + (humanEars-2)*4)
#32
# testLetter = input()
# if testLetter.lower() in ['a','e','i','o','u']:
#     print('vowel')
# else:
#     print('consonant')
#33
# monthDict = {
#     'January':31 ,
#     'February' :28/29,
#     'March' :31,
#     'April' :30,
#     'May':31,
#     'June' :30,
#    'July':31,
#     'August':31,
#    'September':30, 
#     'October':31 ,
#     'November':30,
#     'December':31                                
# } 
# print(monthDict['December'])
#34
# a1 = int(input())
# a2 = int(input())
# if 15 <= a1 + a2 <= 20:
#     print(20)
# else:
#     print(a1+a2)
#35
# testStr = '5'
# try :
#     print(int(testStr),'is integer')
# except:
#     print('is not integer')
#36
# x = int(input())
# y = int(input())
# z = int(input())
# if(x==y and y==z):
#     print('equilateral')
# elif(x == y or x == z or z == y):
#     print(' isosceles')
# else:
#     print('soselce')
#37
# month = input("Input the month (e.g. January, February etc.): ")
# day = int(input("Input the day: "))

# if month in ('January', 'February', 'March'):
# 	season = 'winter'
# elif month in ('April', 'May', 'June'):
# 	season = 'spring'
# elif month in ('July', 'August', 'September'):
# 	season = 'summer'
# else:
# 	season = 'autumn'

# if (month == 'March') and (day > 19):
# 	season = 'spring'
# elif (month == 'June') and (day > 20):
# 	season = 'summer'
# elif (month == 'September') and (day > 21):
# 	season = 'autumn'
# elif (month == 'December') and (day > 20):
# 	season = 'winter'

# print("Season is",season)
#38
# day = int(input("Input birthday: "))
# month = input("Input month of birth (e.g. march, july etc): ")
# if month == 'december':
# 	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
# elif month == 'january':
# 	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
# elif month == 'february':
# 	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
# elif month == 'march':
# 	astro_sign = 'Pisces' if (day < 21) else 'aries'
# elif month == 'april':
# 	astro_sign = 'Aries' if (day < 20) else 'taurus'
# elif month == 'may':
# 	astro_sign = 'Taurus' if (day < 21) else 'gemini'
# elif month == 'june':
# 	astro_sign = 'Gemini' if (day < 21) else 'cancer'
# elif month == 'july':
# 	astro_sign = 'Cancer' if (day < 23) else 'leo'
# elif month == 'august':
# 	astro_sign = 'Leo' if (day < 23) else 'virgo'
# elif month == 'september':
# 	astro_sign = 'Virgo' if (day < 23) else 'libra'
# elif month == 'october':
# 	astro_sign = 'Libra' if (day < 23) else 'scorpio'
# elif month == 'november':
# 	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
# print("Your Astrological sign is :",astro_sign)
#39
# year = int(input("Input your birth year: "))
# if (year - 2000) % 12 == 0:
#     sign = 'Dragon'
# elif (year - 2000) % 12 == 1:
#     sign = 'Snake'
# elif (year - 2000) % 12 == 2:
#     sign = 'Horse'
# elif (year - 2000) % 12 == 3:
#     sign = 'sheep'
# elif (year - 2000) % 12 == 4:
#     sign = 'Monkey'
# elif (year - 2000) % 12 == 5:
#     sign = 'Rooster'
# elif (year - 2000) % 12 == 6:
#     sign = 'Dog'
# elif (year - 2000) % 12 == 7:
#     sign = 'Pig'
# elif (year - 2000) % 12 == 8:
#     sign = 'Rat'
# elif (year - 2000) % 12 == 9:
#     sign = 'Ox'
# elif (year - 2000) % 12 == 10:
#     sign = 'Tiger'
# else:
#     sign = 'Hare'

# print("Your Zodiac sign :",sign)
#40
# l1 = int(input())
# l2 = int(input())
# l3 = int(input())
# print(sorted([l1,l2,l3])[1])
#41
# year = int(input("Input a year: "))

# if (year % 400 == 0):
#     leap_year = True
# elif (year % 100 == 0):
#     leap_year = False
# elif (year % 4 == 0):
#     leap_year = True
# else:
#     leap_year = False

# month = int(input("Input a month [1-12]: "))

# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30


# day = int(input("Input a day [1-31]: "))

# if day < month_length:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
#42
# n = int(input())
# count = 0
# suma = 0
# while n != 0:
#     suma += n
#     count += 1
#     n = int(input())
# print(suma / count)
#43
# num = int(input("Enter a number"))
# for i in range(1,11):
#     print("%d * %d = %d" %(num,i,num*i))
#44
# for i in range(1,10):
#     print('%d'%(i) * i)