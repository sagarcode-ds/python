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

#  2nd round

# 🟢 Problem 1 — Slicing Practice
# arr = np.arange(10, 110, 10) → 10 elements
# Get the first element, last element, and the 5th element
# Get the first 4 elements using slicing
# Get the last 3 elements using negative indexing
# Reverse the entire array
# Get every other element (step slicing) — predict the output first

# arr = np.arange(10, 110, 10)
# print(arr)
# print(' first element, last element, and the 5th element:',arr[[0,-1,4]])
# print(' first 4 elements:',arr[:4])
# print('last 3 elements:',arr[-3:])
# print('reversed array:',arr[-1::-1])
# print('every other element:',arr[::2])


# 🟡 Problem 2 — 2D Indexing
# Create this matrix manually:
#  1   2   3   4
#  5   6   7   8
#  9  10  11  12

# Access the element at row 2, column 3
# Print the entire second row
# Print the entire third column
# Extract the bottom-right 2×2 sub matrix ([[7,8],[11,12]])

# a=np.array([[1,2,3,4], 
#             [5,6,7,8],
#             [9,10,11,12]])
# print(a)
# print(a[1,2])
# print(a[1],a[:,2])
# print(a[1:,2:])

# 🟠 Problem 3 — Boolean Masking with Combined Conditions
# Weekly temperatures (°C): [23, 37, 29, 41, 19, 35, 28]

# Find all hot days (above 30°C)
# Find all cool days (below 25°C)
# Find pleasant days (between 25 and 35 inclusive) — use a combined condition
# Find days that are either below 20°C or above 38°C (extreme days)

# temp=np.array([23, 37, 29, 41, 19, 35, 28])
# print('hot days:',temp[temp>30])
# print('cold days:',temp[temp<25])
# print('pleasant days:',temp[(temp>=25) & (temp<=35)])
# print('extreme days:',temp[(temp<=20) | (temp>=38)])


# 🔴 Problem 4 — Reshape + 2D Operations
# Start with np.arange(1, 13).

# Reshape into a 3×4 matrix — predict the shape before running
# Reshape the same original array into 4×3 using -1 for one dimension
# From the 3×4 matrix: extract the entire second column
# Flatten back to 1D using both .ravel() and .flatten() — they look identical, but which one is a view and which is a copy?

# a=np.arange(1, 13)
# reshaped=a.reshape(3,4)
# print(reshaped)
# print(reshaped[:,1])
# four_by_three=a.reshape(4,-1)
# print(four_by_three)

# flattend1,flattend2=four_by_three.ravel(),four_by_three.flatten()
# print(flattend1)  # modify original
# flattend1[2]=100  # modified
# print(flattend1)
# print(four_by_three)
# print(flattend2)  # copy

# 🔥 Problem 5 — Challenge (Everything Combined)
# You have two batches of exam scores:

# Batch A: [55, 72, 88, 45, 91, 63]
# Batch B: [81, 67, 59, 94, 70, 55]


# A new student joined Batch A with score 78 — insert it at position 3
# Combine both batches (after the insert, Batch A has 7 elements — concatenate as 1D)
# Find the mean of the combined class
# Filter out all students who scored above the mean
# Reshape the original 12-element combined array (before the insert) into a 2×6 matrix — each row is one batch
# From that 2×6 matrix: extract only the scores from Batch B (entire second row)

# a=np.array([55, 72, 88, 45, 91, 63])
# b=np.array([81, 67, 59, 94, 70, 55])
# combined=np.concatenate((a,b))
# a1=np.insert(a,2,78)
# print(a1)
# combined2=np.concatenate((a1,b))
# print(combined2)
# mean=round(np.mean(combined2),2)
# print('scores over mean:',combined2[combined2>mean])
# reshaped=combined.reshape(2,6)
# print(reshaped)
# print('scores from Batch B:',reshaped[1,:])

#  round 3

# 🟢 Problem 1 — Delete & Stack
# You have:
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([6, 7, 8, 9, 10])

# Delete the element at index 2 from a
# Delete elements at indices 0 and 4 from b in one call
# Stack the original a and b row-wise — predict the shape first
# Stack them column-wise — predict the shape first

