import random
#1
#python modules
# import string
# randomColor = random.randint(0,0xFFFFFF)
# print('{} is random color',randomColor)
# alphaString = ''
# for i in range(1,255):
#     alphaString += random.choice(string.ascii_letters)
# print(alphaString)
# print()
#2
# import os
# randomList = [1,2,3,4]
# randomSet = {1,2,3,4}
# randomDict = {"a":1,"b":2,"c":3,"d":4}
# print(random.choice(randomList))
# print(random.choice(list(randomSet)))
# print(randomDict[random.choice(list(randomDict.keys()))])
# print(random.choice(os.listdir("c:/Users/Comp/Desktop/Backend developing")))
#3
# import string
# randomChar = random.choice(string.ascii_letters)
# randomString = ''
# randomStringF = ''
# for i in range(random.randint(1,230)):
#     randomString += random.choice(string.ascii_letters)
# for i in range(7):
#     randomStringF += random.choice(string.ascii_letters)
# print(randomChar,randomString,randomStringF)
#4
# randomNum = random.random()
# randomGenerator = random.Random(0).random()
# print(randomNum,randomGenerator)
#5
# import datetime
# random1 = random.randrange(5)
# random2 = random.randrange(5,10)
# random3 = random.randrange(0,10,3)
# start_dt = datetime.date(2019, 2, 1)
# end_dt = datetime.date(2019, 3, 1)
# time_b = end_dt-start_dt
# days_b = time_b.days
# random4 = random.randrange(days_b)
# random_date = start_dt + datetime.timedelta(days=random4)
# print(random2,random1,random3,random_date)
#6
# import numpy as np
# testList = [1,2,3,4,5]
# print(np.random.permutation(testList))
#7
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# arr = np.random.uniform(size=100)
# sns.displot(arr,kind="kde")
# plt.show()
#8
# arr = range(0,10)
# print(arr)
# print(random.sample(arr,3))
#9
# a = random.Random(10).random()
# print(a)
#types
import types
#10
# def myFunc():
#     print("nesto")
# print(isinstance(myFunc,types.FunctionType))
# print(isinstance(max,types.FunctionType))
# print(isinstance(lambda x: x,types.LambdaType))
#11
# class myClass():
#     def __init__(self) -> None:
#         pass
#     def myMethod(self):
#         return 1
# print(isinstance(myClass().myMethod,types.MethodType))   
# 12
# def myGenerator(a):
#     yield a
# print(isinstance(myGenerator(320),types.GeneratorType)) 
#13
# code = compile("print('nesto')","sample","exec")
# print(isinstance(code,types.CodeType))
# print(isinstance(types,types.ModuleType)) 
# 14
import decimal
# a = decimal.Decimal((1.232324))
# print(a.as_tuple())
# b = decimal.Decimal('1.5')
# print(b.as_tuple())      
#15
# decimal.getcontext().prec = 3
# decimal.getcontext().rounding = decimal.ROUND_UP
# print(decimal.Decimal(30) / decimal.Decimal(4))
# print(decimal.Decimal(8.352))
#16
# def round_to_10_cents(x):
#     remainder = x.remainder_near(decimal.Decimal('0.10'))
#     if abs(remainder) == decimal.Decimal('0.05'):
#         return x
#     else:
#         return x - remainder
# print(round_to_10_cents(0.80))
#17
# decimal.getcontext().prec = 3
# decimal.getcontext().rounding = decimal.ROUND_CEILING
# print(decimal.Decimal(20)/decimal.Decimal(6))
# decimal.getcontext().prec = 3
# decimal.getcontext().rounding = decimal.ROUND_FLOOR
# print(decimal.Decimal(20)/decimal.Decimal(6))
#18
# decimal.getcontext().prec = 3
# decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN
# print(decimal.Decimal(10)/decimal.Decimal(4))
# decimal.getcontext().prec = 3
# decimal.getcontext().rounding = decimal.ROUND_HALF_UP
# print(decimal.Decimal(10)/decimal.Decimal(4))
#19
# decimal.getcontext().prec = 1
# decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
# print(decimal.Decimal(10)/decimal.Decimal(4))
#20
# print(decimal.Decimal(-102000e-5))
import copy
#21
# arr = [1,2,3,4]
# copyList = copy.copy(arr)
# print(copyList)
#22
# arr = [1,[1,2],4]
# copylist = copy.deepcopy(arr)
# print(copylist)
#23
# thisDict = {"a":1,"b":2,"c":3}
# copyDict = copy.copy(thisDict)
# print(copyDict)
#24
# thisDict = {"a":1,"b":2,"c":3}
# copyDict = copy.deepcopy(thisDict)
# print(copyDict)
#25
import csv
# a = csv.reader(open('test.csv','r'))
# for i in a:
#     print(i)
#26
# a = csv.reader(open('test.csv','r'))
# print(len(list(a)))
#27
# a = """ 1 2 3
#         4 5 6
#         7 8 9
# """
# csvLines = a.splitlines()
# csvList = csv.reader(csvLines)
# parsed_csv = list(csvList)
# print(parsed_csv)
#28
# csv_reader = csv.reader(open('test.csv','r'))
# print(next(csv_reader))
# print(next(csv_reader))
# print(next(csv_reader))
#29
# csv_reader = csv.reader(open('test.csv','r'))
# next(csv_reader)
# for i in csv_reader:
#     print(i)
#30
# fr = open('test.csv','w')
# csv_reader = csv.writer(fr,delimiter=",")
# csv_reader.writerow(["a","b","c"])
# csv_reader.writerow(["d","e","f"])
# csv_reader.writerow(["g","h","i"])
# fr.close()
# newCsv = csv.reader(open('test.csv','r'),delimiter=",")
# for i in newCsv:
#     print(i)
#31
# fr = open('test.csv','r')
# csv_reader = csv.reader(fr)
# print(list(dict(csv_reader)))






