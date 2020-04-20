import pandas as pd
#import numpy as np
"""from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sb"""
#%matplotlib inline

dataframe = pd.read_excel('tr_shows.xlsx')
dataframe.head()
print(dataframe.head())
"""dataframe.describe()
	
print(dataframe.groupby('clase').size())

dataframe.drop(['clase'],1).hist()
plt.show()

sb.pairplot(dataframe.dropna(), hue='clase',size=4,vars=["duracion", "paginas","acciones","valor"],kind='reg')

X = np.array(dataframe.drop(['clase'],1))
y = np.array(dataframe['clase'])
X.shape

model = linear_model.LogisticRegression()
model.fit(X,y)

predictions = model.predict(X)
print(predictions)[0:5]

model.score(X,y)"""
