import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

#========================================================

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y, color = 'hotpink')


# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y, color = '#88c999', alpha=0.5)

# plt.show()

#========================================================

# x = np.random.randint(100,  size=(100))
# y = np.random.randint(100,  size=(100))

# sizes = 2 * x
# colors = 2 * y

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
# plt.colorbar()
# plt.show()
