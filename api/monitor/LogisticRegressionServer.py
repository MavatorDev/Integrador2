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
from monitor.RegressionAux import predecir
from optimization.ModuloOptimizacion import mopso
from models.optimization import saveSolution as sSol
from models.temperature import saveGeneratedTemperature as sT


class logistic:

    def __init__(self):
        super().__init__()
        self.model = 0
        self.constantValues = 0

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

    def start(self):
        dataframe = pd.read_excel('./input/predictors.xlsx')
        
        self.constantValues =  dataframe[['TExt', 'T0', 'People', 'Tr', 'month', 'day', 'hour', 'Interval']]

        self.constantValues = self.constantValues.iloc[0, :]

        dataframe = dataframe[['s_Tr_AmbC', 's_Tr_CrcC', 's_Tr_CrcF', 's_Tr_FyrF', 's_Tr_GdF', 's_Tr_GoyaF', 's_Tr_Hal1F', 's_Tr_PitF', 
        's_Tr_StdsC', 's_Tr_StdsF', 's_TRet_AmbF', 's_TRet_StllC', 's_TRet_StllF', 'z_Tr_AmbC', 'z_Tr_GyrreC', 'z_Tr_HalSAPAF', 
        'z_Tr_OrchReheF', 'z_Tr_Sng4', 'z_TRet_Bllt', 'z_TRet_Choir', 'z_TRet_CrcC', 'z_TRet_CrcF', 'z_TRet_Hal6F', 'z_TRet_OffiF', 
        'z_TRet_R14', 'z_TRet_Store', 'z_TRet_Tech']]

        dataframe = dataframe.dropna(axis = 0)

        solution = mopso(self.constantValues)
        sSol(solution)

        predicion = predecir(solution['cap'] + dataframe.iloc[0,:].values.tolist())
        sT(predicion)
        predicion = predicion[0]
        print('bien')

    """def lookWithMonitor(self):

        solution = mopso(Text)

        predicion = predecir(solution['cap'] + dataframe.iloc[0,:].values.tolist())

        dataframe = pd.DataFrame(predicion)

        dataframe.columns = ['s_Tr_AmbC', 's_Tr_CrcC', 's_Tr_CrcF', 's_Tr_FyrF', 's_Tr_GdF', 's_Tr_GoyaF', 's_Tr_Hal1F', 's_Tr_PitF', 
        's_Tr_StdsC', 's_Tr_StdsF', 's_TRet_AmbF', 's_TRet_StllC', 's_TRet_StllF', 'z_Tr_AmbC', 'z_Tr_GyrreC', 'z_Tr_HalSAPAF', 
        'z_Tr_OrchReheF', 'z_Tr_Sng4', 'z_TRet_Bllt', 'z_TRet_Choir', 'z_TRet_CrcC', 'z_TRet_CrcF', 'z_TRet_Hal6F', 'z_TRet_OffiF', 
        'z_TRet_R14', 'z_TRet_Store', 'z_TRet_Tech']
        dataframe['setPoint'] = 23.5
        self.executeModel(dataframe)

    def look(self):
        l = task.LoopingCall(takeTemperature())
        l.start(900)
        reactor.run()"""