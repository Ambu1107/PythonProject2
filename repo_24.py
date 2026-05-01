#3.1.1 Numpy Array Operations
import numpy as np
R,C=map(int,input().split())
list1=[]
for i in range(R):
	row=list(map(int,input().split()))
	list1.append(row)
array=np.array(list1).reshape(R,C)
print(array)
print(array.ndim)
print(array.shape)
print(array.size)