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

import requests
import pandas as pd
import json
from pandas import json_normalize

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot



submission_side_challenge = {"challenge_id": 3}  # the challenge id indicated in the documentation
response = requests.get('https://hackathon.unit8.com/api/get_resource',
                        headers={'Authorization': f'Token {TOKEN_ID}', 'Content-Type': 'application/json'},
                        json=submission_side_challenge
                        )
print(response.json())

dic = response.json()
info = json.loads(dic)

dat_3 = pd.read_json(dic, orient = "columns")


print(dat_3.head(10))

y = dat_3['productivity']
X = dat_3.loc[:, dat_3.columns != 'productivity']

# X, y = make_regression(n_samples=1000, n_features=69, n_informative=5, random_state=1)
# define the model
model = LinearRegression()
# fit the model
model.fit(X, y)
# get importance
importance = model.coef_
# summarize feature importance
for i, v in enumerate(importance):
    print('Feature: %0d, Score: %.5f' % (i, v))
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.show()



# Challenge 4
#########################################

import seaborn as sns
import matplotlib.pyplot as plt

response_4 = requests.get('https://hackathon.unit8.com/api/get_resource',
                        headers={'Authorization': 'Token fed877446aa8e41f956b19f86383d493a7a001a1'},
                        json={'challenge_id': 4}
                        )

print(response_4.json())   

dic_4 = response_4.json()
dat_4 = pd.read_json(dic_4, orient = "columns")

plt.

sns.displot(dat_4["professional_mistakes"], kde = True)
sns.plot()



