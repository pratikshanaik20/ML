from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.datasets import make_classification

x,y=make_classification(
    n_samples=1000,n_features=30,n_informative=15,n_classes=2,random_state=80)

c_space=np.logspace(-5,8,15)
param_grid={'C':c_space}

logreg= LogisticRegression()

logreg_cv=GridSearchCV(logreg,param_grid,cv=5)

logreg_cv.fit(x,y)

print("tuned logistic regression parameters:",format(logreg_cv.best_params_))
print("best score is{}",format(logreg_cv.best_score_))