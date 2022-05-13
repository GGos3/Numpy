import numpy as np

#reshape 데이터는 그대로 둔채 배열의 크기만 변경할 때 사용
a = np.arange(12)
print(a)
b = np.arange(3, 4)
print(b)
#flatten과 ravel: 다차원 배열을 1차원 배열로 변경
a.reshape(2, -1, 3)
fa = a.flatten()
fa[0] = 100
print(a)
print(fa)   #vlatten은 값을 복사하므로, 원본이 바뀌지 않음.

c = a.reshape(3, -1)
re = c.ravel()
print(c)
print(re)   #ravel은 값을 공유하므로, 원본이 바뀜