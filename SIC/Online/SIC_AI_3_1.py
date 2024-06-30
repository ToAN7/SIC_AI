# scipy, numpy -> calculate on matrix
# pandas -> graph-based's data
# sklearn -> ML algorithms
# nltk -> NL toolkits
# tensorflow, pytorch, keras -> DL algorithms

import numpy as np

# Khoi tao vector:

x = np.array([2,4,5])

print(type(x[0]))
print("==============")

y = np.array([5,6,2], dtype=np.float64)

print(type(y[0]))
print("==============")

x_zeros = np.zeros(5)
y_ones = np.ones(5)

print(x_zeros)
print(y_ones)
print("==============")

x_like_zeros = np.zeros_like(x) # Create a zero vector that have the same columns as x
y_like_ones = np.ones_like(y) # Create a one vector that have the same columns as y

print(x_like_zeros)
print(y_like_ones)
print("==============")

a = np.array([5,6,3,-2,-6])
b = np.array([-2,5,12,-6,4])
print(a.shape)
print(a[-2:])

print("==============")
print(a + 2) # Mat(a) + Mat(2)
print(a * 2)
print(a ** 2)
print(a / 2)
print("==============")

print(a.dot(b))
print(b.dot(a))
print(np.dot(a,b))
print("==============")

print(np.max(a)) # 6 - value
print(np.argmax(a)) # 1 - idx
print(np.min(a)) # -6
print(np.argmin(a)) # 4

print("==============")

