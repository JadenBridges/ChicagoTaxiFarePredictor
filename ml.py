#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:30:01 2019

@author: shreyarora
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

def kNN_prediction():
        
    # Randomly split data into 70% training and 30% test
    X_train, X_test, y_train, y_test = train_test_split(datalist, targetlist, test_size=.30)
    
    # Train a kNN model using the training set
    clf_KNN = KNeighborsClassifier()
    clf_KNN.fit(X_train, y_train)
    
    # Predictions using the kNN model on the test set
    print("Predicting labels of the test data set - %i random samples" % (len(X_test)))
    result = clf_KNN.predict(X_test)
    
    return str(accuracy_score(y_test, result))

def nb_prediction():
    
    # Randomly split data into 70% training and 30% test
    X_train, X_test, y_train, y_test = train_test_split(datalist, targetlist, test_size=.30)
    
    # Create NB classifier: 
    nb = GaussianNB()

    # Train the model
    nb.fit(X_train, y_train)
    
    # Predictions
    result = nb.predict(X_test)
    
    return str(accuracy_score(y_test, result))

def nn_prediction():
    
    # Randomly split data into 70% training and 30% test
    X_train, X_test, y_train, y_test = train_test_split(datalist, targetlist, test_size=.30)
    
    # create neural network clf model
    clf = MLPClassifier(solver='sgd', activation='logistic', 
        learning_rate_init=0.01, learning_rate='constant', max_iter=5000, verbose='true',
        hidden_layer_sizes=(5,))
    
    clf.fit(X_train, y_train)

    result = clf.predict(X_test)

    return str(accuracy_score(y_test, result))


df =  pd.read_csv('../filtered_data/01_January_filtered.csv')

target = df.filter(['Fare_Label'], axis=1)
df.drop(['Fare_Label'], axis = 1, inplace = True)

datalist = df.values.tolist()
targetlist = target.values.tolist()

print("kNN accuracy: " + kNN_prediction())
print("Naive Bayes accuracy: " + nb_prediction())
print("Neural Network accuracy: ", nn_prediction())
