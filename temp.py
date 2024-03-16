# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np # used for handling numbers
import pandas as pd # used for handling the dataset

from sklearn.impute import SimpleImputer # used for handling
# missing data

from sklearn.model_selection import train_test_split
# used for splitting training and testing data

from sklearn.preprocessing import StandardScaler
#used for feature scaling
#%%
dataset = pd.read_csv('C:/Users/COMICCODER/Desktop/machineLearn/Data.csv') # to import dataset into a variable

#splitting the attributes into independent and dependent attributes
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values

#%%
dataset

#%%
#encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features[0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)