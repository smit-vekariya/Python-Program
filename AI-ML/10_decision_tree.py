# REF: https://www.w3schools.com/python/python_ml_decision_tree.asp

import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt



df = pd.read_csv(r"AI-ML\files\decision_tree_data.csv")

d = {'UK':0, 'USA':1, 'N':2} 
df["Nationality"] = df["Nationality"].map(d)
d= {"YES":1, "NO":0}
df["Go"] = df["Go"].map(d)

feature = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[feature]
y= df['Go']

print(df)
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

print("[1] means 'GO'")
print("[0] means 'NO'")
print("===>", dtree.predict([[40, 10, 6, 1]]))

tree.plot_tree(dtree, feature_names=feature)
plt.show()