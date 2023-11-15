import self
from Preprocessing.Preproce import x_train,x_test,y_train,y_test
from Preprocessing.Preproce import x1_train,x1_test,y1_train,y1_test
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier



print('---- applying RandomForest Algorithm -------')
rf=RandomForestClassifier()

print('------ parameters for RandomForest -----------')
parmr={'n_estimators':[10,20,30,40,50,60,70,80,90,100],'criterion':['gini','entropy','log_loss'], 'max_depth':range(2,4,1), 'max_features':['sqrt','log2']}

print('----- passing parameters in GridSearchCV ----------')
gridr=GridSearchCV(rf,param_grid=parmr,cv=5,verbose=5)

print('------- fit the x_train and y_test data ------')
gridr.fit(x_train,y_train)

print('----- best parameters for RandomForest --------')
print(gridr.best_params_)

print('------- Again Applying RandomForest Algorithm with best hyperparameters ------------')
randfor=RandomForestClassifier(criterion= 'gini', max_depth= 2, max_features= 'sqrt', n_estimators= 40)

print('---- fit the x_train and y_train data with RandomForest ---------')
randfor.fit(x_train,y_train)

print('--------- Creating Variable for predict ---------')
y_pred=randfor.predict(x_test)

print('------ Calculate the Accuracy of the RandomForest Algorithm ---------')
accr=accuracy_score(y_test,y_pred)

print('------ print the Accuracy Rate for RandomForest ---------')
print(accr)


print('----------- SVC Algorithm --------------')
sv=SVC(C= 1.0,decision_function_shape= 'ovr',degree= 3,gamma= 'scale',kernel= 'rbf',max_iter= -1)

print('------ fit the x_train and y_train data with sv ---------')
sv.fit(x_train,y_train)

print('-------- Creating Variable for predict for sv ------')
y_presv=sv.predict(x_test)

print('--------- Calculate the Accuracy of SVC ---------')
accsv=accuracy_score(y_test,y_presv)

print('------- Final Accuracy for SVC -----------')
print(accsv)


if accr>accsv:
    print('RandomForest is the best fit Algorithm for this Data')
elif accr<accsv:
    print('SVC is the best fit Algorithm for this Data')
else:
    print('Both RandomForest and SVC Algorithms are best fit Algorithms for this Data')



print('---- Applying different types of Algorithms on cl1 dataset ------')
lg=LogisticRegression()

parlg={'penalty':['l1', 'l2', 'elasticnet'], 'C':[1.0], 'random_state':[65], 'solver':['lbfgs', 'liblinear',' newton-cg', 'newton-cholesky', 'sag', 'saga'], 'max_iter':[100], 'multi_class':['auto','ovr']}

print('---- Applying GridSearchCV ------')
gridlg=GridSearchCV(lg,param_grid=parlg,cv=5,verbose=5)
gridlg.fit(x1_train,y1_train)


print('----- print best parameters for Logistic Regression ------')
print(gridlg.best_params_)

lgr=LogisticRegression(C= 1.0, max_iter= 100, multi_class= 'auto', penalty= 'l1', random_state= 65, solver= 'liblinear')
lgr.fit(x1_train,y1_train)

print('------ Applying Bagging method on this data ---------')
baglr=BaggingClassifier(base_estimator=lgr,n_estimators=10,max_samples=1.0,bootstrap=True,n_jobs=5,random_state=65,verbose=5)
baglr.fit(x1_train,y1_train)

print('------ Bagging accuracy rate for Logistic Regression ------')
y1_pred=baglr.predict(x1_test)

print('--------- Print Accuracy Score for Logistic Regression with Bagging method --------------')
acclr=accuracy_score(y1_test,y1_pred)
print(acclr)



det=DecisionTreeClassifier()

pardet={'criterion':['gini','entropy', 'log_loss'], 'splitter':['best','random'], 'max_depth':[2,4], 'min_samples_split':[2,4,5], 'min_samples_leaf':[1,2,3,4],  'max_features':['auto', 'sqrt', 'log2'], 'random_state':[65], 'max_leaf_nodes':[2,3,4], 'ccp_alpha':[0.0]}

girdt=GridSearchCV(det,param_grid=pardet,cv=5,verbose=5)
girdt.fit(x1_train,y1_train)

print('----- print best parameters for Decision Tree -------')
print(girdt.best_params_)


decision=DecisionTreeClassifier(ccp_alpha= 0.0, criterion= 'entropy', max_depth= 4, max_features= 'auto', max_leaf_nodes= 4, min_samples_leaf= 1, min_samples_split= 2, random_state= 65, splitter= 'best')
decision.fit(x1_train,y1_train)
y1_dec=decision.predict(x1_test)
accdec=accuracy_score(y1_test,y1_dec)

print('----- Accuracy score for Decision Tree ------')
print(accdec)


print('---------- Applying Bagging methods on our Dataset ---------')

bagdec=BaggingClassifier(base_estimator=decision,n_estimators=10,max_samples=1.0,bootstrap=True,n_jobs=5,random_state=65,verbose=5)
bagdec.fit(x1_train,y1_train)
y1_bagdec=bagdec.predict(x1_test)
print('--- best parameters for NB -----')
accbagdec=accuracy_score(y1_test,y1_bagdec)

print('---- Accuracy score for Bagging with Decision Tree ------')
print(accbagdec)


