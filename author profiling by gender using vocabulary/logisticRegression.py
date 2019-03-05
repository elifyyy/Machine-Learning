import createFeatures as cr
from sklearn import linear_model
from sklearn.model_selection import cross_val_predict,cross_val_score

X = cr.samples
Y = cr.real_classes

logreg = linear_model.LogisticRegression(C=1e5)
y_pred = cross_val_predict(logreg, X, Y,cv=10)
score = cross_val_score(logreg,X,Y,cv=10,scoring='accuracy').mean()
