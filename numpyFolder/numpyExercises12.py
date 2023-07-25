import numpy as np
#`1`
# arr1 = np.array(['Python' ,'PHP'],dtype=np.str)
# arr2 = np.array([' Java', ' C++'],dtype=np.str)
# print(np.char.add(arr1,arr2))
#2
# arr1 = np.array(['Python', 'PHP' ,'Java' ,'C++'],dtype=np.str)
# print(np.char.multiply(arr1,3))
#3
# arr1 = np.array(['python', 'PHP', 'java' ,'C++'])
# print(np.char.capitalize(arr1))
# print(np.char.upper(arr1))
# print(np.char.lower(arr1))
# print(np.char.swapcase(arr1))
#4
# arr = np.array(['python exercises' ,'PHP' ,'java', 'C++'])
# print(np.char.center(arr,15,fillchar='_'))
# print(np.char.rjust(arr,15,fillchar='_'))
# print(np.char.ljust(arr,15,fillchar='_'))
#5
# arr = np.array(['python exercises', 'PHP' ,'java' ,'C++'])
# print(np.char.join(" ",arr))
#6
# arr = np.array(['python exercises' ,'PHP','java' ,'C++'])
# r = np.char.encode(arr,encoding="cp500")
# print(np.char.decode(r,encoding="cp500"))
#7
# arr = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'], dtype=np.str)
# print(np.char.strip(arr))
#8?
#9
# arr = np.array([' python exercises ' ,' PHP ' ,' java ', ' C++'])
# print(np.char.lstrip(arr))
#10
# arr = np.array(['Python PHP Java C++'])
# print(np.char.split(arr," "))
#11
# arr = np.array(['Python\\Exercises, Practice, Solution'])
# print(np.char.splitlines(arr))
#12
# arr = np.array(['2' ,'11' ,'234' ,'1234' ,'12345'],dtype=np.str_)
# print(np.char.zfill(arr,5))
#13
# arr = np.array(['PHP Exercises, Practice, Solution'])
# print(np.char.replace(arr,"PHP","Python"))
#14
# arr1 = np.array(['Hello' ,'PHP', 'JS' ,'examples' ,'html'])
# arr2 = np.array(['Hello' ,'php' ,'Java' ,'examples', 'html'])
# print(np.char.greater(arr1,arr2))
# print(np.char.greater_equal(arr1,arr2))
# print(np.char.equal(arr1,arr2))
# print(np.char.not_equal(arr1,arr2))
# print(np.char.less(arr1,arr2))
#15
# arr = np.array(['Python', 'PHP' ,'JS' ,'examples', 'html'])
# print(np.char.count(arr,"P"))
#16
# arr = np.array(['Python' ,'PHP', 'JS', 'EXAMPLES' ,'HTML'])
# print(np.char.find(arr,"P"))
#17
# arr = np.array(['Python' ,'PHP' ,'JS' ,'Examples' ,'html5' ,'5'])
# print(np.char.islower(arr))
# print(np.char.isupper(arr))
# print(np.char.isdigit(arr))
#18
# arr = np.array(['Python', 'PHP', 'JS' ,'examples' ,'html'])
# print(np.char.startswith(arr,"P"))
#19
# arr =  np.array(['1.12', '2.23' ,'3.71', '4.23' ,'5.11'])
# print(np.char.zfill(arr,6))
#20
# arr = np.array([['Python-NumPy-Exercises'],['-Python-']])
# print(np.char.replace(arr,'-','='))
#21
# arr = np.array([['Python', 'NumPy' ,'Exercises'],
# ['Python' ,'Pandas' ,'Exercises'],
# ['Python' ,'Machine learning' ,'Python']])
# print(np.char.count(arr,"Python"))
#22
# testStr = """01 V Debby Pramod
# 02 V Artemiy Ellie
# 03 V Baptist Kamal
# 04 V Lavanya Davide
# 05 V Fulton Antwan
# 06 V Euanthe Sandeep
# 07 V Endzela Sanda
# 08 V Victoire Waman
# 09 V Briar Nur
# 10 V Rose Lykos"""
# print([r.split(" ") for r in testStr.splitlines()])

