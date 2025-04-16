# REF: https://www.w3schools.com/python/python_ml_multiple_regression.asp
import pandas, os
from sklearn import linear_model

df = pandas.read_csv(os.getcwd() + r"\AI-ML\files\multiple_regression_data.csv")
print("df", df)

X = df[["Weight","Volume"]]
y = df["CO2"]

regr =  linear_model.LinearRegression()
regr.fit(X, y)

print("Coefficient ==> ",regr.coef_)
# The result array represents the coefficient values of weight and volume.
# Weight: 0.00755095
# Volume: 0.00780526
# These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
# And if the engine size (Volume) increases by 1cm3, the CO2 emission increases by 0.00780526g.

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictCO2 = regr.predict([[2300, 1300]])
print("predictCO2 ==> ", predictCO2)

#What if we increase the weight with 1000kg?
predictedCO2 = regr.predict([[3300, 1300]])
print("predictedCO2 ==> ", predictedCO2)

# We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.
# Which shows that the coefficient of 0.00755095 is correct:

# 107.2087328 + (1000 * 0.00755095) = 114.75968