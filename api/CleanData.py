import pandas as pd
import numpy as np
from pandas import ExcelWriter
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sb
from random import randint, uniform,random
import statistics as stats
#%matplotlib inline


zones = pd.read_excel('./input/tr_zones.xlsx')
setPoint = 23.5

#Selecciona el periodo de observacion
zones = zones[(zones['Date'] >= '2016-09-11') & (zones['Date'] < '2018-04-06')] 

#writer = ExcelWriter('s1.xlsx')
#hvacs.to_excel(writer, 'Hoja de datos', index=False)
#writer.save()

#Remueve ceros
zones = zones.loc[:, (zones != 0).any(axis = 0)]

"""writer = ExcelWriter('s.xlsx')
shows.to_excel(writer, 'Hoja de datos', index=False)
writer.save()"""

zones = zones.set_index(['Date'])

#Re-sampling to 10min & re-filling, with linear interpolation
idx = pd.date_range('2016-09-11', '2018-04-05 23:00', freq = '60T')
zones = zones.reindex(idx).interpolate(method = 'linear')
#zones = zones.reindex(idx).fillna(method = 'pad', limit = 1)

#  Merging tables in one data frame, 'df'
#zones = zones.columns[0:11]

df = pd.DataFrame()
df = zones
#df = zones#.merge(zones, left_index = True, right_index = True)

#  Recovering 'Date' as data with new name, 'tStart'
df = df.reset_index()
df = df.rename(columns = {'index':'tStart'})

df = df[['tStart', 'z_TRet_Tech', 'z_TRet_Store', 'z_TRet_StoreA', 'z_TRet_BxC', 'z_TRet_BxF', 'z_TRet_PitF', 'z_TRet_DrssF',
        'z_Tr_GoyaF', 'z_TRet_R14', 'z_Tr_GoyaF.1', 'z_TRet_OffiF', 'z_TRet_OffiC', 'z_TRet_CfeC', 'z_TRet_CfeF', 'z_TRet_PortalC',
        'z_TRet_PortalF', 'z_TRet_Hal6F', 'z_TRet_HalC', 'z_TRet_CrcC', 'z_Tr_Cfe', 'z_Tr_HalSAPAF', 'z_TRet_CrcF', 'z_TRet_OffiC.1', 
        'z_TRet_OffiF.1', 'z_TRet_RegF', 'z_TRet_StringF', 'z_Tr_OrchOffiF']]

df['setPoint'] = setPoint
df['clasificador'] = 1
df_changes = df.drop(['setPoint', 'clasificador', 'tStart'], 1)

beforeMean = 0
clasificacion = []

for indice_fila, fila in df_changes.iterrows():
    if indice_fila == 0:
        #fila.abs()
        meanRow = fila.mean()
        beforeMean = meanRow
        clasificacion.append(1)

    if indice_fila > 0:
        #fila.abs()
        meanRow = stats.mean(fila)
        if meanRow == 0:
            beforeMean = beforeMean
            clasificacion.append(1)
        elif beforeMean >= setPoint:
            #print(meanFila)
            if (meanRow < beforeMean): #& (countForFails == 1)):
                clasificacion.append(1)
                beforeMean = meanRow
                #countForFails = 1
            elif (meanRow >= beforeMean): #& (countForFails == 1)):
                clasificacion.append(0)
                beforeMean = meanRow
                #countForFails = countForFails + 1    
            """elif ((meanRow >= beforeMean) & (countForFails == 2)):
                clasificacion.append(0)
                countForFails = 1
                beforeMean = meanRow
            elif ((meanRow < beforeMean) & (countForFails ==2)):
                countForFails = 1
                beforeMean = meanRow
                clasificacion.append(0)""" 
        elif beforeMean < setPoint:
            #print(meanFila)
            if (meanRow > beforeMean): #& (countForFails == 1)):
                clasificacion.append(1)
                beforeMean = meanRow
                #countForFails = 1
            elif (meanRow <= beforeMean): #& (countForFails == 1)):
                clasificacion.append(0)
                beforeMean = meanRow
                #countForFails = countForFails + 1    
            """elif ((meanRow <= beforeMean) & (countForFails == 2)):
                clasificacion.append(0)
                countForFails = 1
                beforeMean = meanRow 
            elif ((meanRow > beforeMean) & (countForFails ==2)):
                countForFails = 1
                beforeMean = meanRow
                clasificacion.append(0)"""


for indice_fila, fila in df.iterrows():
    df.iloc[indice_fila, -1] = clasificacion.__getitem__(indice_fila)


writer = ExcelWriter('clasificasion.xlsx')
df.to_excel(writer, 'Hoja de datos', index=False)
writer.save()
