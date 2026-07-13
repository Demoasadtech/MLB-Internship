
'''NumPy

Implement programs to:

Create 1D and 2D arrays.
Perform arithmetic operations on arrays.
Find the maximum, minimum, mean, and sum of an array.
Reshape arrays into different dimensions.
Slice and index arrays.'''



import numpy as np

one_d_array1 = np.array([1, 2, 3])
one_d_array2 = np.array([6, 7, 8])
two_d_array1 = np.array([[1, 2, 3], [4, 5, 6]])

print(one_d_array1 + one_d_array2)  # Addition   
print(one_d_array1 - one_d_array2)  # Subtraction
print(one_d_array1 * one_d_array2)  # Multiplication
print(np.round(one_d_array1 / one_d_array2, 2))  # Division

print(one_d_array1 + two_d_array1)       # Note: broadcasting is applied here and need for arithmetic operations to be performed on arrays of different shapes.
print(one_d_array1 - two_d_array1)
print(one_d_array1 * two_d_array1)
print(np.round(one_d_array1 / two_d_array1, 2))

print(np.max(one_d_array1))  # Maximum
print(np.min(one_d_array1))  # Minimum
print(np.mean(one_d_array1))  # Mean
print(np.sum(one_d_array1))  # Sum

print(np.max(two_d_array1))  # Maximum
print(np.min(two_d_array1))  # Minimum
print(np.mean(two_d_array1))  # Mean
print(np.sum(two_d_array1))  # Sum

print(one_d_array1.reshape(3, 1))  # Reshape to 2D array
print(two_d_array1.reshape(6))  # Reshape to 1D array
print(two_d_array1.reshape(3, 2))  # Reshape to different 2D array

print(one_d_array1[0])  # Indexing
print(one_d_array1[2])  # Indexing
print(two_d_array1[1, 1])  # Indexing

print(one_d_array1[0:2])  # Slicing
print(two_d_array1[0:2, 0:2])  # Slicing 
print(two_d_array1[:, 1])  # Slicing
print(two_d_array1[0, :])  # Slicing
print(two_d_array1)  # Slicing