import numpy as np
#numpy mathemathics
# 1
# print(np.add(1,4))
# print(np.multiply(1,4))
# print(np.subtract(1,4))
# print(np.divide(1,4))
# 2
# l1 = np.log(1e-50)
# l2 = np.log(2.5e-50)
# print(np.logaddexp(l1,l2))
# print(np.logaddexp2(l1,l2))
#3
# arr = np.array([0 ,1 ,2 ,3 ,4 ,5 ,6 ,7 ,8, 9])
# arr = (arr / 3).astype(float)
# print(arr)
#4
# arr = np.arange(1,5)
# print(np.floor_divide(arr,1.5))
#5
# arr = np.arange(7)
# print(np.power(arr,3))
# 6
# arr = np.arange(7)
# print(np.mod(arr,5))
#7
# arr = np.array([ -10.2, 122.2 ,0.2])
# print(np.abs(arr))
#8
# x = np.round([1.45, 1.50, 1.55])
# print(x)
# x = np.round([0.28, .50, .64], decimals=1)
# print(x)
#9
# arr = np.array([-0.7, -1.5, -1.7 ,0.3 ,1.5 ,1.8 ,2.])
# print(np.round(arr))
#10
# arr = np.array([-0.7, -1.5, -1.7 ,0.3 ,1.5 ,1.8 ,2.])
# print(np.trunc(arr))
# print(np.floor(arr))
# print(np.ceil(arr))
#11
# arr = np.random.rand(15).reshape((5,3))
# arr1 = np.random.rand(6).reshape((3,2))
# print(np.dot(arr,arr1))
#12
# arr1 = np.array([ 1.+2.j ,3.+4.j])
# arr2 = np.array([ 5.+6.j ,7.+8.j])
# print(np.vdot(arr1,arr2))
#13
# arr1 = np.arange(24).reshape((1,6,4))
# arr2 = np.array([0,1,2,3])
# print(np.inner(arr1,arr2))
#14
# arr1 = np.array([ 1., 4., 0.])
# arr2 = np.array([ 2., 2., 1.])
# print(np.inner(arr1,arr2))
# print(np.outer(arr1,arr2))
# print(np.cross(arr1,arr2))
#15
# arr1 = np.array([[1, 0], [1, 1]])
# arr2 = np.array([[3, 1], [2, 2]])
# print(np.matmul(arr1,arr2))
#16
# print(np.roots(p=[1,-2,1]))
# print(np.roots(p=[1,-11,9,11,-10]))
#17
# print(np.polyval([1,-2,1],2))
#18
# arr1 = np.polyadd([1, -2, 1],[1, -12, 10, 7, -10])
# arr2 = np.polymul([1, -2, 1],[1, -12, 10, 7, -10])
# arr3 = np.polysub([1, -2, 1],[1, -12, 10, 7, -10])
# arr4 = np.polydiv([1, -2, 1],[1, -12, 10, 7, -10])
# print(arr1,arr2,arr3,arr4)
#19
# arr = np.array([[10, 30],[20, 60]])
# print(np.mean(arr,axis=0))
# print(np.mean(arr,axis=1))
#20
# arr = np.random.random(1000)
# print(np.average(arr))
# print(np.var(arr))
# print(np.std(arr))
#21
# degArr = np.array([ 0. ,0.5, 0.70710678, 0.8660254, 1. ])
# print(np.cos(degArr))
# print(np.tan(degArr))
#22
# arr = np.array([-1., 0, 1.])
# print(np.arccos(arr))
# print(np.arcsin(arr))
# print(np.arctan(arr))
#23
# arr = np.array( [-np.pi, -np.pi/2, np.pi/2, np.pi])
# print(np.rad2deg(arr))
#24
# arr = np.array([-180., -90., 90., 180.])
# print(np.deg2rad(arr))
#25
# arr = np.array([-1,0,1])
# print(np.sinh(arr))
# print(np.cosh(arr))
# print(np.tanh(arr))
#26
# arr = np.array([ 3.1, 3.5 ,4.5 ,2.9 ,-3.1, -3.5 ,-5.9])
# print(np.around(arr))
# print(np.floor(arr))
# print(np.ceil(arr))
# print(np.trunc(arr))
# print(np.round(arr,decimals=0))
#27
# arr = np.array([[1 ,2 ,3],[4 ,5, 6,]])
# print(np.cumsum(arr))
# print(np.cumsum(arr,axis=1))
# print(np.cumsum(arr,axis=0))
#28
# arr = np.arange(1,7).reshape((2,3))
# print(np.cumprod(arr))
# print(np.cumprod(arr,axis=0))
# print(np.cumprod(arr,axis=1))
#29
# arr = np.array([1 ,3, 5, 7 ,0])
# print(np.diff(arr))
#30
# arr = np.array([1 ,3, 5, 7 ,0])
# print(np.diff(arr,prepend=[0,0],append=[200]))
#31
# arr = np.arange(1,5)
# print(np.exp(arr))
#32
# arr = np.arange(1,5)
# print(np.expm1(arr))
#33
# arr = np.arange(1,5)
# print(np.exp2(arr))
#34
# arr = np.array([1, np.e, np.e**2])
# print(np.log(arr))
# print(np.log10(arr))
# print(np.log2(arr))
# from math import log
# def myLog(a,b):
#     return log(a,b)
# print(type(myLog))
# myLog = np.frompyfunc(myLog,2,1)
# print(type(myLog))
#35
# arr = np.array([1.e-099 ,1.e-100])
# print(np.log1p(arr))
#36
# arr = np.arange(-4,5)
# print(np.signbit(arr))
#37
# arr = np.arange(-1,3)
# print(np.copysign(arr,-1))
#38
# arr = np.array([ 0, 1 ,-1])
# print(np.negative(arr))
#39
# arr = np.array([1. ,2. ,0.2 ,0.3])
# print(np.reciprocal(arr))
#40
# arr1 = np.array([[1 ,2],[3 ,4]])
# arr2 = np.array([[1,2],[1,2]])
# print(np.power(arr1,arr2))
#41
# arr = np.array([ 1 ,3 ,5 ,0 ,-1 ,-7 ,0 ,5])
# print(np.sign(arr))


