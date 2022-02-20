# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 16:58:53 2022

@author: kenge
"""

# packages
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# # Data exploration
# df = pd.read_csv("Task/production_line_optimization_first_log.csv")
# print(df)


#############################

# import pandas as pd
# import numpy as np

# np.random.seed(8)

# one = np.arange(1, 22)
# two = np.arange(22, 40)
# three = np.arange(40, 66)
# four = np.arange(66, 74)

# one_rand = np.random.choice(one, size=21, replace=False)
# two_rand = np.random.choice(two, size=len(two), replace=False)
# three_rand = np.random.choice(three, size=len(three), replace=False)
# four_rand = np.random.choice(four, size=len(four), replace=False)

# print(one_rand)
# print(two_rand)
# print(three_rand)
# print(four_rand)


# job_order = {"A": one_rand,
#              "B": two_rand,
#              "C": three_rand,
#              "D": four_rand}

# print(job_order)







# Challenge 3 Productivity Factor
#########################################

# import requests
# import pandas as pd
# import json
# from pandas import json_normalize
# import seaborn as sns

# from sklearn.datasets import make_regression
# from sklearn.linear_model import LinearRegression
# from matplotlib import pyplot



# submission_side_challenge = {"challenge_id": 3}  # the challenge id indicated in the documentation
# response = requests.get('https://hackathon.unit8.com/api/get_resource',
#                         headers={'Authorization': f'Token {TOKEN_ID}', 'Content-Type': 'application/json'},
#                         json=submission_side_challenge
#                         )
# print(response.json())

# dic = response.json()
# info = json.loads(dic)

# dat_3 = pd.read_json(dic, orient = "columns")


# print(dat_3.head(10))


# plt.figure(figsize=(12,10))
# cor = dat_3.corr()
# cor_2 = cor["productivity"]


# sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
# plt.show()





# y = dat_3['productivity']
# X = dat_3.loc[:, dat_3.columns != 'productivity']

# # X, y = make_regression(n_samples=1000, n_features=69, n_informative=5, random_state=1)
# # define the model
# model = LinearRegression()
# # fit the model
# model.fit(X, y)
# # get importance
# importance = model.coef_
# # summarize feature importance
# for i, v in enumerate(importance):
#     print('Feature: %0d, Score: %.5f' % (i, v))
# # plot feature importance
# pyplot.bar([x for x in range(len(importance))], importance)
# pyplot.show()




# # Challenge 4
# #########################################

# import seaborn as sns
# import matplotlib.pyplot as plt

# response_4 = requests.get('https://hackathon.unit8.com/api/get_resource',
#                         headers={'Authorization': 'Token fed877446aa8e41f956b19f86383d493a7a001a1'},
#                         json={'challenge_id': 4}
#                         )

# print(response_4.json())   

# dic_4 = response_4.json()
# dat_4 = pd.read_json(dic_4, orient = "columns")

# sns.jointplot(x = "professional_mistakes", y = "sales_made", data = dat_4)

# # Select the one on the top left side










# Challenge 5
###########################################

# import requests
# import seaborn as sns
# from scipy import stats
# import numpy as np
# import pandas as pd

# response_5 = requests.get('https://hackathon.unit8.com/api/get_resource',
#              headers={'Authorization': 'Token fed877446aa8e41f956b19f86383d493a7a001a1'},
#              json={'challenge_id': 5}
# )

# dic_5 = response_5.json()
# dat_5 = pd.read_json(dic_5, orient = "columns")

# dat_5_sorted = [372,310,325,642,436,237,363,983,339,283,823,365,195,219,352,28,616,710,391,375,596,249,260,456,693,100,797,256,511,113]
# dat_5_sorted.sort()
# print(dat_5_sorted)

# sns.pairplot(dat_5) 

# z = np.abs(stats.zscore(dat_5))
# print(np.where(z > 3))


# dat_5.nlargest(10, "temperature_on_line C")

# sns.histplot(dat_5["temperature_on_line C"])
# sns.histplot(dat_5["time_spent_on_line s"])







# Challenge 2
###################################################

import requests
import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd
import json
from pathlib import Path
import os

response_2 = requests.get('https://hackathon.unit8.com/api/get_resource',
                          headers={'Authorization': 'Token fed877446aa8e41f956b19f86383d493a7a001a1'},
                          json={'challenge_id': 2}
                          )

dic_2 = response_2.json()
dic_2 = json.loads(dic_2)

dic_2_train = dic_2["train"]
dic_2_test = dic_2["test"]

dat_2_train = pd.DataFrame.from_dict(dic_2_train, orient='index')
dat_2_test = pd.DataFrame.from_dict(dic_2_test, orient='index')

# Save dataframes as .csv for R
# dat_2_train.to_csv("Ken\data2_train.csv", index = True)
# dat_2_test.to_csv("Ken\data2_test.csv", index = True)

# Split into predictor and features
y_train = dat_2_train.loc["label"]
x_train = dat_2_train.loc["1":"18"].T

x_test = dat_2_test.loc["1":"18"].T

# Set row 1 and 18 to factors
y_train = y_train.astype("category")
x_train["1"] = x_train["1"].astype("category")
x_train["18"] = x_train["18"].astype("category")
x_test["1"] = x_test["1"].astype("category")
x_test["18"] = x_test["18"].astype("category")




# Logistic regression
###########################################################

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

model = LogisticRegression(solver='newton-cg', random_state=0)
model.fit(x_train, y_train)
pred = model.predict(x_test).tolist()

# Getting indices
ind = x_test.index.tolist()

# Dictionary
res = dict(zip(ind, pred))

res_int = {int(key):res[key] for key in res}




# Random forest
###########################################################

# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import make_classification

# X, y = make_classification(n_samples=1000, n_features=4,
#                             n_informative=2, n_redundant=0,
#                             random_state=0, shuffle=False)

# clf = RandomForestClassifier(max_depth=2, random_state=0)
# clf.fit(x_train, y_train)

# from sklearn.ensemble import RandomForestClassifier

# #Create a Gaussian Classifier
# clf=RandomForestClassifier(n_estimators=10000, random_state = 42)

# #Train the model using the training sets y_pred=clf.predict(X_test)
# clf.fit(x_train, y_train)

# y_pred=clf.predict(x_test)

# # Dictionary
# ind = x_test.index.tolist()
# res = dict(zip(ind, y_pred))
# res_int = {int(key):res[key] for key in res}
