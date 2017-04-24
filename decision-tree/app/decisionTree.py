import pandas as pd
train_df = pd.read_csv("D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/dataSet.csv")

y = targets = labels = train_df["sick"].values

columns = ["temperature", "heartbeat", "humidity"]
features = train_df[list(columns)].values
print features

from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X = imp.fit_transform(features)

from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X, y)

from sklearn.externals.six import StringIO
with open("D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/titanic.dot", 'w') as f:
  f = tree.export_graphviz(clf, out_file=f, feature_names=columns)
#import numpy as np
#X1 = np.array([[1],[10]]) # wrong shape
print clf.predict(X[:1, :])