import numpy as np
#29
# arr = np.array([[4,6],[2,1]])
# print(np.sort(arr,axis=0))
# print(np.sort(arr,axis=1))
#30
# first_names =    ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')
# last_names = ('Woolum', 'Battle', 'Plotner', 'Brien', 'Stahl')
# x = np.lexsort((first_names, last_names))
# print(x)
#31
# arr = np.array([[ 0 ,10 ,20],[20 ,30, 40]])
# print(np.argwhere(arr > 10))
#32
# arr = np.arange(1,11)
# np.savetxt("text.out",arr)
#33
# arr = np.zeros((4,4))
# print(arr.size * arr.itemsize)
#34
# arr = np.ones((4,4),dtype='i')
# print(arr)
#35
# arr = np.arange(1,10).reshape((3,3))
# print(arr)
#36
# arr = np.array([[10, 20, 30],
# [20, 40 ,50]])
# print(arr.reshape(-1))
#37
# arr = np.zeros((2,3),dtype='i4')
# print(arr.dtype)
# print(arr)
# print(arr.shape)
#38
# arr = np.array([[1, 2],
# [3 ,4],
# [5 ,6]])
# print(arr.reshape(2,3))
#39
# arr  = np.array([[ 2 ,4 ,6],
# [ 6 ,8 ,10]])
# arr1 = arr.astype(float)
# print(arr1)
#40
# arr = np.full((3,5),2)
# print(arr)
#41
# x = np.arange(4, dtype=np.int64)
# print(np.full_like(x,10))
#42
# arr = np.eye(3)
# print(arr)
#43
# arr = np.diagflat([4,5,6,8])
# print(arr)
#44
# arr1 = np.arange(0,50)
# arr2 = np.arange(10,50)
# print(arr1,arr2)
#45
# arr = np.linspace(2.5,6.5,30)
# print(arr)
#46
# arr = np.logspace(2,5,20)
# print(arr)
#47
# x = np.tri(4,3,-1)
# print(x)
#48
# arr = np.arange(2,14).reshape((4,3))
# print(np.triu(arr,-1))
#49
# arr = np.zeros((3,3,3))
# print(arr.reshape(-1))
#50
# arr = np.array([[2,4,6],[6,8,10]])
# print(arr.flat[3])
#51
# arr = np.array([[1,2,3]])
# print(np.swapaxes(arr,axis1=0,axis2=1))
#52
# x = np.zeros((2, 3, 4))
# print(np.moveaxis(x, 0, -1).shape)
#53
# arr = np.zeros((2,3,4,5))
# print(np.moveaxis(arr,3,1).shape)
#54
# arr = np.atleast_1d(12)
# print(arr)
#55
# arr1 = np.atleast_2d(12)
# arr2 = np.atleast_3d(12)
# print(arr1,arr2)
#56
# arr = np.zeros((3,4))
# print(np.expand_dims(arr,1).shape)
#57
# arr = np.zeros((3,1,4))
# print(np.squeeze(arr))
#58
# print(np.concatenate(([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]])))
#59
# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# print(np.column_stack((arr1,arr2)))
#60
# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# print(np.dstack((arr1,arr2)))
#61
# arr = np.arange(1,15)
# print(np.split(arr,[2,6]))
#62
# arr = np.arange(16).reshape((4,4))
# print(np.array_split(arr,2,axis=1))
#63
# arr = np.array([[ 0 ,10 ,20],[20 ,30 ,40]])
# print(np.size(arr[arr!=0]))
#64
# arr = np.zeros((5,5))
# arr[:] = np.arange(0,5)
# print(arr)
#65
# arr = np.array([[1,4,7],[5,4,4],[2,9,4]])
# print(np.in1d(arr,4))
#66
# arr = np.linspace(0,1,12,endpoint=True)[1:-1]
# print(arr)
#67
# arr = np.array([1,2,3,4])
# arr.flags.writeable = False
#68
# arr = np.arange(1,100)
# arr1 = arr[(arr % 3 == 0) | (arr % 5 == 0)]
# print(arr1.sum())
#69
# arr = np.arange(1,1000)
# print(arr)
#70
# arr = np.arange(1,11)
# for i in np.nditer(arr):
#     print(i,end=" ")
#71
# arr = np.arange(1,11).reshape(2,5)
# for i in np.nditer(arr,order="F"):
#     print(i)
#72
# print(np.ones((5,5,5)))
#73
# arr = np.arange(1,13).reshape(3,4)
# print(arr*3)
#74
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([[1,2,3,4],[5,6,7,8]])
# for i,j in np.nditer([arr1,arr2]):
#     print("%d:%d" % (i,j),)
#75
# x = np.zeros((3,), dtype=('i4,f4,a40'))
# print(x)
#76
# arr = np.array([1,2,3])
# print(np.power(arr,3))
#77
# arr = np.array([[ 0 ,1 ,2 ,3],[ 4 ,5 ,6 ,7],[ 8 ,9 ,10 ,11]])
# for a in np.nditer(arr, flags=['external_loop'], order='F'):
#     print(a)
#78
# a = np.array([1,2,3,4])
# b = np.array(['Red', 'Green', 'White', 'Orange'])
# c = np.array([12.20,15,20,40])
# for i in np.nditer(np.vstack((a,b,c)),order="F"):
#     print(i)
#79
# arr = np.random.randn(100).reshape(25,4)
# print(arr)
#80
# arr = np.array([1,2,3,4])
# print(arr.tolist())
#81
# arr = np.arange(1,7).reshape(3,2)
# for i in arr:
#     print(i)
#82
# arr  = np.array([[ 12. ,12.51],[ 2.34 ,7.98],[ 25.23 ,36.5 ]])
# print(np.floor(arr))
#83
# arr = np.array([ 0.26153123, 0.52760141, 0.5718299 ,0.5927067 ,0.7831874, 0.69746349,
# 0.35399976 ,0.99469633 ,0.0694458 ,0.54711478])
# np.set_printoptions(precision=3)
# print(arr)
#84
# x=np.array([1.6e-10, 1.6, 1200, .235])
# np.set_printoptions(suppress=True)
# print(x) 
#85
# iteratora = (x for x in range(10))
# arr = [np.fromiter(iteratora,dtype=int)]
# print(arr)
#86
# arr1 = np.array([[10,20,30], [40,50,60]])
# arr2 = np.array([[100], [200]])
# print(np.append(arr1, arr2, axis=1))
#87
# arr = np.array([[10,11],[10,11],[5,18],[7,4],[5,18],[7,2],[7,4]])
# y = np.ascontiguousarray(arr).view(np.dtype((np.void,arr.dtype.itemsize * arr.shape[1])))
# _,idx = np.unique(y, return_index=True)
# print(arr[idx])
#88
# arr = np.array([[ 0.42436315, 0.48558583, 0.32924763],
# [ 0.7439979 ,0.58220701 ,0.38213418],
# [ 0.5097581 ,0.34528799 ,0.1563123 ]])
# print(arr[arr>0.5])
#89
# arr = np.array([ 10, 20 ,30 ,40 ,50 ,60 ,70 ,80 ,90 ,100])
# print(np.delete(arr,[0,3,4]))
#90
# arr = np.array([-1 ,-4 ,0 ,2 ,3 ,4 ,5 ,-6])
# arr[arr < 0] = 0
# print(arr)
#91
# arr = np.array([[ 1., 2., 3.],[ 4., 5., np.nan],[ 7., 8., 9.],[ 1., 0., 1.]])
# print(arr[~np.isnan(arr).any(axis=1)])
#92
# a = np.array([97, 101, 105, 111, 117])
# b = np.array(['a','e','i','o','u'])
# for i,j in np.nditer((a,b)):
#     if 100<i<110:
#         print(j)
#93
# arr = np.arange(1,6)
# print(np.sqrt(np.power(arr,2).sum()))
# print(np.linalg.norm(arr))
#94
# arr = np.array([10 ,10 ,20 ,10 ,20 ,20 ,20 ,30 ,30 ,50 ,40 ,40])
# return_elements,count_elements = np.unique(arr,return_counts=True)
# print(np.asarray((return_elements,count_elements)))
#95
# arr = np.array([])
# print(np.size(arr))
#96
# v = np.array([20 ,30, 40])
# arr = np.array([[20, 20, 20],
# [30 ,30 ,30],
# [40, 40, 40]])
# print(arr/v)
#97
# print(np.zeros(4))
#98
# arr =  np.array([ 10 ,20 ,30],float)
# arr1 = _+?
# print(arr1)
#99
# arr = np.array([ 10. ,20. ,30.])
# print(np.sum(arr),np.product(arr))
#100
# arr1 = np.array([ 10. ,10. ,20. ,30. ,30.])
# arr2 = np.array([0,40])
# arr1.put([0,4],arr2)
# print(arr1)
