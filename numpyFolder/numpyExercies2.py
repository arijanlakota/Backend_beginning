import numpy as np
#31
# arr = np.random.random((3,3,3))
# print(arr)
# #32
# arr = np.random.random((3,2))
# print(arr)
# print(np.sum(arr))
# print(np.sum(arr,axis=1))
# print(np.sum(arr,axis=0))
# #33
# arr1 = np.array([1,23,4,2,4])
# arr2 = np.array([3,0,2,3,5])
# print(np.dot(arr1,arr2))
#34
# x = np.arange(1,26).reshape((5,5))
# print(x)
# v = np.array([1,1,1,1,1])
# k = x.copy()
# for i in range(len(x)):
#     k[i,:] = x[i,:] + v[i]
# print(k)
# print(x)
#35
# s = np.array([1,2,3,4,5])
# np.save(arr=s,file="be")
#37
# x = np.array([2,3,4,1,0])
# np.savetxt(fname="nesto.txt",X=x)
# result = np.loadtxt("nesto.txt")
# print(result)
#38
# arr = np.array([1,2,3,4,6])
# arr1 = arr.tobytes()
# print(arr1)
# arr2 = np.frombuffer(arr1,dtype=arr.dtype)
# print(arr2)
#39
# a = [1,2,3,4,5]
# arr = np.array(a)
# arr1 = arr.tolist()
# if a == arr1:
#     print(True)
#40
# import matplotlib.pyplot as plt
# a = np.arange(0,3*np.pi,0.2)
# y = np.sin(a)
# plt.plot(a,y)
# plt.show()
#41
# arr = np.float32(0)
# a = arr.item()
# print(type(arr))
# print(type(a))
#42
# arr = np.array([[1,2,4],[2,0,5],[0,2,3]])
# element = 5
# t = []
# for y,x in np.ndenumerate(arr):
#     if x == 0:
#         t.append(y[0])
#     if t != []:
#         if y[0] == t[len(t) - 1]:
#             continue
#     arr[y] += element
# print(arr)
#43
# arr = np.array([[1,2,3,np.nan],[1,2,3,np.nan],[np.nan,2,np.nan,7],[1,np.nan,3,np.nan]])
# print(np.isnan(arr))
#44
# arr1 = np.array([1,2,3,4.000001,5])
# arr2 = np.arange(1,6)
# np.set_printoptions(precision=10)
# print(np.equal(arr1,arr2))
# print(arr1 == arr2)
#45
# arr = np.arange(10,1000)
# print(arr)
#46
# arr = np.random.random((3,2,1))
# print(arr)
#47
import matplotlib.pyplot as plt
import seaborn as sns
# arr = np.random.uniform(size=40)
# print(arr)
# sns.displot(arr,kind="kde")
# plt.show()
#48
# arr = np.random.normal(loc=200,scale=7,size=40).reshape(8,5)
# sns.displot(arr,kind="kde")
# print(arr)
# plt.show()
#49
# arr1 = np.array([2,3,7,56,23,45,20])
# arr2 = np.random.choice(arr1,5,p=[0.1,0.2,0.05,0.15,0.3,0.1,0.1])
# sns.displot(arr2,kind="kde")
# plt.show()
# #50
# arr = np.random.random((4,4))
# arr1 = arr.copy()
# temp = arr[0]
# arr1[0] = arr1[-1]
# arr1[-1] = temp
# print(temp)
# print(arr)
# print(arr1)
# #51
# arr1 = np.zeros(30).reshape(5,6)
# print(arr1)
# arr1[::2,::2] = 3
# arr1[1:-1:2,1::2] = 7
# print(arr1)
#52
# arr = np.array([[6,3,1],[0,5,1],[2,0,7],[1,4,6],[8,0,5]])
# print(np.sort(arr))
# print(np.sort(arr,axis=0))
#53
# target = 5
# arr = np.array([0,6,7,2,20,3,8,34,4,3,5,5,5,2,5,6,0,2,1,9])
# a = arr != target
# print(arr[a])
#54
# arr = np.array([0,6,7,2,20,3,8,34,4,3,5,5,5,2,5,6,0,2,1,9])
# n = 5
# r = 44
# arr1= arr.view()
# arr1[arr>n] = r
# print(arr)
# arr1[arr<n] = r
# print(arr)
# arr1[arr==n] = r
# print(arr)
#56
# a = np.arange(1,61).reshape(3,5,4)
# print(a)
#57
# arr = np.arange(16).reshape((4,4))
# print(arr)
# arr1 = arr.copy()
# col1 = arr[:,0]
# col2 = arr[:1]
# arr1[:,0] = arr1[:,-1]
# arr1[:,1] = arr1[:,2]
# arr1[:,-1] = col1
# arr1[:,2] = col2
# print(arr1)
#58
# arr = np.arange(16).reshape(4,4)
# print(arr[::-1,::-1])
#59
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([6,7,8,9,10])
# print(np.multiply(arr1,arr2))
