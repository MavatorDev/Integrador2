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

#hvacs_raw = pd.read_excel('./input/tr_hvacs.xlsx')
zones = pd.read_excel('./input/tr_zones.xlsx')
setPoint = 23.5

'''hvacs =   hvacs_raw[
    ['Date',
    'h_Cap_Ch1', 
    'h_Cap_Ch2', 
    'h_Cap_ChC', 
    'h_Cap_ChF'
    ]
]'''


#df2 = pd.DataFrame()
#df2 = zones
#print(df2.count)
#Selecciona el periodo de observacion
zones = zones[(zones['Date'] >= '2016-09-11') & (zones['Date'] < '2018-01-01')] 

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
idx = pd.date_range('2016-09-11', '2018-03-24 23:50', freq = '10T')
zones = zones.reindex(idx).interpolate(method = 'linear')

#  Merging tables in one data frame, 'df'
df = pd.DataFrame()
df = zones.merge(zones, left_index = True, right_index = True)


#  Recovering 'Date' as data with new name, 'tStart'
df = df.reset_index()
df = df.rename(columns = {'index':'tStart'})

df['setPoint'] = setPoint
df['clasificador'] = 1

#print(df.count)

df_changes = df.drop(['tStart', 'setPoint', 'clasificador'], 1)

#
#print(df_changes.dtypes)

beforeMean = 0
countForFails = 1
countForFails2 = 1
clasificacion = []
#setpoinst = [20.3, 15.6, 27.5, 18.9]
#aux = 0
#setPoint = randint(0, 3)
"""for indice_fila, fila in df.iterrows():
    if aux >= 72:
        aux = 0
        setPoint = randint(0, 3)
    df.iloc[indice_fila, -2] = setpoinst.__getitem__(setPoint)
    aux = aux+1

print(df.head())"""



for indice_fila, fila in df_changes.iterrows():
    if indice_fila == 0:
        fila.abs()
        meanRow = fila.mean()
        beforeMean = meanRow
        clasificacion.append(1)

    if indice_fila > 0:
        fila.abs()
        meanRow = stats.mean(fila)
        if beforeMean >= setPoint:
            #print(meanFila)
            if ((meanRow < beforeMean) & (countForFails == 1)):
                clasificacion.append(1)
                beforeMean = meanRow
                countForFails = 1
            elif ((meanRow >= beforeMean) & (countForFails == 1)):
                clasificacion.append(1)
                beforeMean = beforeMean
                countForFails = countForFails + 1    
            elif ((meanRow >= beforeMean) & (countForFails == 2)):
                clasificacion.append(0)
                countForFails = 1
                beforeMean = meanRow
            elif ((meanRow < beforeMean) & (countForFails ==2)):
                countForFails = 1
                beforeMean = meanRow
                clasificacion.append(0) 
        elif beforeMean < setPoint:
            #print(meanFila)
            if ((meanRow > beforeMean) & (countForFails == 1)):
                clasificacion.append(1)
                beforeMean = meanRow
                countForFails = 1
            elif ((meanRow <= beforeMean) & (countForFails == 1)):
                clasificacion.append(1)
                beforeMean = meanRow
                countForFails = countForFails + 1    
            elif ((meanRow <= beforeMean) & (countForFails == 2)):
                clasificacion.append(0)
                countForFails = 1
                beforeMean = meanRow 
            elif ((meanRow > beforeMean) & (countForFails ==2)):
                countForFails = 1
                beforeMean = meanRow
                clasificacion.append(0) 


for indice_fila, fila in df.iterrows():
    df.iloc[indice_fila, -1] = clasificacion.__getitem__(indice_fila)


#print(df.head())
#print(df_changes.count)
#print(clasificacion)
writer = ExcelWriter('clasificasion.xlsx')
df.to_excel(writer, 'Hoja de datos', index=False)
writer.save()
