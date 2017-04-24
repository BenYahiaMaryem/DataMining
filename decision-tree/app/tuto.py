import pandas as pd
train_df = pd.read_csv("D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/titanic-train.csv")
train_df["Sex"] = train_df["Sex"].apply(lambda sex: 0 if sex == 'male' else 1)


y = targets = labels = train_df["Survived"].values

columns = ["Fare", "Pclass", "Sex", "Age", "SibSp"]
features = train_df[list(columns)].values

from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X = imp.fit_transform(features)
print X
from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(X, y)

from sklearn.externals.six import StringIO
with open("D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/titanic.dot", 'w') as f:
  f = tree.export_graphviz(clf, out_file=f, feature_names=columns)
 
# import pydot

# (graph,) = pydot.graph_from_dot_file("D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/titanic.dot")
# graph.write_png('"D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/titanic.png') 
from subprocess import check_call
check_call(['dot','-Tpng','D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/titanic.dot','-o','D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/titanic.png'])

import numpy as np
nb_females = y.sum()
p_female = float(y.sum())/len(y)
p_male = 1. - p_female
entropy_root = - p_female * np.log2(p_female) - p_male * np.log2(p_male)
print entropy_root

entropy_before_split = 0.9607
weighted_entropy_after_split = 577./(577+314) * 0.699182 + 314./(577+314) * 0.823655
information_gain_root_node = entropy_before_split - weighted_entropy_after_split 
print "Information gain of the root node split:", information_gain_root_node

data = np.array([[2.,13.],[359., 41.]])
def p_log_p(p_):
  p = p_.copy()
  p[p != 0] = - p[p != 0] * np.log2(p[p != 0] )
  return p

def entropy(p):
  assert (p>=0.).all()
  assert np.allclose(1., p.sum(), atol=1e-08)
  return p_log_p(p).sum()
  
def conditional_entropy(p, axis=0):
  if axis == 1:
    p = p.T
  p_y_given_x = p / p.sum(axis=0)
  c = p_log_p(p_y_given_x) 
  p_x = p.sum(axis=0)/p.sum()
  s = c * p_x
  return s.sum()
 
def information_gain(p0, axis = 0):
  p = p0.copy()
  if axis == 1:
    p = p.T
  p_ = p.sum(axis=1)
  return entropy(p_) - conditional_entropy(p)

p = data / data.sum()
p = p.T
p_y = p.sum(axis=1)

print "Entropy H(Y) = ", entropy(p_y)  
print "Conditional-Entropy H(Y|X) = ",  conditional_entropy(p)
print "Information Gain I(Y; X) = H(Y) - H(Y|X) =", information_gain(p)

