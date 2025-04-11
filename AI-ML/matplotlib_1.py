import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,1,2,3])

plt.plot(x, y)
plt.show()

#================================================================

# y = np.array([3, 8, 1, 10]) #  defualt x is [0,1,2...]

# plt.plot(y,  marker = 'o', ms = 20, mfc = 'r',  mec = 'b',  ls = ':')
# plt.show()


#================================================================


# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 50, 260, 270, 2, 290, 30, 151, 320, 330])

# plt.plot(x, y)

# plt.title("Sports Watch Data", fontdict = {'family':'serif','color':'Green','size':15})
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plt.show()
