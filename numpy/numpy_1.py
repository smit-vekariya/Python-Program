#import module 
import numpy  as np

print("========================= dimensional  ==========================")

data = np.array([1,2,3,4,5,6]) 
print("1-D =>", data[1] + data[2])

data = np.array([[1,2],[3,4]]) 
print("2-D =>",data[0, 1] + data[1, 1])

data =  np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3-D =>",data[0, 0, 2] + data[0, 1, 2] + data[1, 0, 2] + data[1, 1, 2])

print("========================= slicing ==========================")

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-3:-1])
# print(arr[:4])
# print(arr[1:5:2])

print("========================= Iterating  =======================")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)

# for x in np.nditer(arr):
#     print(x)

# for x in np.nditer(arr[:, ::2]):
#   print(x)

# for idx, x in np.ndenumerate(arr):
#   print(idx, x)


print("========================= Joining  =======================")

a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[4,5,6],[1,2,3]])

# print(np.concatenate((a1, a2)))
# print(np.concatenate((a1, a2), axis=1))

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

# print(np.stack((a1, a2), axis=1))
# print(np.hstack((a1, a2)))


print("========================= Splitting   =======================")

a1 = np.array([1,2,3,4,5,6,7,8,9])

# print(np.array_split(a1 ,3))
# print(np.array_split(a1, 4))

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# print(np.array_split(arr, 3))
# print(np.array_split(arr, 3, axis=1))


print("========================= Search  =======================")

arr = np.array([1, 2, 3, 4, 5, 4, 4])
# print(np.where(arr == 2))

arr = np.array([6, 7, 8, 9])
# print(np.searchsorted(arr, 8))
# print(np.searchsorted(arr, 8, side="right"))

print("========================= Sort  =======================")

arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))
arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))

print("========================= Filter  =======================")

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
# print(arr[x])
# print(arr[arr > 42])
# print(arr[arr % 2 == 0])

print("====================== Extra =====================")

zeros = np.zeros((2, 3))
# print(zeros)

ones = np.ones((3, 3))
# print(ones)

rand = np.random.rand(2, 2)
# print(rand)

r = np.arange(0, 10, 2)
# print(r)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
# print(x + y)
# print(x * y)

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])
# print(np.dot(A, B))