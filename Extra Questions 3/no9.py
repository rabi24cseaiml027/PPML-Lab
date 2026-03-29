import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
arr = a@b
#arr2 = np.dot(a,b)
print("After matrix multiplication :\n", arr)
