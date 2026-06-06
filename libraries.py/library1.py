# features of numpy
# speed,uses low memory,easy math operations,used in data science/ML/AI
# when working with large datasets, numpy is used

import numpy as np
# l = [1, 2, 3, 4]
# arr = np.array(l)
# print(arr)
# print('list multiplication:',2*l)
# print('array multiplication:',2*arr)

# creating array from scratch
# zeros=np.zeros((3,4))
# print('zeros array:\n',zeros)

# ones=np.ones((3,4))
# print('\nones array:\n',ones)

# full=np.full((4,6),9)
# print('\nfull arrays:\n',full)

# matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix)

# creating sequence of no
# arr=np.arange(1,10,1) # similar to range in python
# print(arr)

# creating identity matrices
# identity_matrix=np.eye(4,5,5,) # takes either one-three arguments
# print(identity_matrix)


# properties of numpy arrays

# 1 checking shape,size,type,no of dimensions(note:shape=no of row and column)
# arr2d=np.array([[1,2,3],
#                 [5,6,7]])
# print(arr2d.shape)  # (2,3)

# # size=total no of elements in array
# print(arr2d.size) # 6

# # no of dimensions
# arr1d=np.array([1,2,3])
# arr3d=np.array([[1,2],[3,5],[9,8.0]])
# print(arr1d.ndim)
# print(arr2d.ndim)
# print(arr3d.ndim)

# data type
# print(arr3d.dtype)

# changing data type

# arr1=np.array([1.1,2.8,3.6])
# print(arr1.dtype)
# arr2=arr1.astype(int)
# print(arr2,arr2.dtype)
# arr3=arr1.astype(str)
# print(arr3,arr3.dtype)

# operations on numpy arrays
# arr=np.array([10,20,30])
# print(arr+5)
# print(arr*6)
# print(arr**2)


# aggregation functions
# arr=np.array([10,20,30,40,50])
# Sum=np.sum(arr)
# print(Sum)
# # similarly
# print(np.mean(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.std(arr))
# print(np.var(arr))

