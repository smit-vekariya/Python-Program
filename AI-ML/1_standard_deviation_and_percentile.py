# ref: https://www.w3schools.com/python/python_ml_standard_deviation.asp
# ref: https://www.w3schools.com/python/python_ml_percentile.asp

'''Standard deviation is a number that describes how spread out the values are.
A low standard deviation means that most of the numbers are close to the mean (average) value.
A high standard deviation means that the values are spread out over a wider range.
In fact, if you take the square root of the variance, you get the standard deviation!
Or the other way around, if you multiply the standard deviation by itself, you get the variance!'''

import numpy
print("============== Standard deviation =============")

speed = [86,87,88,86,87,85,86]
std_y = numpy.std(speed)
var_y = numpy.var(speed)

print("Variance:", var_y)
print("Standard Deviation:", std_y)


speed = [32,111,138,28,59,77,97]
std_x = numpy.std(speed)
var_x = numpy.var(speed)

print("Variance:", var_x)
print("Standard Deviation:", std_x)


print("======= startdard deviation without using numpy ========")

speed = [86, 87, 88, 86, 87, 85, 86]

# Step 1: Calculate the mean
mean = sum(speed) / len(speed)

# Step 2: Calculate the squared differences from the mean
squared_diffs = [(x - mean) ** 2 for x in speed]

# Step 3: Calculate the average of those squared differences
variance = sum(squared_diffs) / len(speed)

# Step 4: Take the square root of variance
std_dev = variance ** 0.5

print("Variance:", variance)
print("Standard Deviation:", std_dev)


print("=================== percentile ================")

ages = [0,1,2,3,4,5,6,7,8,9,10]
x = numpy.percentile(ages, 80)
print(x, f"=> its means that 80% of the people are aged {x} years or younger.")

print("======= percentile without using numpy ========")

def percentile(data, percentile):
    data.sort()
    n= len(data)
    rank = (percentile/100) * (n -1)
    lower = int(rank)
    upper = lower + 1

    if upper >= n:
        return data[lower]

    weight = rank - lower
    return data[lower] * (1 - weight) + data[upper] * weight

x = percentile([11,12,13,14,15,16,17,18,19,20], 80)
print(x, f"=> its means that 80% of the people are aged {x} years or younger.")
