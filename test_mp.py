# conda activate test
# cd Desktop/Hackathon
# python3 test.py

# packages
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
# import nltk
# import sklearn as sk

# from collections import Counter
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split

# print("Hello World")
#
# # test
# df = pd.read_csv("Task/production_line_optimization_first_log.csv")
# print(df)
# # df['SQRT Balance'] = np.sqrt((df['Balance']))
# # df.plot(x="Balance", y=["Deposits", "Withdrawls"])
# # plt.show()
# # plt.savefig("figs/test.png")
#
# df = pd.read_csv("Task/Book1.csv")
# df.time = pd.to_datetime(df.time)
#
# # print(df)
# # df.time = pd.to_datetime(df.time)
# # start = min(df.time)
# # end = max(df.time)
# # dif = end - start

response = requests.get(
    'https://hackathon.unit8.com/api/get_resource',
    headers={'Authorization': 'Token fed877446aa8e41f956b19f86383d493a7a001a1'},
    json={'challenge_id': 5}
)

print(response.json)
