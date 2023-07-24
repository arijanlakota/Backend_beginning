import numpy as np
#1
# arr = np.array([[10 ,40],[30, 20]])
# print(np.sort(arr,axis=0))
# print(np.sort(arr,axis=1))
# print(np.sort(arr.flat))
#2
# arr = [(b'James', 5, 48.5 ), (b'Nail', 6, 52.5 ), (b'Paul', 5, 42.1 )
# ,(b'Pit', 5, 40.11)]
# data_types = [("name","S15"),("class",int),("height",float)]
# arr1 = np.array(arr,dtype=data_types)
# print(np.sort(arr1,order="height"))
#3
# arr = [(b'James', 5, 48.5 ) ,(b'Nail', 6, 52.5 ) ,(b'Paul', 5, 42.1 ), (b'Pit', 5, 40.11)]
# data_types = [("name","S15"),("class",int),("height",float)]
# arr1 = np.array(arr,dtype=data_types)
# print(np.sort(arr1,order=["class","height"]))
#4
# student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
# student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])
# print(np.lexsort((student_id,student_height)))
# for i in np.lexsort((student_id,student_height)):
#     print(student_id[i],student_height[i])
#5
# arr = np.array([1023 ,5202 ,6230 ,1671 ,1682 ,5241 ,4532])
# print(np.argsort(arr))
#6
# arr = np.array([(1+2j), (3-1j), (3-2j), (4-3j), (3+5j)])
# print(np.sort_complex(arr))
#7
# nums = np.array([70, 50, 20, 90, -11, 60, 50, 40])
# print(np.partition(nums, 4))
#8
# arr = np.array([0.39536213, 0.11779404 ,0.32612381, 0.16327394 ,0.98837963 ,0.25510787, 0.01398678 ,0.15188239, 0.12057667 ,0.67278699])
# print(arr[np.argpartition(arr,range(5))])
#9
# arr = np.array([[1 ,5 ,0],[3, 2 ,5],[8, 7 ,6]])
# k = 2
# arr1 = np.array(arr[:,k-1])
# print(arr[np.argsort(arr[:,k-1])])