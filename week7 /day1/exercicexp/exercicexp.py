import numpy as np
from random import *
import pandas as pd
# lst = [1, 2, 3]

# print(lst)



# lst_2d = [[3, 5, 7, -4, 1], [0, 5, 33, -750, 2]]
# numpy_arr_2d = np.array(lst_2d)
# print(numpy_arr_2d.shape)

# def calc(one_dim_array):
#     minimum = np.amin(one_dim_array)
#     product = np.prod(one_dim_array)
#     standart = np.std(one_dim_array)
#     arr_prod = one_dim_array.dot(one_dim_array)

#     return minimum, product, standart, arr_prod 




# array = [1, 2, 3 ,4]
# numpy_arr = np.array(array)

# res1, res2, res3, res4 = calc(numpy_arr)
# print(res1)
# print(res2)
# print(res3)
# print(res4)
# print(numpy_arr+4)

list_0 = np.zeros(10)
list_0[4] = 1 
# print(list_0)

vector = np.arange(10, 51, 1)
res = vector[::-1]
# print(vector)
# print("Resultant new reversed array:",res)


matrix = np.arange(0, 9, 1 ).reshape((3, 3))
# print(matrix)

x = [1,2,0,0,4,0]
# print(np.nonzero(x))

array_2D=np.identity(3)
# print('3x3 matrix:')
# print(array_2D)

n = np.random.random((3, 3, 3))
# print(n*10)

big_array = np.random.random((10, 10))
minimum = np.amin(big_array)
maximum = np.amax(big_array)
# print(minimum, maximum)


vector_v = np.random.rand(30,).reshape(6,5)
np.mean(vector_v)
# print(vector_v)

s = np.zeros((5, 3))
s[0]=1
s[-1]=1
# print(s)

array_D= np.diag([1, 2, 3, 4, 7])
# print(array_D)

V = np.random.rand(5, 5)
# print(V)

x = np.random.random((5,3))
y = np.random.random((3,2))
z = np.dot(x, y)
# print(z)


x = np.random.random(10)
x.sort()
# print(x)