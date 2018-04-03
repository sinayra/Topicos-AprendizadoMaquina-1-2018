
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

train = pd.read_csv('dataset/train.csv')
test = pd.read_csv('dataset/test.csv')

dataset_train = train[['GrLivArea', 'SalePrice']]
dataset_test = test[['GrLivArea']]

X_train = dataset_train.iloc[:, :-1].values #ano
Y_train = dataset_train.iloc[:, 1].values #preço

### Treinamento ###

#gráficos
plt.scatter(X_train, Y_train, color = 'red')

plt.title('Área da sala de estar vs Preço (train)')
plt.xlabel('Área')
plt.ylabel('Preço')
plt.show()
