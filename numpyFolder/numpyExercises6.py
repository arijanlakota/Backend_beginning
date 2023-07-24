import numpy as np
#173
# arr = np.ones((8,8,8))
# print(np.triu(arr,1))
#174
# arr = np.arange(1,13,dtype='i8').reshape((3,4))
# print(arr.ndim)
# print(arr.size)
# print(arr.itemsize)
#175
# arr = np.arange(0,39,2)
# print(arr.reshape((5,4)))
# print(arr.reshape(-1))
#176
# arr = np.arange(20).reshape((4,5))
# arr[:,[0,3]] = arr[:,[3,0]]
# print(arr)
#177
# arr = np.arange(20).reshape((4,5))
# arr[:] = arr[3::-1]
# print(arr)
#178
# arr1 = np.arange(20).reshape((4,5))
# arr2 = np.array([[ 1., 2., np.nan],[ 4., 5., 6.],[np.nan, 7., np.nan]])
# arr2[np.isnan(arr2)] = np.mean(arr1)
# print(arr2)
#179
# arr = np.arange(20).reshape((4,5))
# print(arr[(arr > 6)&(arr % 3 == 0)])
#180
# arr1 = np.arange(20).reshape((4,5))
# arr2 = np.arange(20).reshape((5,4))
# if(arr1.shape == arr2.shape):
#     print(True)
# else:
#     print(False)
#with unfunc
# def isSameDimension(a,b):
#     try:
#         a+b
#     except ValueError:
#         print("Not same")
#     else:
#         print("same")
# isSameDimension = np.frompyfunc(isSameDimension)
#181
# from time import sleep
# arr = np.zeros((4,4))
# sleep(np.random.randint(1,5))
# arr[np.random.randint(1,4),np.random.randint(1,4)] = np.random.randint(1,16)
# print(arr)
#182
# arr = np.array([[0.59243452, 0.51883289, 0.03732848, 0.49544926 ,0.22637201 ,0.45750412,0.81614237, 0.86681236, 0.95482226 ,0.54789281],[0.14428353 ,0.20556412 ,0.97059136, 0.53545871, 0.93828877, 0.81535277,0.60563373 ,0.47543413, 0.0468766, 0.97460889]])
# arr[:] = arr[:] - np.mean(arr,axis=1,keepdims=True)
# print(arr)
#183
# arr = np.array([[1,0,2],[2,0,2]])
# if np.all(arr[:,::]) == 0:
#     print(True)
# else:
#     print(False)
#184
# arr = np.random.randint(15,size=15)
# print(arr)
#185
# arr = np.array([1 ,2, 3 ,4 ,5 ,6 ,7 ,8])
# num_zeroes = np.zeros(len(arr) + 2*(len(arr)-1))
# num_zeroes[::3] = arr
# print(num_zeroes)
#186
# arr1 = np.ones((2,2,3))
# arr2 = np.array([1,2,3,4]).reshape((2,2))
# print(()?
#187
# arr = np.array([ 0 ,1 ,3 ,5 ,7, 9 ,11 ,13 ,15])
# arr1 = []
# for i in arr:
#     arr1.append([np.binary_repr(i,width=9)])
# arr1 = np.asarray(arr1)
# print(arr1)
#188
# arr = np.array([1,2,3,2,2,3,4,5,6,2,3,4,1,2,2,2,1,1,1,1,1,1,1,2,2,2,2,3,3,3]).reshape((10,3))
# new_nums = np.logical_and.reduce(arr[:,1:] == arr[:,:-1], axis=1)
# arr = arr[~new_nums]
# print(arr)
#189
# nums1 = np.random.randint(0,6,(6,4))
# nums2 = np.random.randint(0,6,(2,3))
# print(nums1[np.in1d(np.unique(nums2.flat),nums1[:])])
#190
# arr = np.array([['Yasemin Rayner' ,'88.5', '90'],
# ['Ayaana Mcnamara', '87', '99'],
# ['Jody Preece', '85.5' ,'91']])
# print(np.core.records.fromarrays(arr.T,names='col1, col2, col3',formats = 'S80, f8, i8'))
#191
# arr =np.ones((25,25))
# arr.reshape(-1,5,5)
# arr[:] = np.sum(arr)
# print(arr)
#192
# arra1 = np.random.randint(0,5,(12,12))
# print(arra1)
# n = 4
# i = 1 + (arra1.shape[0]-4)
# j = 1 + (arra1.shape[1]-4)
# result = np.lib.stride_tricks.as_strided(arra1, shape=(i, j, n, n), strides = arra1.strides + arra1.strides)
# print(result)
#193
# import time
# start_time = time.perf_counter()
# a = np.ones(10000)
# end_time = time.perf_counter()
# print(end_time - start_time)
#194
# arr1 = np.random.randint(256,size=(300,400,5))
# arr2 = np.random.randint(256,size=(300,400,5))
# print(np.stack((arr1,arr2)))
#195
# arr1 = np.random.randint(5,size=(1,3,4))
# print(arr1.shape)
#196
# arr = np.random.rand(12,12,4)
# print(arr[:6, :6, :])
#197
# arr1 = np.array([[4.5, 3.5],[5.1 ,2.3]])
# arr2 = np.array([[1],[2]])
# print(np.concatenate((arr1,arr2),axis=1))
#198
# arr = np.random.rand(10,4)
# np.set_printoptions(precision=4)
# print(arr)
#199
# arr = np.array([1.2e-07 ,1.5e-06, 1.7e-05])
# np.set_printoptions(suppress=True)
# print(arr)
#200
# arr1 = np.random.rand(5,7)
# print(arr1)
# k=3
# print(np.delete(arr1,k,1))
#201
# arr = np.random.randint(10,size=(90,30))
# print(arr)
# np.append(arr,values=np.random.randint(10,size=(10)))
# np.set_printoptions(edgeitems=10)
# print(arr)
#202
# arr1 = np.array([[2 ,5 ,2],
# [1 ,5 ,5]])
# arr2 = np.array([[5, 3, 4],
# [3 ,2 ,5]])
# print((arr1+arr2)/2)
#203
# arr = np.array([['stident_id', 'Class', 'Name'],
# ['01' ,'V' ,'Debby Pramod'],
# ['02' ,'V', 'Artemiy Ellie'],
# ['03' ,'V' ,'Baptist Kamal'],
# ['04' ,'V' ,'Lavanya Davide'],
# ['05' ,'V' ,'Fulton Antwan'],
# ['06' ,'V' ,'Euanthe Sandeep'],
# ['07' ,'V' ,'Endzela Sanda'],
# ['08' ,'V' ,'Victoire Waman'],
# ['09' ,'V' ,'Briar Nur'],
# ['10' ,'V', 'Rose Lykos']])
# np.random.shuffle(arr[2:5])
# print(arr)
#204
# arr = np.array([['01' ,'V' ,'Debby Pramod'],
# ['02' ,'V' ,'Artemiy Ellie'],
# ['03' ,'V', 'Baptist Kamal'],
# ['04' ,'V' ,'Lavanya Davide'],
# ['05' ,'V', 'Fulton Antwan'],
# ['06' ,'V' ,'Euanthe Sandeep'],
# ['07' ,'V', 'Endzela Sanda'],
# ['08' ,'V' ,'Victoire Waman'],
# ['09' ,'V', 'Briar Nur'],
# ['10' ,'V' ,'Rose Lykos']])
# for i in (arr[:,[-1]].reshape(-1)):
#     if i[0].lower() == "e":
#         print(i)
#205
# arr = np.array([['01' ,'V' ,'Debby Pramod', '30.21'],
# ['02' ,'V' ,'Artemiy Ellie' ,'29.32'],
# ['03' ,'V' ,'Baptist Kamal', '31.0'],
# ['04' ,'V' ,'Lavanya Davide', '30.22'],
# ['05' ,'V' ,'Fulton Antwan' ,'30.21'],
# ['06' ,'V' ,'Euanthe Sandeep', '31.0'],
# ['07' ,'V' ,'Endzela Sanda' ,'32.0'],
# ['08' ,'V' ,'Victoire Waman' ,'29.21'],
# ['09' ,'V' ,'Briar Nur' ,'30.0'],
# ['10' ,'V' ,'Rose Lykos' ,'32.0']])
# result = np.char.startswith(arr[:,2],"E")
# new_arr = arr[result][:,3].astype(float)
# print(np.sum(new_arr))



