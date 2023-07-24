import numpy as np
#statistics
#1
# arr = np.array([[0 ,1],[2 ,3]])
# print(np.amax(arr))
# print(np.amin(arr))
#2
# arr = np.array([[0 ,1],[2 ,3]])
# print(np.amax(arr,axis=1))
# print(np.amin(arr,axis=1))
#3
# arr = np.arange(12).reshape(2,-1)
# print(np.subtract(np.amax(arr,axis=1),np.amin(arr,axis=1)))
#4
# arr = np.arange(12).reshape((2,6))
# print(np.percentile(arr,80,axis=1))
#5
# arr =  np.arange(12).reshape((2,6))
# print(np.mean(arr))
#6
# arr = np.arange(5)
# weights = np.arange(1,6)
# print(np.average(arr,weights=weights))
# r2 = (arr*(weights/weights.sum())).sum()
# print(r2)
#7
# arr = np.arange(6)
# print(arr.mean())
# print(arr.std())
# print(arr.var())
#8
# arr1 = np.array([0 ,1 ,2])
# arr2 = np.array([2 ,1 ,0])
# print(np.cov(arr1,arr2))
#9
# arr1 = np.array([0 ,1 ,3])
# arr2 = np.array([2,4,5])
# print(np.correlate(arr1,arr2,"valid"))
#10
# arr1 = np.array([0, 1 ,3])
# arr2 = np.array([2,4,5])
# print(np.corrcoef(arr1,arr2))
#11
# print(np.isfinite(1))
# print(np.isfinite(0))
# print(np.isfinite(np.nan))
# print(np.isinf(np.inf))
# print(np.isinf(np.nan))
# print(np.isinf(np.NINF))
#12
# arr = np.arange(9).reshape((3,3))
# print(np.average(arr,axis=1 ,weights=[1./4, 2./4, 2./4]))
#13
# arr = np.array([0, 1, 6, 1, 4, 1, 2, 2, 7])
# print(np.bincount(arr))
# #14
# arr = np.array([0.5, 0.7 ,1. ,1.2 ,1.3 ,2.1])
# bins = np.arange(5)
# import matplotlib.pyplot as plt
# plt.hist(arr,bins=bins)
# plt.show()


