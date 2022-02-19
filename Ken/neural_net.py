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





import tensorflow as tf
from sklearn.model_selection import train_test_split

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train, x_test, y_train, y_test = train_test_split(xdata)






import os
import pandas as pd

df = pd.read_excel("")



