import self
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,Normalizer,OneHotEncoder,RobustScaler,StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import cross_validate,KFold,RandomizedSearchCV,GridSearchCV,train_test_split
from Cluster.Kmean import cl0,cl1,cl2,cl3,cl4,cl5,cl6

print('-------- cluster cl0 data-----')
print(cl0.head())
print('------- cluster cl0 columns ----------')
print(cl0.columns)
print('---- split the cl0 data into x,y --------')

x=cl0.drop(columns=['prognosis_n', 'labels'])
y=cl0['prognosis_n']

print('----- cluster cl0 x data -----------')
print(x.head())
print('------ cluster cl0 shape data ------------')
print(x.shape)
print('------ cluster cl0 y data ---------------')
print(y.head())
print('------ cluster cl0 shape data ----------')
print(y.shape)

print('-------- Applying Standard Scaling to cl0 data -----------')

scale=StandardScaler()
x_scale=scale.fit_transform(x)

print('---------- print the x_scale data ----------')
print(x_scale)

print('------- VIF ------------')
var=x_scale
vif=pd.DataFrame()
vif['VIF']=[variance_inflation_factor(var,i) for i in range(var.shape[1])]
vif['Features']=x.columns
print(vif)


print('------- split the x,y data into train and test data -----------')

x_train,x_test,y_train,y_test=train_test_split(x_scale,y,test_size=0.20,random_state=55)

print('------ cl0 x_train data -------')
print(x_train)
print('----- cl0 x_test data -----------')
print(x_test)
print('------ cl0 y_train data -----------')
print(y_train)
print('------- cl0 y_test data ----------')
print(y_test)


print('------- cluster cl1 data ---------')
print(cl1.head())
print('------- cl1 columns --------')
print(cl1.columns)

print('------- split the data into x1 and y1 ---------')
x1=cl1.drop(columns=['prognosis_n', 'labels'])
y1=cl1['prognosis_n']

print('---- cluster cl1 x1 data -----')
print(x1.head())
print('---- x1 shape data -----')
print(x1.shape)

print('---- cluster cl1 y1 data -----')
print(y1.head())
print('---- y1 shape data -----')
print(y1.shape)


print('---- Applying Standard Scaler on x1 data -----')
scale1=StandardScaler()
print('--- fit and transfer the x1 data ------')
x1_scale=scale1.fit_transform(x1)
print('----- print x1_scale data ------')
print(x1_scale)


print('---- Split the data into x1_train,x1_test,y1_train,y1_test -------')
x1_train,x1_test,y1_train,y1_test=train_test_split(x1_scale,y1,test_size=0.20,random_state=65)


print('----- print x1_train data -----')
print(x1_train)
print('----- print x1_test data ------')
print(x1_test)
print('----- print y1_train ------')
print(y1_train)
print('----- print y1_test data ------')
print(y1_test)






