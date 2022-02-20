# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 10:35:20 2022

@author: kenge
"""

# import os
# import pandas as pd
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.wrappers.scikit_learn import KerasRegressor
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import KFold
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline

# # load dataset
# dataframe = pd.read_csv("boston.csv", sep=",")
# dataset = dataframe.values

# # splitting to features and predictor
# X = dataset[:,0:13]
# Y = dataset[:,13]

# # Define base model
# def baseline_model():
#     # create model
#     model = Sequential()
#     model.add(Dense(13, input_dim = 13, kernel_initializer="normal", activation="relu"))
#     model.add(Dense(1, kernel_initializer="normal"))
#     # compile model
#     model.compile(loss = "mean_squared_error", optimizer = "adam")
#     return model
    

# estimator = KerasRegressor(build_fn = baseline_model, epochs = 5, batch_size = 5, verbose = 0)
# kfold = KFold(n_splits = 10)
# results = cross_val_score(estimator, X, Y, cv=kfold)
# print("Baseline: %.2f (%.2f) MSE" % (results.mean(), results.std()))




# Packages
import os 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# Data prep
sub = pd.read_excel("submissions.xlsx")
# Line A
X = sub["A"]
Y = sub["Score A"]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state=1)

x_train = x_train.to_list()
x_test = x_test.to_list()
y_train = y_train.to_list()
y_test = y_test.to_list()

mlp = MLPClassifier(hidden_layer_sizes=(8,8,8), activation='relu', solver='adam', max_iter=500)
mlp.fit(x_train, y_train)

# predict_train = mlp.predict(x_train)
# predict_test = mlp.predict(x_test)

# a1 = [ 5, 21, 17, 16, 11,  7,  4,  9,  2, 12, 20, 18, 15,  6,  1, 13, 19, 14, 10,  3,  8]
# a2 = [15 ,13 ,12  ,2  ,4  ,1 ,19  ,6  ,3 ,20  ,9 ,11 ,10 ,17  ,5 ,14 ,21 ,18  ,7 ,16  ,8]
# a3 = [15,  9,  2, 17, 14,  3, 16, 10, 11,  5,  7, 20, 18,  4, 13, 19,  8, 1,  6, 12, 21]

# X = pd.DataFrame(list(zip(a1, a2, a3)), index = [])



