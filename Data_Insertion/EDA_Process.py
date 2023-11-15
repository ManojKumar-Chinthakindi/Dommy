import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import AdaBoostClassifier,BaggingClassifier,ExtraTreesClassifier,GradientBoostingClassifier,RandomForestClassifier,StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,auc,confusion_matrix,log_loss,plot_roc_curve,roc_auc_score,roc_curve
from sklearn.model_selection import cross_validate,KFold,RandomizedSearchCV,GridSearchCV,train_test_split
from sklearn.naive_bayes import BernoulliNB,ComplementNB,GaussianNB
from sklearn.neighbors import KNeighborsClassifier,NearestNeighbors
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler,Normalizer,OneHotEncoder,RobustScaler,StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier,ExtraTreeClassifier
from statsmodels.stats.outliers_influence import variance_inflation_factor


df=pd.read_csv('E:\iNeuron\ML\Apple Project\Apple_Chronic_Disease_Prediction\Data_Insertion\Chronic_Data.csv')
class Eda_Data:
    def __init__(self,df):
        self.df=df
        print(df.head())
        print(df)
        print(df.tail())
        print(df.columns)
        print(df.count())
        print(df.describe())
        print(df.dtypes)
        print(df.empty)
        print(df.index)
        print(df.info)
        print(df.isnull().sum())
        print(df.items())
        print(df.kurtosis())
        print(df.max())
        print(df.mean())
        print(df.median())
        print(df.mode(axis=1))
        print(df.min())
        print(df.ndim)
        print(df.pivot_table)
        print(df.quantile(q=0.25))
        print(df.quantile(q=0.50))
        print(df.quantile(q=0.75))
        print(df.shape)


Eda_Data(df)





