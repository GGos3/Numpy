import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
an =[]

for di in arr:
    an.append(2 * di)
print(an)

a = np.array([1, 2, 3])
b = np.array([10, 20 ,30])
print(a * 2 + b)
print(a == b)
print(b > 20)
print((a == 2) &  (b > 10))