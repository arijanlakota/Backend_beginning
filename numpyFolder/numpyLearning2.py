import numpy as np
arr = np.array([1,2,3,4],dtype="i4")
# print(arr.ndim)
# # print(arr.dtype)
# print(arr)
# print(arr.dtype)

#Converting type make a copy with astype
# newarr = arr.astype("S")
# newestarr = newarr.astype(bool)
# print(newestarr)
# print(newestarr.dtype)

#  copy not effected by changes
# x = arr.copy()
# arr[0] = 34
# print(arr)
# print(x)
# view is effected by changes
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)
# newarr = np.array([1,2,3,4],ndmin=5)
# print(newarr.shape)
#Reshaping an array(it's a view)
# newarr = np.array([1,2,3,4,5,6,7,8,9])
# newarr = newarr.reshape(3,3,1)
# print(newarr)
# print(newarr.base)
#iterating to high dimnesional array
# someArr = np.array([[[1,2,4],[2,2,5],[8,8,3]]])
# for i in np.nditer(someArr,flags=["buffered"],op_dtypes=["S"]):
#     print(i)
# someArr = np.array([[[1,2,4],[2,2,5],[8,8,3]]])
# for i in np.nditer(someArr[:,:,::2],flags=['buffered'],op_dtypes=["S"]):
#     print(i)
# someArr = np.array([[[1,2,4],[2,2,5],[8,8,3]]])
# for idx,x in np.ndenumerate(someArr):
#     print(idx,x)
# spliting array
# someArr = np.array([1,2,3,4,5,6])
# splitArr = np.array_split(someArr,4)
# print(splitArr)
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newArr = np.array_split(arr,3,axis=1)
# print(newArr)

#finding value
# arr = np.array([1,2,3,4,5,6,4,4])
# x = np.where(arr%2 == 0)
# print(x)
#filter value array
# arr = np.array([1,2,3,4])
# x = [True,False,True,False]
# newarr = arr[x]
# # print(newarr)
# arr = np.array([30,35,41,41,42,42,45,46,48])
# filetredArr = arr >= 42
# newArr = arr[filetredArr]
# print(newArr)