from modulefinder import Module
from operator import itemgetter
import random
offsetLine = 65
emptyIndex = 0
pT1 = [emptyIndex, 1174, 1384, 1162, 1929, 929, 1420, 1022, 1370]
pT2 = [emptyIndex, 1325, 888, 1136, 1160, 1239, 1124, 1341, 1236]
pT3 = [emptyIndex, 1885, 2023, 1277, 1606, 1985, 1472, 6415, 1394]
pT4 = [emptyIndex, 977, 1146, 1024, 1156, 1604, 1337, 1826, 1133]

jobId = list(range(66-offsetLine, 73+1-offsetLine))
jobWaitingLounge = []
triedCombinations = []

Module1 = 0
Module1Timer = 0
Module1Finish = False

Buffer1_1 = 0
Buffer1_2 = 0

Module2 = 0
Module2Timer = 0
Module2Finish = False

Buffer2_1 = 0
Buffer2_2 = 0

Module3 = 0
Module3Timer = 0
Module3Finish = False

Buffer3_1 = 0
Buffer3_2 = 0

Module4 = 0
Module4Timer = 0
Module4Finish = False

quickestId = []
quickestTime = 9999999999


for iteration in range(1, 100000):
    random.shuffle(jobId)
    # jobId.remove(70-offsetLine)
    # jobId.remove(68-offsetLine)
    # jobId.remove(66-offsetLine)
    # jobId.insert(0,70-offsetLine)
    # jobId.insert(1,68-offsetLine)
    # jobId.insert(8,66-offsetLine)
    jobWaitingLounge = jobId.copy()
    if jobWaitingLounge in triedCombinations:
        continue
    triedCombinations.append(jobId.copy())
    time = 0
    while True:
        # if time > 10000000:
        #print("timeout reached!")
        # exit()
        time += 1
        if (Module1):
            Module1Timer += 1
        if Module2:
            Module2Timer += 1
        if Module3:
            Module3Timer += 1
        if Module4:
            Module4Timer += 1

        Module1Finish = Module1Timer > pT1[Module1]
        Module2Finish = Module2Timer > pT2[Module2]
        Module3Finish = Module3Timer > pT3[Module3]
        Module4Finish = Module4Timer > pT4[Module4]

        if (Module1 == 0) and jobWaitingLounge:  # If Module empty and item waiting
            Module1 = jobWaitingLounge.pop(0)

        if (Buffer1_1 == 0) and Module1Finish:
            Buffer1_1 = Module1
            Module1 = 0
            Module1Timer = 0

        if (Buffer1_2 == 0) and Buffer1_1:
            Buffer1_2 = Buffer1_1
            Buffer1_1 = 0

        if (Module2 == 0) and Buffer1_2:
            Module2 = Buffer1_2
            Buffer1_2 = 0

        if (Buffer2_1 == 0) and Module2Finish:
            Buffer2_1 = Module2
            Module2 = 0
            Module2Timer = 0

        if Buffer2_2 == 0 and Buffer2_1:
            Buffer2_2 = Buffer2_1
            Buffer2_1 = 0

        if (Module3 == 0) and Buffer2_2:
            Module3 = Buffer2_2
            Buffer2_2 = 0

        if (Buffer3_1 == 0) and Module3Finish:
            Buffer3_1 = Module3
            Module3 = 0
            Module3Timer = 0

        if Buffer3_2 == 0 and Buffer3_1:
            Buffer3_2 = Buffer3_1
            Buffer3_1 = 0

        if (Module4 == 0) and Buffer3_2:
            Module4 = Buffer3_2
            Buffer3_2 = 0

        if (Module4Finish):
            Module4 = 0
            Module4Timer = 0

        if (jobWaitingLounge == []) and (Module1+Buffer1_1+Buffer1_2+Module2+Buffer2_1+Buffer2_2+Module3+Buffer3_1+Buffer3_2+Module4 == 0):
            if time <= quickestTime:
                quickestTime = time
                quickestId = jobId.copy()
                quickestId = [x+offsetLine for x in quickestId]
                print(quickestId)
                print(itemgetter(*jobId.copy())(pT1))
                print(itemgetter(*jobId.copy())(pT2))
                print(itemgetter(*jobId.copy())(pT3))
                print(itemgetter(*jobId.copy())(pT4))
                print(quickestTime)
                print("Iteration:")
                print(iteration)
            break

print("final result:")
print(quickestId)
print(quickestTime)
