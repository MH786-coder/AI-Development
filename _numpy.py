import numpy as np
from os import system

system('clear')
#In array, the element size are should equal.like below,
array = np.array([[1,2,3,4],[6,7,8,9]])
string_arr = np.array(['iam','mohamed','hathim'])
strings = np.array([['this','is','double'],['strings','are','numpy']])
print("To print the string by array : ",string_arr)
print("To print array using numpy : \n",array,end='\n')

#To print datatype:
print("To print data type of numpy array variable: ",array.dtype,end='\n')
print("To print shape of numpy array variable: ",array.shape,end='\n')
print("To print the size of the array : ",array.size,end='\n')

print('\n\n')
#To access specific elements using from array
print("To access specific element from the array :",array[0][1])
print("To access specific element from the array :",array[1][2])

#same as string
print("To access specific element from the array :",strings[0][1])
print("To access specific element from the array :",string_arr[1])

print('\n\n')

print('Lets generate array\n')
arr = np.zeros((2,2))
arr_forOnce = np.ones((2,2))

print('To print zeros array :\n',arr,end='\n')
print('To print once array :\n',arr_forOnce,end='\n')

print('\nGenerate random number using numpy array\n')
rand_arr = np.random.rand(2,2)
print(rand_arr)

print('\narray operation\n')
a = np.array([1,2,3])
b = np.array([3,4,5])

print("Addition of two matrix:",a+b) #---> a[index] + b[index] until ends
print("Multiplication of two matrix:",a*b) #---> a[index] * b[index] until ends

print("Dot product of two matrix:",np.dot(a,b),end='\n')

print('slicing of array:',a[0],end='\n')
print('slicing of array:',a[0:],end='\n')
print('slicing of array:',a[-1],end='\n')


print('To find the dimension of the array\n')

print("The dimension of array a is",np.ndim(a))
print("The dimension of array b is",np.ndim(b))

print("The dimension of array \'strings\' is",np.ndim(strings))

print('\nwe can also create array like this\n')
c = np.arange(6) # 0 to 6 = total 6
print(c,end='\n')
reshape_array = c.reshape(2,3)
print('\nAfter reshaping these\n')
print(reshape_array)
print('\n')
print(np.linspace(0, 1, 5))  
print('\n')
print(np.eye(3))
print('\n')
print(np.random.randint(1,10,size=3))
print(np.random.randint(1,10))