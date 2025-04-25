# REF : https://www.w3schools.com/python/python_ml_train_test.asp
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
test_x = x[80:]

train_y = y[:80]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0,6,100)

train_r2 = r2_score(train_y, mymodel(train_x))
test_r2 = r2_score(test_y, mymodel(test_x))
# The result 0.809 shows that the model fits the testing set as well, and we are confident that we can use the model to predict future values.\

plt.scatter(train_x, train_y)
# plt.scatter(test_x, test_y)
plt.plot(myline, mymodel(myline))
plt.show()