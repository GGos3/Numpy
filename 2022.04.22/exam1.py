import numpy as np


#1
bb = np.array([[10, 20, 30, 40], [50, 60 , 70 ,80]], dtype="f")
cc = np.array([[10, 20, 30, 40], [50, 60 , 70 ,80]], dtype="int16")
#2
cc.flatten()
#3
cc = cc.reshape(4, 2)
cc.T    #행&열 변환
#4
dd = np.ones_like(cc)