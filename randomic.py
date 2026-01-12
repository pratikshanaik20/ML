import numpy as np
from sklearn.datasets import make_classification
X,y=make_classification( n_samples=1000,n_features=30,n_informative=15,n_classes=2,random_state=80)
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV

param_dist={
    "max_depth":[3,None],
    "max_features":randint(1,8),
    "min_samples_leaf":randint(1,7),
    "criterion":["gini","entropy"]}

tree=DecisionTreeClassifier()
tree_cv=RandomizedSearchCV(tree,param_dist,cv=5)
tree_cv.fit(X,y)

print("tuned decision tree parameters:",format(tree_cv.best_params_))
print("best score is{}",format(tree_cv.best_score_))