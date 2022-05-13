import numpy as np

a = np.array([[1, 2], [3, 4]])

a_r = a.ravel()
a_f = a.flatten()

a[0][0] = 777
print(a)

print(a_r)  #ravel은 메모리를 공유하므로 같이 변경
print(a_f)  #flatten은 값 복사를 시행하므로 변경 X