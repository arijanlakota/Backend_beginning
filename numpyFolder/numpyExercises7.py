import numpy as np
#linear algebra
#1
# arr1 = np.array([[1,2,3],[1,2,3]])
# arr2 = np.array([[2,2,3],[1,5,4]])
# print(np.multiply(arr1,arr2))
#2
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([0,2,1,2,0])
# print(np.outer(arr1,arr2))
#3
# arr1 = np.array([[1,2],[2,4]])
# arr2 = np.array([[1,2],[2,5]])
# print(np.cross(arr1,arr2))
#4
# arr = np.array([[1,0,9],[1,2,4],[1,10,3]])
# print(np.linalg.det(arr))
#5
# arr1 = np.array([[2,33,4],[2,12,9],[7,0,2]])
# arr2 = np.array([[1,2,1],[7,0,2],[7,0,2]])
# print(np.einsum("mk,kn",arr1,arr2))
#6
# arr1 = np.array([[1,2,3]])
# arr2 = np.array([[0,2,0]])
# print(np.inner(arr1,arr2))
#7
# arr = np.full((3,3),3)
# print(np.linalg.eig(arr))
# print(np.linalg.eigvals(arr))
#8
# arr1 = np.arange(12).reshape((3,4))
# arr2 = np.arange(5,17).reshape((3,4))
# print(np.kron(arr1,arr2).shape)
#9
# arr = np.array([[1,2,4],[2,2,7],[1,9,0]])
# print(np.linalg.cond(arr))
#10
# arr = np.arange(100).reshape((-1,4))
# print(np.linalg.norm(arr))
#11
# arr = np.array([[10,11,12],[10,11,12],[10,11,12]])
# print(np.linalg.det(arr))
#12
# m = np.array([[1,2],[3,4]])
# print(np.linalg.inv(m))
#13
# arr = np.array([[10,12,20],[11,5,6]])
# print(np.linalg.qr(arr))
#14?
#15
# arr = np.arange(100).reshape((10,10))
# print(np.diag(arr).sum())
#16
# arr = np.array([[4, 12, -16], [12, 37, -53], [-16, -53, 98]], dtype=np.int32)
# print(np.tril(np.linalg.cholesky(arr)))
#17?
#18
# arr = np.array([[10,19,12],[9,11,3],[14,6,5]])
# print(np.linalg.svd(arr))
#19
# arr = np.array([[10,19,12],[9,11,3],[14,6,5]])
# print(np.linalg.norm(arr,ord="fro"))


