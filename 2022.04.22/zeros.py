#zeros는 모든 값을 0으로 설정하고 생성
import numpy as np

a = np.zeros(5)
print(a)
print("--------------")
b = np.zeros((2,3))
print(b)
print("--------------")
c = np.zeros((5, 2), dtype = "i")
print(c)
print("--------------")

#ones는 모든 값을 1으로 설정하고 생성
e = np.ones((2, 3, 4), dtype = "i8")
print(e)
print("---------------")
f = np.ones_like(b, dtype="f")
print(f)
print("---------------")

#transpose
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print(A.T)
print("---------------")

