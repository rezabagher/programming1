# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zgOELxH7DYvbASorzNKCek668E6KiOmw
"""

import numpy as np
import pandas as pd 
from statsmodels.tools.eval_measures import mse

from google.colab import files
uploaded_1 = files.upload()

df = pd.read_excel('TRAIN.xlsx')
df.head()

print(df)

df1=df.drop(['Perovskite composition','Ionization_energy_a','Ionization_energy_b'], axis=1)
df2=df['Ionization_energy_a']
df3=df['Ionization_energy_b']
print(df1)

pip install pandas-profiling

import pandas as pd
from pandas_profiling import ProfileReport

profile = ProfileReport(df)

profile.to_notebook_iframe()

from sklearn.decomposition import PCA
# Perform PCA 
pca = PCA(n_components=1)
X_pca = pca.fit_transform(df1)

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(df1.to_numpy(), df.Ionization_energy_a)

import numpy as np
import matplotlib.pyplot as plt
plt.scatter(X_pca,df.Ionization_energy_a)

from google.colab import files
uploaded_2 = files.upload()

test=pd.read_excel('Suplemmentry_data_1(test).xlsx')
test.head()

df4=test.drop(['Perovskite composition','Ionization_energy_b','Ionization_energy_a'], axis=1)
df5=test['Ionization_energy_a']
df6=test['Ionization_energy_b']

y_pred = model.predict(df4.to_numpy())

model.score(df4,df5)

print(y_pred)

X_pca_test = pca.fit_transform(df4)

sns.scatterplot( y_pred)
sns.scatterplot(df5)

plt.scatter(X_pca_test,y_pred)

print(mse(y_pred,df5))

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(df1,df2 )

from sklearn import svm
h1=svm.SVR()
h1.fit(df1,df2)

import seaborn as sns
sns.set()

#model evaluation
y_pred_svr=h1.predict(df4)

sns.scatterplot( y_pred_svr)
sns.scatterplot(df5)

a = model.intercept_
b = model.coef_[0]

plt.scatter(X_pca_test,y_pred_svr)

print(mse(y_pred_svr,df5))

h1.score(df4,df5)

#ANN

from sklearn.neural_network import MLPRegressor

nn=MLPRegressor(hidden_layer_sizes=(100,100,100), activation='tanh', max_iter=100)
nn.fit(df1,df2)

y_pred_ann=nn.predict(df4)

print(mse(y_pred_ann,df5))

nn.score(df4,df5)

sns.scatterplot( y_pred_ann)
sns.scatterplot(df5)