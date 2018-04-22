import math as m
import numpy as np
import pandas as pd

train = pd.read_csv('dataset/train.csv')

dataset_train = train[['GrLivArea', 'SalePrice']]

X_train = dataset_train.iloc[:, 0].values #area de estar
Y_train = dataset_train.iloc[:, 1].values #preço


###Média amostral
media_amostral_x = np.sum(X_train)/X_train.size
media_amostral_y = np.sum(Y_train)/Y_train.size

###Variância amostral
aux = [m.pow(x - media_amostral_x, 2) for x in X_train]
variancia_amostral_x = np.sum(aux)/X_train.size

aux = [m.pow(y - media_amostral_y, 2) for y in Y_train]
variancia_amostral_y = np.sum(aux)/Y_train.size

###Desvio padrão
desvio_padrao_x = m.sqrt(variancia_amostral_x)
desvio_padrao_y = m.sqrt(variancia_amostral_y)

###Covariância amostral
aux = 0
for x in X_train:
    aux += (x - media_amostral_x) * (x - media_amostral_x)
covXX = aux/X_train.size

aux = 0
for y in Y_train:
    aux += (y - media_amostral_y) * (y - media_amostral_y)
covYY = aux/X_train.size

aux = 0
for x,y in zip(X_train,Y_train):
    aux += (x - media_amostral_x) * (y - media_amostral_y)
covXY = aux/X_train.size

covariancia_amostral = pd.DataFrame({'X': [covXX, covXY], 'Y':[covXY, covYY]})
covariancia_amostral = covariancia_amostral.rename(index={0: 'X', 1: 'Y'})

#coeficiente de correlação amostral
coeficiente_correlacao_amostral = covariancia_amostral/(desvio_padrao_x * desvio_padrao_y)

del aux
del covXX
del covYY
del covXY
del x
del y
del train
del dataset_train