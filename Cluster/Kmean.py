import self
import pandas as pd

from LabelEncoding.LabelEncode import dd
from sklearn.cluster import KMeans


for i in range(0,8):
    kn=KMeans(n_clusters=i, init='k-means++',random_state=55)

print('----------------Fit the label Encoded data with cluster------------')

print(kn.fit(dd))

print('----------------find the best parameters for cluster--------------')

print(kn.get_params)

print('--------------------print the label----------------------------')



kmean=KMeans(n_clusters=7, init='k-means++', random_state=55)

print('-----------------fit the label encoding data to cluster----------------')

print(kmean.fit(dd))

print('---------------create object/variable for label data------------------')

label=kmean.labels_

print('-------------------get labels from cluster method----------------------')

print(label)

dk=pd.DataFrame(label,columns=['labels'])
print('------------labels data------------------')
print(dk.head())

print('----------concat the label encoding data with cluster data--------------')

ds=pd.concat([dd,dk],axis=1)

print('-----------both combined data--------------')

print(ds.head())

cl0=ds[ds['labels']==0]

print('----------printing cl0 data---------')
print(cl0.head())
print('------shape of cl0 data-------')
print(cl0.shape)

cl1=ds[ds['labels']==1]

print('----------printing cl1 data------------')
print(cl1.head())
print('------shape of cl1 data-------')
print(cl1.shape)

cl2=ds[ds['labels']==2]

print('----------printing cl2 data------------')
print(cl2.head())
print('----------shape of cl2 data------------')
print(cl2.shape)

cl3=ds[ds['labels']==3]

print('--------printing of cl3 data---------------')
print(cl3.head())
print('--------shape of cl3 data------------')
print(cl3.shape)

cl4=ds[ds['labels']==4]

print('-----------printing of cl4 data--------------')
print(cl4.head())
print('----------shape of cl4 data-------------')
print(cl4.shape)

cl5=ds[ds['labels']==5]

print('-----------printing of cl5 data------------')
print(cl5.head())
print('---------shape of cl5 data--------------')
print(cl5.shape)

cl6=ds[ds['labels']==6]

print('-------printing of cl6 data------------')
print(cl6.head())
print('---------shape of cl6 data--------------')
print(cl6.shape)
