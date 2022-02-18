# conda activate test
# cd Desktop/Hackathon
# python3 test.py

# packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import nltk
# import sklearn as sk

df = pd.read_csv("Task/production_line_optimization_first_log.csv")
# print(df)
df.time = pd.to_datetime(df.time)

start = min(df.time)
end = max(df.time)
dif = end - start
