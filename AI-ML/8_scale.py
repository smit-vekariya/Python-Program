# REF: https://www.w3schools.com/python/python_ml_scale.asp

import pandas, os
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv(os.getcwd() + r"\AI-ML\files\scale_data.csv")

X = df[['Weight', 'Volume']]
y = df["CO2"]

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()  
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictCO2 = regr.predict([scaled[0]])
print("predictCO2 ==> ", predictCO2)