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


#  deleting the array element  : np.delete(array,index,axis=None)
# arr=np.array([10,20,30,40,50,60])
# new_arr=np.delete(arr,0)  # 10 deleted
# print(new_arr)

#  for 2D
# arr2d=np.array([[1,2,3],[4,5,6]])
# new_arr2d=np.delete(arr2d,0,axis=0)
# print(new_arr2d)

# stacking  vstack() row wise,  hstack() column wise
# a1=np.array([1,2,3])
# a2=np.array([4,5,6])
# print(np.vstack((a1,a2)))
# print(np.hstack((a1,a2)))
# a = np.array([[1, 2], [3, 4]])   # 2×2
# b = np.array([[5, 6], [7, 8]])   # 2×2

# print(np.vstack((a, b)))   # adds rows → 4×2
# print(np.hstack((a, b)))   # adds cols → 2×4


# splitting np.split(), np.hsplit(), np.vsplit()
# arr=np.array([1,2,3,4,5,6])
# print(np.split(arr,2))
# print(np.vsplit(arr,2))  #error

#  broadcasting : expands smaller arrays to larger,faster than loops
# prices=np.array([100,200,300,400])
# discount=10 # percent
# final_prices=prices-prices*discount/100
# print(final_prices)

# how numpy handle arrays of different shapes?
#  rule 1: matching dimension, example
# print(np.array([1,2,3])+np.array([1,2,3])) # [2 4 6]

# rule 2: expanding single elements
# print(np.array([1,2,3])+10) # [11 12 13]

# rule 3 : incompatible shapes
#  error

# matrix=np.array([[1,2,3],[4,5,6]]) # 2x3
# vector=np.array([10,20,30]) #1D
# result=matrix+vector  
# print(result)  #  [[11 22 33] [14 25 36]]

# print(np.array([[1,2,3],[4,5,6]])+np.array(np.array([1,2])))  #ValueError: operands could not be broadcast together with shapes (2,3) (2,)
#  solution:  reshape

#  vectorization : apply operations on entire array, faster than loops, used in matrix operation
# print(np.array([1,2,3])+np.array([4,5,6]))
# print(np.array([10,20,30]) * 3)


#  handling missing and special values
# np.isnan-detect missing values, np.nan_to_num(), np.isinf()
# nan- not a num(either calculation fail or data missing)

# arr=np.array([1,2,np.nan,4,np.nan,5,6])
# print(np.isnan(arr))
# print(np.nan==np.nan)  # False, can't be compared

# replace np.nan values:  np.nan_to_num(array,nan=number, default=0)
# arr2=np.nan_to_num(arr,nan=4)
# print(arr2)

#  handling infinite values : np.isinf(array)
# arr=np.array([1,2,np.inf,4,-np.inf,6])
# print(arr)
# print(np.isinf(arr))

#  now replace infinite values with non-infinite
# arr2=np.nan_to_num(arr,posinf=1000,neginf=-1000)
# print(arr2)

#  Missing concepts from Tutorial

# np.where()
# scores = np.array([40,55,70,85])

# result = np.where(scores >= 50,
#                   "Pass",
#                   "Fail")

# print(result)


# Conditional Replacement
# Replace negative numbers with 0.
# arr = np.array([-5,10,-3,20])
# arr[arr < 0] = 0
# print(arr)

# sorting
# arr = np.array([5,1,8,3])
# print(np.sort(arr))

# removing duplicates from array
# arr = np.array([1,1,2,2,3,3,3])
# print(np.unique(arr))

#  sum by rows and columns
# np.sum(arr, axis=0) sum by columns, not row
# np.sum(arr, axis=1)


# arr = np.array([10,20,30,40])
# print(np.any(arr > 35))
# print(np.all(arr > 5))

# Transpose
# A = np.array([[1,2,3],
#               [4,5,6]])
# print(A.T)

# np.linspace()- evenly spaced points
# arr = np.linspace(0, 1, 5)
# print(arr)
# [0. 0.25 0.5 0.75 1.0]


# finding indices of largest,smallest items
# arr = np.array([10,20,30,40])
# print(np.argmax(arr))
# print(np.argmin(arr))
# print(np.argsort(arr)) # indices that would sort it


# np.clip()-keeps all values within min-max range.
# arr=np.array([-10,5,200,85,-3,110])
# clipped=np.clip(arr,0,100)
# print(clipped) # [  0   5 100  85   0 100]

# np.cumsum() and np.cumprod()-
# sales=np.array([100,200,150,300])
# # running totals and running products
# sales_cumsum = np.cumsum(sales)
# sales_cumprod = np.cumprod(sales)
# print('sales:', sales)
# print('cumulative sum:', sales_cumsum)
# print('cumulative product:', sales_cumprod)

# np.median() and np.percentile
# np.percentile(array,25)- First Quartile or 25th percentile,  np.percentile(array,75)- 3rd Quartile or 75th percentile


# matrix multiplication : np.dot() and @
# a=np.array([[1,2],
#             [3,4]])
# b=np.array([[5,6],
#             [7,8]])
# print(a*b) # element wise multiplication
# print(np.dot(a,b))  # true mathematical multiplication
# print(a @ b) # same as np.dot just shorter syntax

# np.newaxis- used to reshape 1D arrays for broadcasting with 2D arrays
# row=np.array([1,2,3])
# col=np.array([10,20,30]) 

# Want to add them as row + column? Need 2D shapes
# row_2d = row[np.newaxis, :] # shape (1, 3)
# col_2d = col[:, np.newaxis] # shape (3, 1)

# print(row_2d)
# print(col_2d)
# result = row_2d + col_2d # broadcasts to (3, 3)
# print(result)


### 10. `np.corrcoef()` — Correlation (Key for EDA)
# Tells you how strongly two variables are related. Returns values between -1 and 1.

# hours_studied = np.array([1, 2, 3, 4, 5])
# scores = np.array([50, 60, 65, 80, 95])

# print(np.corrcoef(hours_studied, scores))
# [[1. , 0.98],
# [0.98, 1. ]] ← 0.98 means very strong positive correlation
