# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 22:01:40 2019

@author: Shrishti D Hore
"""

from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#load the data
telescope=pd.read_csv('‪C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\gamma.csv')

#clean the data
telescope_shuffle=telescope.iloc[np.random.permutation(len(telescope))]
tele=telescope_shuffle.reset_index(drop=True)

#store 2 classes
tele['Class']=tele['Class'].map({'g':0,'h':1})
tele_class = tele['Class'].values

#split training, testing and validation data
training_indices, validation_indices = training_indices, testing_indices = train_test_split(tele.index, stratify = tele_class, trian_size = 0.75, test_size=0.25)

#let genetic programming find the best ML model and hyperparameters
tpot = TPOTClassifier(generations = 5, verbosity = 2)
tpot.fit(tele.drop('Class', axis = 1).loc[training_indices].values, tele.loc[training_indices, 'Class'].values)

#score the accuracy
tpot.score(tele.drop('Class',axis=1).loc[validation_indices].values, tele.loc[validation_indices, 'Class'].values)

#export the generated code
tpot.export('pipeline.py')
