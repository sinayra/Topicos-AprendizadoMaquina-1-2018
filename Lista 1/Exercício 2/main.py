
import numpy as np
import pandas as pd


train = pd.read_csv('dataset/train.csv')

dataset_train = train[['GrLivArea', 'SalePrice']]

X_train = dataset_train.iloc[:, 0].values #area de estar
Y_train = dataset_train.iloc[:, 1].values #preço


media_amostral_x = np.mean(X_train)
media_amostral_y = np.mean(Y_train)
variancia_amostral_x = np.var(X_train)
variancia_amostral_y = np.var(Y_train)
desvio_padrao_x = np.std(X_train)
desvio_padrao_y = np.std(Y_train)
covariancia_amostral = np.cov(X_train, Y_train)
covariancia_amostral = pd.DataFrame(covariancia_amostral)
covariancia_amostral.columns = ['X', 'Y']
covariancia_amostral = covariancia_amostral.rename(index={0: 'X', 1: 'Y'})
# cov(X, X)   cov(X, Y)
# cov(Y, X)   cov(Y, Y)
coeficiente_correlacao_amostral = covariancia_amostral/(desvio_padrao_x * desvio_padrao_y)