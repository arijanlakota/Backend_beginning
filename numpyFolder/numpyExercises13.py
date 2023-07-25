import numpy as np
#advanced numpy
# 1 arr1 = np.array([[1,2,4]])
# arr2 = np.array([1,5,6])
# print(np.dot(arr1,arr2))
#2
# arr1 = np.identity(3)
# print(np.vstack((arr1,arr1,arr1)))
# print(np.hstack((arr1,arr1,arr1)))
#3
# arr = np.random.random((4,4))
# print(arr)
# print(np.sum(arr,axis=1))
#4
# arr1 = np.random.random((3,3))
# print(arr1)
# print(np.subtract(arr1,np.mean(arr1,axis=0)))
#5
# arr = np.random.rand(3,3)
# sub_rows = np.mean(arr,axis=1,keepdims=True)
# print(arr - sub_rows)
#6
# arr = np.random.randn(5,5)
# print(np.divide(arr,np.linalg.norm(arr,axis=1)))
#7
# arr = np.random.randn(5,5)
# print(arr / np.linalg.norm(arr,axis=0))
#8
# arr = np.random.rand(3,3,3)
# print(np.sum(arr,axis=2))
#9
# arr = np.random.rand(5,5)
# print(np.sort(arr,axis=1))
#10
# arr = np.random.rand(5,5)
# print(np.sort(arr,axis=0))
#11
# nums = np.arange(25).reshape((5,5))
# second_largest = np.sort(nums,axis=1)[:,-2]
# print(second_largest)
#12
# nums = np.random.rand(5,5)
# second_largest = np.sort(nums,axis=0)[:,-2]
# print(second_largest)
#13
# arr = np.random.rand(5,5)
# print(arr)
# arr[np.where(arr == np.max(arr))] = 0
# print(arr)
#14
# arr = np.random.rand(5,5)
# print(arr)
# arr[np.where(arr == np.min(arr))] = 0
# print(arr)
#15
# arr = np.random.rand(5,5)
# print(np.exp(arr))




