import numpy as np
#102
# arr = np.arange(6)
# np.savetxt("test.csv", arr, delimiter=",")
#103
# arr = np.array([[3,4],[1,2]])
# print(np.linalg.norm(arr))
#104
# arr = np.array([[1 ,2 ,3],[4 ,5 ,6],[7 ,8 ,9],[2 ,3,7],[5, 6,7],[8,7, 9]],dtype=object)
# print(arr[:,-2:])
#105
# arr = np.loadtxt("test.csv",dtype="i")
# print(arr)
#106
# arr = np.array([10 ,20 ,20 ,20 ,20 ,0 ,20 ,30 ,30 ,30 ,0 ,0 ,20 ,20 ,0])
# for a in np.unique(arr,return_counts=True):
#     print(a)
#107
# arr = np.arange(1,6)
# print(np.percentile(arr,50))
#108
from PIL import Image 
# image = Image.open('')
# arr = np.asarray(image)
#109
# arr = np.zeros((200,200,3),dtype=np.uint8)
# img = Image.fromarray(arr,"RGB")
# img.save("test.png")
# img.show()
#110
# arr = np.array([200., 300., np.nan, np.nan, np.nan, 700.])
# print(arr[~np.isnan(arr)])
#111
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(np.transpose([np.tile(arr1,len(arr2)),np.repeat(arr2,len(arr1))]))
#112
# from sys import getsizeof
# arr = np.arange(1,11)
# print(getsizeof(arr))
#113
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4,5])
# arr3 = np.array([6,7])
# resultArr = np.array(np.meshgrid(arr1,arr2,arr3)).T.reshape((-1,3))
# print(resultArr)
#114
# arr = np.random.randint(10,size=(10,5))
# print(arr)
#115
# arr = np.array([1,0,0,0,3,0,3,2,4,0,4,0,4,6,8,0])
# print(np.argwhere(arr == 0).reshape(-1))
#116
# import seaborn as sns
# import matplotlib.pyplot as plt
# arr = np.random.logistic(scale=70,loc=10,size=1000)
# sns.displot(arr,kind="hist")
# plt.show()
#117
# import matplotlib.pyplot as plt
# arr = np.random.randint(1, 50, 10)
# y, x = np.histogram(arr, bins=np.arange(51))
# fig, ax = plt.subplots()
# ax.plot(x[:-1], y)
# fig.show()
#118
# arr = np.arange(-6,6)
# n = 4
# print(len(np.where(arr > n)[0]))
#119
# arr2 = np.array([],dtype='i')
# print(np.append(values=[1,2,3,4,5],arr=arr2))
#120
# arr = np.arange(1,13).reshape((2,6))
# print(np.argmax(arr,axis=1))
# np.unravel_index()
#121
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(np.stack((arr1,arr2),axis=0))
#122
# arr = np.arange(16).reshape((4,4))
# print(arr[[0,1,2],[0,1,3]])
#123
# arr = np.arange(16).reshape(4,4)
# arr = np.resize(arr,(2,2))
# print(arr)
# arr = np.resize(arr,(6,6))
# print(arr)
#124
# arr1 = np.array([[0, 0, 0],[1 ,2 ,3],[4 ,5, 6]])
# arr2 = np.array([10,11,12])
# arr1[::] += arr2
# print(arr1)
#125
# arr1 = np.array([[ 0],
# [10],
# [20]])
# arr2 = np.array([10,11,12])
# print(arr1 + arr2)
#126
# arr = np.arange(24).reshape(6,4)
# print(np.swapaxes(arr,axis1=0,axis2=1))
#127
# arr1 = np.array([[0, 1 ,2],
# [3, 4 ,5],
# [6 ,7, 8]])
# arr2 = np.array([[ 0, 3, 6],
# [ 9 ,12, 15],
# [18 ,21 ,24]])
# print(np.hstack((arr1,arr2)))
#128
# arr1 = np.array([[0, 1 ,2],
# [3, 4 ,5],
# [6 ,7, 8]])
# arr2 = np.array([[ 0, 3, 6],
# [ 9 ,12, 15],
# [18 ,21 ,24]])
# print(np.vstack((arr1,arr2)))
#129
# arr1 = np.array([1,2,3])
# arr2 = np.array([2,3,4])
# print(np.stack((arr1,arr2),axis=1))
#130
# arr1 = np.array([1,2,3])
# arr2 = np.array([2,3,4])
# print(np.stack((arr1,arr2),axis=0))
#131
# arr = np.arange(16).reshape((4,4))
# print(np.array_split((arr),4))
#132
# arr = np.array([[[ 0., 1. ,2., 3.],
# [ 4., 5., 6., 7.]],
# [[ 8., 9., 10., 11.],
# [12., 13., 14., 15.]]])
# print(np.dsplit(arr,2))
#133
# arr = np.arange(24).reshape((2,12))
# print(arr.ndim)
# print(arr.size)
# print(arr.itemsize)
#134
# arr = np.arange(16).reshape((4,4))
# print(arr[0])
#135
# arr = np.arange(16).reshape((4,4))
# print(arr[1])
#136
# arr = np.arange(16).reshape((4,4))
# print(arr[:,2])
#137
# arr = np.arange(16).reshape((4,4))
# print(arr[:2,:2])
#138
# arr = np.arange(16).reshape((4,4))
# print(arr[:2,2:])
#139
# arr = np.arange(16).reshape((4,4))
# print(arr[::2,::2])
#140
# arr = np.arange(16).reshape((4,4))
# print(arr[1::2,1::2])
# 141
# arr = np.arange(16).reshape((4,4))
# print(arr[:,1:3])
# 142
# arr = np.arange(16).reshape((4,4))
# print(arr[:,::3])
#143
# arr = np.arange(16).reshape((4,4))
# print(arr[1,0],arr[3,3])
#144
# arr = np.arange(16).reshape((4,4))
# print(arr[1:3,1:3])
#145
# arr = np.arange(36).reshape((6,6))
# print(arr[2::2,::2])
#146
# arr = np.arange(36).reshape((6,6))
# print(arr[2::2,::2])
#147
# arr1 = np.ones((3,3))
# arr2 = np.arange(3)
# print(arr1 + arr2)
#148
# arr1 = np.array([12,23,4,1,55])
# arr2 = arr1.copy()
# print(arr2)
#149
# a = np.array([1, 3, 7, 9, 10, 13, 14, 17, 29])
# result = np.where(np.logical_and(a>=7, a<=20))
# print(a[result])
#150
# arr = np.arange(12).reshape((4,3))
# arr1 = arr.view()
# temp = arr[:,0]
# arr1[:,0] = arr[:,1]
# arr1[:,1] = temp
# print(arr1)
#151
# arr = np.arange(36).reshape((4,9))
# print(np.where(np.any(arr>10,axis=1)))
#152
# arr = np.arange(36).reshape((4,9))
# print(np.sum(arr,axis=0))
#153
# arr = np.arange(18).reshape((6,3))
# print(arr[np.triu_indices(3)])
#154
# result  = np.triu([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1)
# print(result)
#155
# arr = np.arange(25).reshape((5,5))
# v = np.array([ 5 ,6 ,7 ,8 ,9])
# for i in arr:
#     if v.tolist() == i.tolist():
#         print(True)
#156
# arr = np.array([[10., 20. ,30.],
# [40., 50. ,np.nan],
# [np.nan ,6., np.nan],
# [np.nan, np.nan, np.nan]])
# for i in arr[~np.isnan(arr)]:
#     print(np.average(i))
#157
# arr = np.array([ 1 ,2 ,3 ,2 ,4 ,6 ,1 ,2 ,12 ,0 ,-12 ,6])
# print(np.mean(arr.reshape(3,4),axis=0))
#158
# arr1= np.array([[0, 1], [2, 3]])
# arr2 = np.array([[4, 5], [0, 3]])
# print(np.average((arr1,arr2),axis=1))
#159
# arr = np.array([[ 11, 22, 33, 44, 55],
# [ 66 ,77 ,88 ,99 ,100]])
# i = [1,3,0,4,2]
# result = arr[:,i]
# print(result)
#160
# arr = np.array([ 1., 7. ,8. ,2. ,0.1 ,3. ,15. ,2.5])
# print(np.sort(arr)[:4])
#161
# a = np.full((512, 256, 3), 255, dtype=np.uint8)
# image = Image.fromarray(a, "RGB")
# image.save("white.png", "PNG")
#162
# a = np.random.randint(0, 10, (3, 4, 8))
# tidx = np.random.randint(0, 3, 4)
# print(a[tidx, np.arange(len(tidx)),:])
#163
# arr1 = np.array([ 10 ,-10 ,10 ,-10 ,-10 ,10])
# arr2 = np.array([0.85, 0.45, 0.9 ,0.8, 0.12 ,0.6 ])
# print(np.where((arr1 == 10 & (arr2 >0.5))))
#164
# arr = np.array([[1, 0, "aaa"],
# [0 ,1, "bbb"],
# [0 ,1 ,"ccc"]])
# np.savetxt("text.txt",arr,fmt="%s")
#165
# arr1 = np.arange(10).reshape((2,5))
# arr2 = np.arange(10).reshape((2,5))
# arr3 = np.arange(10).reshape((2,5))
# print(np.meshgrid((arr1,arr2,arr3)))
#166
# array1 = ['PHP','JS','C++']
# array2 = ['Python','C#', 'NumPy']  
# result  = np.r_[array1[:-1], [array1[-1]+array2[0]], array2[1:]]
#167
# thisDict = {'column0': {'a': 1, 'b': 0.0, 'c': 0.0, 'd': 2.0},
# 'column1': {'a': 3.0, 'b': 1, 'c': 0.0, 'd': -1.0},
# 'column2': {'a': 4, 'b': 1, 'c': 5.0, 'd': -1.0},
# 'column3': {'a': 3.0, 'b': -1.0, 'c': -1.0, 'd': -1.0}}
# arr = np.asarray(thisDict)
# print(arr)
#168
# import pandas as pd
# arr = np.array([[0.02482073, 0.02318678, 0.36032194],
# [0.69001834 ,0.04285817, 0.31768865]])
# print(pd.DataFrame(arr))
#169
# arr = np.arange(60).reshape((3,5,-1))
# result = np.diagonal(arr, axis1=1, axis2=2)
# print(result)
#170
# arr = np.arange(6,dtype='i4').reshape((2,3))
# print(repr(arr).count("1, 2"))
#171
# arr = np.arange(1,13).reshape(4,3)
# print(np.where((arr == [4,5,6]).all(1))[0])
#172
# arr1 = np.array([])
# arr2 = np.array([[ 1, 1, 0],
# [ 0 ,0 ,0],
# [ 0, 2 ,3],
# [ 0 ,0, 0],
# [ 0 ,-1 ,1],
# [ 0 ,0 ,0]])
# for i in arr2:
#     if i.tolist() not in arr1.tolist():
#         np.append(arr1,values=i)
#     print(i.tolist())
#     print(arr1.tolist())
# print(arr1)?




