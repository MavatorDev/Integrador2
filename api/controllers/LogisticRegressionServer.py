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
from RegresionAux import predecir
from ModuloOptimizacion import mopso

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
        #print('lei')
        dataframe = pd.read_excel('./input/predictors.xlsx')
        Text =  dataframe[['TExt', 'T0', 'People', 'Tr', 'month', 'day', 'hour', 'Interval']]
        Text = Text.iloc[0, :]
        print('temperatura')
        dataframe = dataframe[['s_Tr_AmbC', 's_Tr_CrcC', 's_Tr_CrcF', 's_Tr_FyrF', 's_Tr_GdF', 's_Tr_GoyaF', 's_Tr_Hal1F', 's_Tr_PitF', 
        's_Tr_StdsC', 's_Tr_StdsF', 's_TRet_AmbF', 's_TRet_StllC', 's_TRet_StllF', 'z_Tr_AmbC', 'z_Tr_GyrreC', 'z_Tr_HalSAPAF', 
        'z_Tr_OrchReheF', 'z_Tr_Sng4', 'z_TRet_Bllt', 'z_TRet_Choir', 'z_TRet_CrcC', 'z_TRet_CrcF', 'z_TRet_Hal6F', 'z_TRet_OffiF', 
        'z_TRet_R14', 'z_TRet_Store', 'z_TRet_Tech']]
        dataframe = dataframe.dropna(axis = 0)
        print('mopso')
        solution = mopso(Text)
        print(solution)
        #print(dataframe.iloc[0,:].values.tolist())
        predicion = predecir(solution['cap'] + dataframe.iloc[0,:].values.tolist())
        predicion = predicion.__getitem__(0)
        print(predicion)
        predicion1 = pd.DataFrame()
        predicion1['s_Tr_AmbC'] = predicion.__getitem__(0)
        predicion1['s_Tr_CrcC'] = predicion.__getitem__(1)
        predicion1['s_Tr_CrcF'] = predicion.__getitem__(2)
        predicion1['s_Tr_FyrF'] =predicion.__getitem__(3)
        predicion1['s_Tr_GdF'] =predicion.__getitem__(4)
        predicion1['s_Tr_GoyaF'] = predicion.__getitem__(5)
        predicion1['s_Tr_Hal1F'] = predicion.__getitem__(6)
        predicion1['s_Tr_PitF'] = predicion.__getitem__(7)
        predicion1['s_Tr_StdsC'] = predicion.__getitem__(8)
        predicion1['s_Tr_StdsF'] = predicion.__getitem__(9)
        predicion1['s_TRet_AmbF'] = predicion.__getitem__(10)
        predicion1['s_TRet_StllC'] = predicion.__getitem__(11)
        predicion1['s_TRet_StllF'] = predicion.__getitem__(12)
        predicion1['z_Tr_AmbC'] = predicion.__getitem__(13)
        predicion1['z_Tr_GyrreC'] = predicion.__getitem__(14)
        predicion1['z_Tr_HalSAPAF'] = predicion.__getitem__(15)
        predicion1['z_Tr_OrchReheF'] = predicion.__getitem__(16)
        predicion1['z_Tr_Sng4'] = predicion.__getitem__(17)
        predicion1['z_TRet_Bllt'] = predicion.__getitem__(18)
        predicion1['z_TRet_Choir'] = predicion.__getitem__(19)
        predicion1['z_TRet_CrcC'] = predicion.__getitem__(20)
        predicion1['z_TRet_CrcF'] = predicion.__getitem__(21)
        predicion1['z_TRet_Hal6F'] =predicion.__getitem__(22)
        predicion1['z_TRet_OffiF'] =predicion.__getitem__(23)
        predicion1['z_TRet_R14'] =predicion.__getitem__(24)
        predicion1['z_TRet_Store'] =predicion.__getitem__(25)
        predicion1['z_TRet_Tech']=predicion.__getitem__(26)
        predicion1['setPoint'] = 23.5
        #predicion1.iloc[0, -1] =predicion.__getitem__(0)
        #print(predicion1.head())
        print(self.executeModel(predicion1))

    def look(self):
        l = task.LoopingCall(takeTemperature())
        l.start(900)
        reactor.run()


principal = logistic()
principal.chargeDataInitial()
principal.takeTemperature()