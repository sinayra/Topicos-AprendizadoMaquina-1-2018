
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

train = pd.read_csv('dataset/train.csv')
test = pd.read_csv('dataset/test.csv')
sample = pd.read_csv('dataset/sample_submission.csv')

test_sample = test.join(sample.set_index('Id'), on='Id') #juntando preços com outras informações

dataset_train = train[['GrLivArea', 'SalePrice']]
dataset_test = test_sample[['GrLivArea', 'SalePrice']]

X_train = dataset_train.iloc[:, :-1].values #ano
Y_train = dataset_train.iloc[:, 1].values #preço

X_test = dataset_test.iloc[:, :-1].values #ano
Y_test = dataset_test.iloc[:, 1].values #preço

### Treinamento ###

#gráficos
plt.scatter(X_train, Y_train, color = 'red')

plt.title('Área da sala de estar vs Preço (train)')
plt.xlabel('Área')
plt.ylabel('Preço')
plt.show()

### Teste ###

#gráficos
plt.scatter(X_test, Y_test, color = 'red')

plt.title('Área da sala de estar vs Preço (test)')
plt.xlabel('Área')
plt.ylabel('Preço')
plt.show()