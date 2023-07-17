import numpy as np
#without vectorization
# x = [1,2,3,4,5]
# y = [2,3,4,5,6]
# z = []
# for i,j in zip(x,y):
#     z.append(i+j)
# print(z)
#with vectorization
# x = [1,2,3,4,5]
# y = [2,3,4,5,6]
# print(np.add(x,y))
#creating ufunc function
# def myAdd(x,y):
#     return x + y
# myAdd = np.frompyfunc(myAdd,2,1)
# print(myAdd([1, 2, 3, 4],[5, 6, 7, 8]))
# print(type(myAdd))
# print(type(np.concatenate))
#checking if functions is ufunc
# if type(np.add) == np.ufunc:
#     print("add is ufunc")
# else:
#     print("is not")
#conditional arythmetic
# arr1 = np.array([10,12,16,20,13])
# arr2 = np.array([3,4,7,1,2])
# print(np.power(arr1,arr2))
#rounding decimals
#truncation
# arr = np.array([-3.16666,3.66667])
# print(np.trunc(arr))
#rounding
# arr1 = np.around(3.16667,2)
# print(arr1)
#floor
# arr= np.array([-3.123123,3.888889])
# print(np.floor(arr))
#ceil
# arr = np.array([-3.123123,3.888889])
# print(np.ceil(arr))
#log
# arr = np.arange(1,10)
# print(np.log10(arr))
# print(np.log2(arr))
# print(np.log(arr))
# from math import log
# myLog = np.frompyfunc(log,2,1)
# print(myLog(100,15))
#sumations
# arr1 = np.array([4,2,3])
# arr2 = np.array([4,2,3])
# print(np.sum([arr1,arr2],axis=1))
# print(np.cumsum(arr1))
#Products
# arr = np.arange(1,11)
# arr1 = np.linspace(1,10,10,dtype="i")
# print(arr1)
# x =np.prod([arr1,arr])
# print(x)
#Differences
# arr = np.array([1,2,3,4,5])
# print(np.diff(arr,n=2))
#finding LCM
# class findLCM():
#     def __init__(self,a1,a2) -> None:
#         self.a1 = a1
#         self.a2 = a2
#     def Solve(self):
#         return np.lcm(self.a1,self.a2)
# class miniFindLCM(findLCM):
#     def __init__(self, a1, a2) -> None:
#         super().__init__(a1, a2)
#     def Solve(self):
#         newArr = []
# p1 = miniFindLCM(4,6)
# print(p1.Solve())
# arr = np.array([3,6,9])
# print(np.lcm.reduce(arr))
# arr = np.array([100,20,80])
# print(np.gcd.reduce(arr))
# x = np.cos(np.pi/2)
# print(x)
#trigonometry
# arr = np.array([10,12,3,0.7,3.5,11])
# arr = np.rad2deg(arr)
# print(np.cos(arr))
# newArr = np.cos(arr)
# newArr1 = np.arccos(newArr)
# print(newArr1)
# x1 = 3
# x2 = 4
# print(np.hypot(x1,x2))
#set operators
# arr = np.array([1,1,1,2,2,2,3,3,4,4,4,5,5,6,6,6,7,8,8,9])
# arr1 = np.unique(arr)
# arr2 = np.array([3,4,5,6,22])
# print(np.union1d(arr1,arr2))
# print(np.intersect1d(arr1,arr2))
# print(np.setdiff1d(arr1,arr2,assume_unique=True))
# print(np.setxor1d(arr1,arr2,assume_unique=True))