# print(np.delete(a,2))
# print(np.delete(b,[0,4]))
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))  # could not predict this one


# 🟡 Problem 2 — Splitting
# Start with np.arange(1, 25) (24 elements):
# Reshape into a 4×6 matrix
# Split into 2 equal parts using vsplit — what shape will each part be?
# Split into 3 equal parts using hsplit — what shape will each part be?
# On the original 1D array, split at indices [6, 14, 20] using np.split — how many parts does this produce?

# a=np.arange(1, 25)
# print('a :',a)
# reshaped=a.reshape(4,6)
# print(reshaped)
# print(np.vsplit(reshaped,2))
# print(np.hsplit(reshaped,3))  # could not predict shape
# print(np.split(a,[6,14,20]))


# 🟠 Problem 3 — Broadcasting
# You have a 3×4 matrix of product prices:
# prices = np.array([[100, 200, 300, 400],
#                    [150, 250, 350, 450],
#                    [200, 300, 400, 500]])

# Apply a flat 10% discount to all prices
# Apply different discounts per row — row 0 gets 10%, row 1 gets 20%, row 2 gets 30%. The discount array is [10, 20, 30]. You'll need to reshape it first — think about what shape makes it broadcast correctly across columns

# prices = np.array([[100, 200, 300, 400],
#                    [150, 250, 350, 450],
#                    [200, 300, 400, 500]])
# discount=np.array([10,20,30])
# dis=discount.reshape(3,1) * 1/100
# print(dis)

# final_prices=prices-(prices*10/100)
# print(final_prices)

# discounted_prices=prices-prices*dis
# print(discounted_prices)


# 🔴 Problem 4 — Stack + Delete + Slice + Aggregation
# You have:
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
# Stack them vertically — what shape is the result?
# Delete the 4th row (index 3) from the stacked matrix
# Extract the second column from the resulting matrix
# Find the mean of that column — predict it before running

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
# stacked=np.vstack((a,b))
# print(stacked)
# arr=np.delete(stacked,3,axis=0)
# print(arr)
# second_column=arr[:,1]
# print(second_column)
# print(np.mean(second_column))

#  Round 3

# 🟢 Problem 1 — Warm-up
# arr = np.array([3.0, np.nan, 7.0, np.nan, 12.0, 5.0])

# Print the boolean mask showing where NaN values are
# Count how many NaN values exist — do it in one line using two functions you now know
# Replace all NaN with 0 using nan_to_num
# On the original array, find the sum and mean the safe way

# print(np.isnan(arr))
# print(np.sum(np.isnan(arr)))
# arr2=np.nan_to_num(arr,nan=0)
# print(arr2)
# print(np.nansum(arr),np.nanmean(arr))


### 🟡 Problem 2 — NaN-safe aggregation
# scores = np.array([85.0, 92.0, np.nan, 78.0, np.nan, 88.0, 95.0])

# 1. Try `np.mean(scores)` — what comes out and why?
# 2. Find the correct mean, min, max, and std using nan-safe functions
# 3. Replace each NaN with the **nanmean** of the array (compute it first, then pass to nan_to_num)
# 4. After replacement, verify no NaN remain — use `np.sum` + `np.isnan` in one line

# print(np.mean(scores))  # nan, due to presence of np.nan value, 
# print(np.nanmean(scores),np.nanmin(scores),np.nanmax(scores),round(np.nanstd(scores),2))
# mean=np.nanmean(scores)
# scores2=np.nan_to_num(scores,nan=mean)
# print(scores2)
# print(np.sum(np.isnan(scores2))) # 0, verified no Nan remained


# 🟠 Problem 3 — Mixed NaN and inf
# data = np.array([5.0, np.inf, 3.0, np.nan, -np.inf, 8.0, np.nan, 2.0])

# Count NaN values and infinite values separately
# Extract only the finite values using np.isfinite + boolean masking
# From those finite values, find mean, min, max
# Clean the full array in one call: NaN → 0, +inf → 999, -inf → -999
# Predict what np.sum(data) gives before cleaning. Then verify after cleaning.

