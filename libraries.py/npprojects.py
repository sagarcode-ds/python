import numpy as np

# 🟢 Problem 1 — Warm Up
# Topic: Array creation + properties
# Create a 1D NumPy array of even numbers from 2 to 20 (inclusive).
# Then print:

# Its shape, size, ndim, and dtype
# Can you predict what each value will be before running the code?

# arr1d=np.arange(2,21,2)
# print(arr1d)
# print('shape:',arr1d.shape)
# print('size:',arr1d.size)
# print('dimension:',arr1d.ndim)
# print('type:',arr1d.dtype)


# 🟡 Problem 2 — Easy
# Topic: Operations + aggregation functions
# A student scored [72, 85, 90, 68, 95, 78, 88] in 7 subjects.

# Store it as a NumPy array
# Find total marks, average, highest score, and lowest score
# The teacher gives 5 bonus marks to every subject — print the new scores
# What is the dtype? Now convert it to float and print again

# marks=np.array([72, 85, 90, 68, 95, 78, 88])
# print('total marks:',np.sum(marks))
# print('average marks:',round(np.mean(marks),2))
# # similarly
# print(np.max(marks),np.min(marks))

# print('new score:',marks+5)  #dtype=int
# float_type=marks.astype(float)
# print(float_type)


# 🟠 Problem 3 — Medium
# Topic: 2D arrays + all aggregation functions
# Create this 3x3 matrix manually:
# 10  20  30
# 40  50  60
# 70  80  90

# Print its shape, size, and ndim
# Find the sum, mean, min, max, std, and var of the entire matrix
# Triple every element and print the new array
# Without running code first — what do you expect the new sum to be? Verify it.

# matrix=np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(matrix)
# print(matrix.shape)
# print(matrix.size)
# print(matrix.ndim)

# print(np.sum(matrix))
# print(np.mean(matrix))
# print(np.max(matrix))
# print(np.min(matrix))
# print(f'{np.std(matrix):.2f}')
# print(f'{np.var(matrix):.2f}')

# new_arr=matrix*3
# # new sum = old sum * 3 
# print(np.sum(new_arr))


# 🔴 Problem 4 — Medium-Hard
# Topic: Eye + operations + dtype conversion + reasoning

# Create a 4x4 identity matrix using np.eye()
# Multiply every element by 5
# Before running — predict the sum and mean of this matrix. (Hint: think about how many 5s exist in it)
# Convert it from float to int dtype
# Find the variance and standard deviation

# matrix=np.eye(4,4) * 5
# print(matrix)
# # my prediction: sum=20 , mean=20/size
# print(np.sum(matrix))
# print(np.mean(matrix))
# matrix2=matrix.astype(int)
# print(matrix2)
# print(np.var(matrix2),round(np.std(matrix2),2))

# 🔥 Problem 5 — Challenge
# Topic: Everything combined + real-world thinking
# A small shop's monthly sales in thousands for 6 months: [120, 145, 110, 160, 135, 175]

# Find total 6-month sales and monthly average
# Create a new array with actual values (multiply by 1000)
# The shop expects 8% growth next year — create a projected sales array (original values × 1.08)
# Convert the projected array to int dtype (drop decimals)
# Find the range of original sales (max − min) — NumPy has no direct range function, so think about combining two functions you know
# Find std and var of the original array — what do these tell you about consistency of sales?

# sales=np.array([120, 145, 110, 160, 135, 175])
# new_array=sales*1000
# print('sales:',new_array)
# growth_array=new_array*(0.08+1)
# print('array after growth:',growth_array)
# int_growth_array=growth_array.astype(int)
# print(int_growth_array)
# print(f'range of original sales:{np.max(sales)-np.min(sales)}')
# print(round(np.std(sales),2) ,round(np.var(sales),2))
# since std=22.5, so data are not very spread around mean so maybe consistent?

