#!/usr/bin/env python



# 1. State the question and determine the required data

# Teatro Real HVAC System Data-based Simulator Model Ver. 0
# The outputs are intended to provide the fitness score to the MO algorithm:
#   - Comfort, Consumed energy, Cost & Performance (COP)
#   - Variance of temperature and time before the show when the goal is reached
# ????? The model is to simulate the start up of the engines until Tr reaches T0
# (It can also work with any event that requires a change in the capacities)
# Necessary inputs are each chiller capacity (%), the OM, and OM' start time

# Project framework libraries selection
#   Jupyter notebook Server, Ver. 5.7.8
#   Current Kernel Information: Python 3.7.3

# Python core - Vectors, Matrices & Dates
#   - Python 3.7.6rc1 
#   - pandas 0.25.3
import pandas as pd
import numpy as np

# Data analysis:
#   - To split dataset
#   - To build Random Forest Regressor
#   - To build MLP
#   - For Grid search, tuning hyper-parameters of an estimator 
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from pandas import ExcelWriter


# Unlimited # of displayed columns
pd.options.display.max_columns = None




#Building the model architecture
#     Random Forest Regressor parameters
#       bootstrap = True
#       criterion = 'mse' (or 'mae')
#       max_depth (of a tree) = None
#       max_features = 'auto' ('int', 'float', 'sqrt', 'log2')
#       max_leaf_nodes = None ('int')
#       min_impurity_decrease = 0.0
#       min_samples_leaf (node) = 1
#       min_samples_split (of an internal node) = 2
#       min_weight_fraction_leaf (node) = 0.0
#       n_estimators = 10 (or 100?), number of trees
#       n_jobs = 2 (parallel running)
#       oob_score = True (out of bag samples to estimate R2 on unseen data)
#       random_state (of the bootstraping) = None
#       verbose (when fitting and predicting) = 0 
#       warm_start = False
#     Attributes
#       base_estimator_: Child estimator template, collecting fitted sub-estim.
#       estimators_: collection of fitted sub-estimators.
#       feature_importances_: feature importances, the higher, the more important
#       n_features_: number of features when fit is performed
#       n_outputs_: number of outputs when fit is performed.
#       oob_score_: Score of the training dataset with an out-of-bag estimate
#       oob_prediction_: Prediction with out-of-bag estimate

forestAux = RandomForestRegressor(
    bootstrap = True,
    criterion = 'mse',
    max_depth = None,
    max_features = 'auto',
    max_leaf_nodes = None,
    min_impurity_decrease = 0.0,
    min_impurity_split = None,
    min_samples_leaf = 1,
    min_samples_split = 2,
    min_weight_fraction_leaf = 0.0,
    n_estimators = 30,
    n_jobs = 2,
    oob_score = True,
    random_state = None,
    verbose = 0,
    warm_start = False)
#Random Forest Model learning
x = pd.read_excel('input/predictors.xlsx')
x = x.drop(['Time', 'TExt', 'T0', 'People', 'Tr', 'month', 'day', 'hour', 'Interval'], axis=1)[:len(x)]

y = x[ [ 's_Tr_AmbC', 's_Tr_CrcC', 's_Tr_CrcF', 's_Tr_FyrF', 's_Tr_GdF', 's_Tr_GoyaF', 's_Tr_Hal1F', 's_Tr_PitF', 
's_Tr_StdsC', 's_Tr_StdsF', 's_TRet_AmbF', 's_TRet_StllC', 's_TRet_StllF', 'z_Tr_AmbC', 'z_Tr_GyrreC', 'z_Tr_HalSAPAF', 
'z_Tr_OrchReheF', 'z_Tr_Sng4', 'z_TRet_Bllt', 'z_TRet_Choir', 'z_TRet_CrcC', 'z_TRet_CrcF', 'z_TRet_Hal6F', 'z_TRet_OffiF', 
'z_TRet_R14', 'z_TRet_Store', 'z_TRet_Tech' ] ]

x = x.dropna().iloc[0:3371]
y = y.dropna().iloc[1:]

#print(y.columns)
#print(x.columns)

forestAux.fit(x,y)

def predecir(lista):
    return forestAux.predict([lista])