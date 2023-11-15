import self

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from Data_Insertion.EDA_Process import df

le = LabelEncoder()

d1 = le.fit_transform(df['prognosis'])
print(d1)
print('--------------------')
d2 = pd.DataFrame(d1, columns=['prognosis_n'])
print(d2.head())
print('--------------------')
d3 = pd.concat([df, d2], axis=1)
print(d3.head())
print('--------------------')
dd =d3.drop(columns='prognosis')
print(dd.head())




