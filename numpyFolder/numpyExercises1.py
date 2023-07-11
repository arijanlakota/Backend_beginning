import numpy as np
#1. print(np.__version__)
# print(np.show_config())
#2.
# print(np.info(np.add))
#3.
# arr  = np.array([12,2,3,0])
# print(np.all(arr))
# 4.arr  = np.array([12,2,3,0])
# print(np.any(arr))
#5.
# arr  = np.array([12,2,3,0,np.nan,np.inf])
# print(np.isfinite(arr))
#6.
# arr = np.array([1,2,3,4,np.inf,-np.inf])
# newarr = np.isinf(arr)
# print(newarr) 
#7.
# arr  = np.array([12,2,3,0,np.nan])
# print(np.isnan(arr))
#8.
# arr  = np.array([12,2,3,0,5j])
# newArr = []
# for i in arr:
#     if np.isreal(i) or np.iscomplex(i) and np.isscalar(i):
#         newArr.append(True)
#     else:
#         newArr.append(False)
# print(newArr)
#9.
#?
#10
# arr1 = np.array([12,23,1,4,6,22,0])
# arr2 = np.array([16,17,4,0,24,0,25])
# print(np.greater(arr1,arr2))
# print(np.greater_equal(arr1,arr2))
# print(np.less(arr1,arr2))
# print(np.less_equal(arr1,arr2))
#11
# arr1 = np.array([12,23,1,4,6,22,0])
# arr2 = np.array([16,17,4,0,24,22,25])
# print(np.equal(arr1,arr2))
# print(np.allclose(arr1,arr2))
#12
# arr = np.array([1,7,13,105])
# print("%d bytes" % (arr.size * arr.itemsize))
#13
# arr0 = np.zeros(10)
# arr1 = np.ones(10)
# arr5 = arr1 * 5
# print(arr0,arr1,arr5)
#14
# arr = np.arange(30,71)
# print(arr)
#15
# testArr = np.arange(30,71) % 2 == 0
# print(np.arange(30,71)[testArr])
#16
# arr = np.identity(3)
# print(arr)
# 17
# rand_num = np.random.normal(0,1,1)
# print(rand_num)
# 18
# arr = np.random.normal(0,1,15)
# print(arr)
# 19.
# arr = np.arange(15,56)
# print(arr[1:-1])
#20
# arr = np.arange(10,22).reshape((3,4))
# for i in np.nditer(arr):
#     print(i)
#21
# arr = np.linspace(10,49,5)
# print(arr)
#22
# arr = np.arange(0,21)
# newView = arr.view()
# newView[9:16] = newView[9:16] * (-1)
# print(arr) 
#23
# arr = np.array_split(np.arange(11),5)
# print(arr)
#24
# arr1 = np.array([12,23,1,4,6,22,0])
# arr2 = np.array([16,17,4,0,24,22,25])
# print(np.multiply(arr1,arr2))
#25
# arr = np.array_split(np.arange(10,22),3)
# arr1 = np.arange(10,22).reshape(3,4)
# print(arr1)
#26
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr.shape)
#27
# x = np.eye(3)
# print(x)
#28
# arr = np.ones((10, 10))
# arr[1:-1, 1:-1] = 0
# print(arr)
#29
# arr = np.diag([1,2,3,4,5])
# print(arr)
#30
# arr = np.zeros((4,4))
# arr[::2, 1::2] = 1
# arr[1::2, ::2] = 1
# print(arr)
#31
# arr = np.random.random((3,3,3))
# print(arr)