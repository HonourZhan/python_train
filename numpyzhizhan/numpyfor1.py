import numpy as np

# a=np.array([1,2,3,4])
# print(a)
# data1=[1,2,3,4,5,6]
# a1=np.array(data1)
# print(a1)
data2=np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
# print(data2)
# data2.shape(0)

# print(data2.dtype)

# arr1=np.array([1,2,3],dtype=np.float64)
# arr2=np.array([1,2,3],dtype=np.int32)
#
# float_arr=arr2.astype(np.float64)
# print(float_arr.dtype)
# numeric_str=np.array(['1.25','-9.6','42'])
# numeric_str=numeric_str.astype(np.float64)
# print(numeric_str.dtype)
# print(arr2+arr2)
# print(arr2*3)

# print(data2)
# print(data2[:2])
# print(data2[:2,:2])
# print(data2[1,:3])

a=data2[1]
print(a)
a[:]=99
print(a)
print(data2)