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

# indexing and slicing
#  1D array(index)  2D array(row,column)

# arr=np.array([10,20,30,40,50])
# first_element,last_element=arr[0],arr[-1] # and so on
# print(first_element,last_element)
# first_three_elements=arr[:3]
# print(first_three_elements)
# last_to_first=arr[-1::-1]
# print(last_to_first)

# fancy indexing: selecting multiple elements at once
# arr=np.array([10,20,30,40,50])
# print(arr[[0,2,4]])

#  filtering data (boolean masking)
# print(arr[arr>25])
# print(arr[arr%2==0])
# print(arr[arr<0])


# reshaping : manipulating array dimension
# note: reshaping does not create copy, it returns a view
# arr=np.array([10,20,30,40,50,60])
# reshaped_arr=arr.reshape(2,3)
# print(reshaped_arr,arr)

# flattening array (multi D to 1D array)
# note: .ravel()-view  .flatten()-copy
# arr2d=np.array([[1,2,3],
#                 [4,5,6]])
# print(arr2d.ravel())
# print(arr2d.flatten())
# print(arr2d)


#  Advance numpy
# np.insert(array,idx,val,axis=None) for 2D axis=0(row wise),axis=1(column wise)
# arr=np.array([10,20,30,40,50,60])
# new_arr=np.insert(arr,2,100)
# print(new_arr)

# insert in 2D array
# arr2d=np.array([[1,2],[8,9]])

# new_arr2d=np.insert(arr2d,1,[4,5],axis=None)
# print(new_arr2d)

# append (add at end)
# a=np.append(arr2d,[40,50,60])
# print(a)

# concatenation :  np.concatenation(array1,array2,axis=0,1)
# a1=np.array([1,2,3])
# a2=np.array([4,5,6])
# new_a=np.concatenate((a1,a2))
# print(new_a)