# print(np.sum(np.isnan(data)),np.sum(np.isinf(data))) # 2,2
# finites=data[np.isfinite(data)]
# print(finites)
# print(np.mean(finites),np.min(finites),np.max(finites))
# print(np.sum(data)) # nan obviously
# cleaned_arr=np.nan_to_num(data,nan=0,posinf=999,neginf=-999)
# print(cleaned_arr,np.sum(cleaned_arr))


# 🔴 Problem 4 — 2D Missing Data
# readings = np.array([[1.0,  2.0, np.nan, 4.0],
#                      [5.0, np.nan, 7.0,  8.0],
#                      [np.nan, 10.0, 11.0, 12.0]])

# Print the boolean mask of NaN positions
# Count total NaN values in the entire matrix
# Replace all NaN with the nanmean of the entire matrix
# After replacement, verify no NaN remain
# Find the sum and mean of the cleaned matrix — do these match what nansum and nanmean gave on the original?

# print(np.isnan(readings))
# print(np.sum(np.isnan(readings)))
# mean=np.nanmean(readings)
# readings2=np.nan_to_num(readings,nan=mean)
# print(readings2)
# print(np.sum(np.isnan(readings2)))  # 0, verified
# summ,mean=np.nansum(readings),np.nanmean(readings)
# summ2,mean2=np.sum(readings2),np.mean(readings2)

# print(summ,summ2,summ==summ2)
# print(mean,mean2,mean==mean2)  # does not match with original sum but match with mean


# 🔥 Problem 5 — Challenge (Full pipeline)
# You have a 12-point temperature sensor dataset with errors:
# temps = np.array([23.0, np.nan, 37.0, np.inf, 19.0, np.nan,
#                   -np.inf, 28.0, 35.0, 41.0, np.nan, 29.0])

# Count NaN values and infinite values separately
# Extract only finite values using boolean masking — find their mean, min, max
# Clean the full array: NaN → mean of finite values, +inf → max finite value, -inf → min finite value (use nan_to_num with the values from step 2)
# Reshape the cleaned 12-element array into a 3×4 matrix (3 weeks, 4 readings each)
# Filter all temperatures above the overall mean from the reshaped matrix using boolean masking
# Delete the first week (row 0) from the matrix, then find the mean and std of what remains

# print(np.sum(np.isnan(temps)),np.sum(np.isinf(temps)))
# finite=temps[np.isfinite(temps)]
# mean,minn,maxx=np.mean(finite),np.min(finite),np.max(finite)
# print(finite),print(mean,minn,maxx)

# cleaned_arr=np.nan_to_num(temps,nan=mean,posinf=maxx,neginf=minn)
# print(cleaned_arr)

# reshaped_arr=cleaned_arr.reshape(3,4)
# print(reshaped_arr)

# filtered_arr=reshaped_arr[reshaped_arr>mean]
# print(filtered_arr)

# new_arr=np.delete(reshaped_arr,0,axis=0)
# print(f'{np.mean(new_arr):.2f},{np.std(new_arr):.2f}')

#  Projects

### Project 1 — Student Grade Analyzer *(Beginner)*

# **Goal:** Given raw marks, produce a full grade report.
# Tasks:
# 1. Create an array of 10 student scores (use np.random.randint)
# 2. Find class average, highest, lowest, std deviation
# 3. Use np.where() to assign grades: A(≥80), B(≥65), C(≥50), F(<50)
# 4. Count how many students passed (score ≥ 50)
# 5. Find the rank of each student using argsort

np.random.seed(42)
scores = np.random.randint(0, 101, 10)
print(scores)
print(np.mean(scores),np.max(scores),np.min(scores),np.std((scores)))

grades = np.where(scores >= 80, 'A',
         np.where(scores >= 65, 'B',
         np.where(scores >= 50, 'C', 'F')))
print(grades)
print('no of students who passed:',np.sum(scores >= 50) )
print('\nrank of each students:')
ranks = np.argsort(np.argsort(-scores)) + 1
print(ranks)



