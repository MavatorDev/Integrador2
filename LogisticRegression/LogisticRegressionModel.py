import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sb
#%matplotlib inline

dataframe = pd.read_excel('./input/clasificasion.xlsx')
#print(dataframe.head())
#print(dataframe.head())
#dataframe.describe()
	
#numero de cada categoria
#print(dataframe.groupby('clasificador').size())

#visualizo los datos
#dataframe.drop(['clasificador'],1).hist()
#plt.show()

#grafico de las variables
#sb.pairplot(dataframe.dropna(), hue='clasificador', height=8,vars=["s_TExt_SWC", "s_TExt_NWF","s_Tr_AmbC","s_TRet_AmbF",
#"h_Cap_ChF", "h_Cap_ChC", "h_Cap_Ch1", "h_Cap_Ch2"], kind='reg')

#Eliminacion de datos no necesarios del Data Frame
#dataframe1 = dataframe.drop(['tStart'], 1)
#print(dataframe1.head())
#Construccion de "X" (independiente) y "y" (dependiente) 
dfm = dataframe.drop(['clasificador', 'tStart'], 1)
#   print(dfm.head())
X = dfm
y = dataframe['clasificador']

#comprobacion de dimension
#print(X.shape)

#construccion del modelo de regresion
model = linear_model.LogisticRegression(max_iter=500)
model = model.fit(X,y)

#Prediccion acorde a los datos anteriores
#predictions = model.predict(X)
#print(predictions[:])#[0:5]
#print(dataframe['clasificador'])

#print(model.score(X,y))
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, y, test_size=validation_size, random_state=seed)

name='Logistic Regression'
kfold = model_selection.KFold(n_splits=10, random_state=seed)
cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
print(msg)

predictions = model.predict(X_validation)
print('\n')
print(accuracy_score(Y_validation, predictions))
print('\n')
print(confusion_matrix(Y_validation, predictions))

print(f1_score(Y_validation, predictions, average='weighted'))