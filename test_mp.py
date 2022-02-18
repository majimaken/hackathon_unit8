# conda activate test
# cd Desktop/Hackathon
# python3 test.py

# packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import nltk
# import sklearn as sk

<<<<<<< Updated upstream
# from collections import Counter
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split

# print("Hello World")

# test
df = pd.read_csv("Task/production_line_optimization_first_log.csv")
print(df)
# df['SQRT Balance'] = np.sqrt((df['Balance']))
# df.plot(x="Balance", y=["Deposits", "Withdrawls"])
# plt.show()
# plt.savefig("figs/test.png")
=======
df = pd.read_csv("Task/Book1.csv")
df.time = pd.to_datetime(df.time)

# print(df)
# df.time = pd.to_datetime(df.time)
# start = min(df.time)
# end = max(df.time)
# dif = end - start

# Line_A = pd.DataFrame(columns=['job_id', 'module', 'dif'])

for i in range(1, 5):
    Job_Id = df[df.job_id == i]
    # print("Job ID: ", i)
    for j in range(1, 4):
        Module = Job_Id[Job_Id.module == j]
        # print("Module: ", j)
        if "storing_job" in Module.state.values:
            dif = Module[Module.state == 'storing_job']['time'] - \
                Module[Module.state == 'fetching_job']['time']
        else:
            dif = df.at[j, 'time'] - df.at[j, 'time']
        print(dif)

#     print("yes")
# else:
#     print("no")
#     dif = Module[Module.state == "storing_job"].time - \
#         Module[Module.state == "fetching_job"].time
#     print(dif)
# #     else:
#         dif = Module[Module.state == "processing"] - Module[Module.state == "fetching_job"]

#     # Choose entries with id p01
# df_new = df[df['Pid'] == 'p01']
>>>>>>> Stashed changes
