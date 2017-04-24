# Random Forest Classification

from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier


with open('D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/dataSet.csv', 'r') as file:
		csv_reader = reader(file)
		array = csv_reader.values
		X = array[:,0:1]
		Y = array[:,2]
seed = 7
num_trees = 100
max_features = 3
kfold = model_selection.KFold(n_splits=10, random_state=seed)
model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
results = model_selection.cross_val_score(model, X, Y, cv=kfold)
print(results.mean())