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

import pandas as pd
import numpy as np

np.random.seed(8)

one = np.arange(1,22)
two = np.arange(22, 40)
three = np.arange(40,66)
four = np.arange(66,74)

one_rand = np.random.choice(one, size = 21, replace = False)
two_rand = np.random.choice(two, size = len(two), replace = False)
three_rand = np.random.choice(three, size = len(three), replace = False)
four_rand = np.random.choice(four, size = len(four), replace = False)

print(one_rand)
print(two_rand)
print(three_rand)
print(four_rand)



job_order = {"A": one_rand,
             "B": two_rand,
             "C": three_rand,
             "D": four_rand}

print(job_order)


# Create data set
##############################

