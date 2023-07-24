import numpy as np
# 1 print(np.__version__)
# 2 
# nes = [1,2,3,4]
# arr = np.array(nes)
#3
# arr = np.arange(2,11).reshape((3,3))
# print(arr)
#4
# arr = np.zeros(10)
# arr[5] = 11
# print(arr)
#5
# print(np.arange(12,39))
#6
# arr = np.arange(1,11)
# newArr = arr[::-1]
# print(newArr)
#7
# arr = np.arange(1,5,dtype='f')
# print(arr)
#8 
# arr = np.ones(100).reshape((10,10))
# arr[1:-1,1:-1] = 0
# print(arr)
#9
# x = np.ones((3,3))
# x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
# print(x)
#10
# arr = np.ones((8,8))
# arr[::2,::2] = 0
# arr[1::2,1::2] = 0
# print(arr)
#11
# tup = (1,2,3,4,7,5,6,9)
# arr = np.array(tup)
# print(arr)
#12
# x = [10,20,30]
# print(np.append(x,[40,50,60,70,80,90]))
#13
# arr1 = np.empty((3,3))
# print(arr1)
# arr2 = np.full((3,3),6)
# print(arr2)
#14
# arrCent =  np.array([0, 12, 45.21, 34, 99.91])
# arrFehn = arrCent*9/5 + 32
# print(arrFehn)
#15
# arr = np.array([1+2j,2-3j,-1-1j])
# arrNew = np.real(arr)
# print(arrNew)
#16
# arr = np.array([1,2,3])
# print(len(arr))
# print(arr.itemsize)
# print(arr.itemsize * len(arr))
#17
# arr1 = np.array([ 0,10,20,40,60])
# arr2 = np.array([0,40])
# print(np.in1d(arr1,arr2))
#18
# arr1 = np.array([ 0 ,10 ,20 ,40 ,60])
# arr2 = np.array([10, 30, 40])
# print(np.intersect1d(arr1,arr2))
#19
# arr1 = np.array([10 ,10 ,20 ,20 ,30 ,30])
# print(np.unique(arr1))
# print(arr1)
#20
# arr1 = np.array([0 ,10 ,20 ,40 ,60 ,80])
# arr2 = np.array([10, 30, 40, 50, 70, 90])
# print(np.setdiff1d(arr1,arr2))
#21
# arr1 =np.array([ 0,10,20,40,60,80])
# arr2 = np.array([10, 30, 40, 50, 70])
# print(np.setxor1d(arr1,arr2))
#22
# arr1 =np.array([ 0,10,20,40,60,80])
# arr2 = np.array([10, 30, 40, 50, 70])
# print(np.union1d(arr1,arr2))
# 23
# arr1 =np.array([ 1,10,20,40,60,80])
# print(np.all(arr1))
#24
# arr1 =np.array([[ 1,10,20,40,60,80],[True,True,False,True],[1,1,1,0]])
# print(arr1.any(axis=0))
#25
# arr = np.array([1,2,3,4])
# newArr = np.tile(arr,3)
# print(newArr)
#26
# arr = np.array([1,2,3,5])
# print(np.repeat(arr,2))
#27
# arr = np.array([1,2,3,4,5,6])
# print(np.argmax(arr))
# print(np.argmin(arr))
#28
# arr1 = np.array([1,2])
# arr2 = np.array([0,8])
# print(np.greater(arr1,arr2))
# print(np.greater_equal(arr1,arr2))
# print(np.less(arr1,arr2))
# print(np.less_equal(arr1,arr2))
#29


