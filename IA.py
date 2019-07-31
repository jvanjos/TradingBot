import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
import numpy as np
import pickle

dataset = pd.read_csv('Class5c15m.csv')
dataset = dataset.drop('Unnamed: 0', axis=1)

linha = dataset.shape[0]
coluna = dataset.shape[1] - 1

gb = 0

#print(dataset.columns)
#variaveis = ['Abertura', 'Maximo', 'Minimo', 'Fechamento', 'Abertura.1', 'Maximo.1', 'Minimo.1', 'Fechamento.1']
#x = dataset[variaveis]
#y = dataset['Fechamento.2']
#print(x.head())
#print(y.head())


x = dataset.iloc[:, 0:coluna-3].values
y = dataset.iloc[:, coluna].values

#print(dadosTrei)
#print(Fechamento)



X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0, shuffle=False)



#regressor = RandomForestRegressor(n_estimators=100, random_state=0)
#regressor.fit(X_train, y_train)
#y_pred = regressor.predict(X_test)
lr_list = [0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1]

for learning_rate in lr_list:
    gb = GradientBoostingClassifier(n_estimators=100, learning_rate=learning_rate, max_features=2, max_depth=2, random_state=0)
    gb.fit(X_train, y_train)

    print("Learning rate: ", learning_rate)
    print("Accuracy score (training): {0:.3f}".format(gb.score(X_train, y_train)))
    print("Accuracy score (validation): {0:.3f}".format(gb.score(X_test, y_test)))


y_pred = gb.predict(X_test)


#gb = GradientBoostingClassifier(n_estimators=100, learning_rate = 0.5, random_state = 0)
#gb.fit(X_train, y_train)
#y_pred = gb.predict(X_test)
#print(X_test)
#teste = [[0,2,-2,2,3,4,-1,1]]
#y_pred = gb.predict(teste)
#print(y_pred)
#print('Mean Absolute Error:', metrics.mean_absolute_error(y_pred, y_test))
#print('Mean Squared Error:', metrics.mean_squared_error(y_pred, y_test))
#print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_pred, y_test)))
#filename = 'GBC3c1m.sav'
#pickle.dump(gb, open(filename, 'wb'))
np.savetxt("testePred.csv", y_test, delimiter=",")
np.savetxt("Pred.csv", y_pred, delimiter=",")



