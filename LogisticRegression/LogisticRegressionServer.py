import pandas as pd
import numpy as np
import sched, time
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sb
from time import time
import random
import sched, time
from twisted.internet import task
from twisted.internet import reactor

from Integrador2.optimización.ModuloOptimizacion import op

#app = Flask(__name__)


class logistic:

    def __init__(self):
        super().__init__()
        self.model = 0 
    def chargeDataInitial(self):
        dataframe = pd.read_excel('./input/clasificasion.xlsx')
        dfm = dataframe.drop(['clasificador', 'tStart'], 1)
        X = dfm
        y = dataframe['clasificador']
        self.model = linear_model.LogisticRegression(max_iter=500)
        self.model = self.model.fit(X,y)
    
    def executeModel(self, X):
        prediction = self.model.predict(X)
        return prediction

    def takeTemperature(self):
        pass

    def look(self):
        l = task.LoopingCall(takeTemperature())
        l.start(900)
        reactor.run()