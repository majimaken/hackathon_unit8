from modulefinder import Module
import random
from operator import itemgetter 
emptyIndex = 0
offsetLine = 39
pT1 = [emptyIndex,2059,1790,1935,1568, 572,1218,1604, 572,1308, 572,1630,5938, 572,1656,1578, 572,1632,1590,1396,1251,1694,1091, 572,1425,1630,1668]
pT2 = [emptyIndex,572, 572, 572, 572,1583, 572, 572,1497, 572, 572,1525,1635,1473, 572, 572,1313,1213, 572, 572,1482, 572, 572, 572, 572, 572, 572]
pT3 = [emptyIndex,572, 572, 572,1595,1728, 572, 572, 572,1416,1413, 572,1432,1389, 572, 572, 572, 572,1499,1439,1632,1098,1120,1406,1692,1115,1108]
pT4 = [emptyIndex,572, 572, 572, 572, 572,1072,1110, 572, 572,1447, 572, 572, 572,1315, 572, 572,1334, 572,1590, 572, 572, 572, 572, 572, 572, 572]
pT5 = [emptyIndex,572, 572, 572,6587, 572, 572, 572, 572,1432,1191,1358, 572,1375, 572, 572,1475,1756, 572, 572,1249,1609,1120,1275,1110,1730,1477]
pT6 = [emptyIndex,572, 572, 572, 572, 572, 572, 572,1268, 572,1582,1480,1289, 572, 572,1630, 572,1656,1733, 572,1296,1330,1416, 572,1458,1730, 572]
pT7 = [emptyIndex,286, 286, 286, 286,1315, 853,1392, 286,1127, 286,1211, 286, 286,1225, 286, 286,1315, 286,1022, 286, 286,1215, 910, 286,1463, 1163] #655

jobId = list(range(40-offsetLine,65+1-offsetLine))
jobWaitingLounge = [],
triedCombinations =[]

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

Buffer4_1 = 0
Buffer4_2 = 0

Module5 = 0
Module5Timer = 0
Module5Finish = False

Buffer5_1 = 0
Buffer5_2 = 0

Module6 = 0
Module6Timer = 0
Module6Finish = False

quickestId = []
quickestTime = 9999999999


for iteration in range(1,1000000):
    random.shuffle(jobId)
    jobId.remove(62-offsetLine)
    jobId.remove(41-offsetLine)
    jobId.insert(0, 62-offsetLine)
    jobId.insert(25, 41-offsetLine)
    jobWaitingLounge = jobId.copy()
    if jobWaitingLounge in triedCombinations:
        print("Hey, you already tried this!")
        continue
    triedCombinations.append(jobId.copy())
    time = 0
    while True:
        #if time > 10000000:
            #print("timeout reached!")
            #exit()
        time += 1
        if (Module1):
            Module1Timer += 1
        if Module2:
            Module2Timer += 1
        if Module3:
            Module3Timer += 1   
        if Module4:
            Module4Timer += 1        
        if Module5:
            Module5Timer += 1   
        if Module6:
            Module6Timer += 1   
        
        Module1Finish = Module1Timer > pT1[Module1]
        Module2Finish = Module2Timer > pT2[Module2]
        Module3Finish = Module3Timer > pT3[Module3]
        Module4Finish = Module4Timer > pT4[Module4]
        Module5Finish = Module5Timer > pT5[Module5]
        Module6Finish = Module6Timer > pT6[Module6]
 
        if (Module1 == 0) and jobWaitingLounge: #If Module empty and item waiting
            Module1 = jobWaitingLounge.pop(0)
            
        if (Buffer1_1 == 0) and Module1Finish:
            Buffer1_1 = Module1
            Module1 = 0; Module1Timer=0
            
        if (Buffer1_2 == 0) and Buffer1_1:
            Buffer1_2 = Buffer1_1
            Buffer1_1 = 0
            
        if (Module2 == 0) and Buffer1_2:
            Module2 = Buffer1_2
            Buffer1_2 = 0
            
        if (Buffer2_1 == 0) and Module2Finish:
            Buffer2_1 = Module2
            Module2 = 0; Module2Timer = 0
            
        if Buffer2_2 == 0 and Buffer2_1:
            Buffer2_2 = Buffer2_1 
            Buffer2_1 = 0
            
        if (Module3 == 0) and Buffer2_2:
            Module3 = Buffer2_2
            Buffer2_2 = 0
            
        if (Buffer3_1 == 0) and Module3Finish:
            Buffer3_1 = Module3
            Module3 = 0; Module3Timer = 0
            
        if Buffer3_2 == 0 and Buffer3_1:
            Buffer3_2 = Buffer3_1 
            Buffer3_1 = 0
            
        if (Module4 == 0) and Buffer3_2:
            Module4 = Buffer3_2
            Buffer3_2 = 0
            
        if (Buffer4_1 == 0) and Module4Finish:
            Buffer4_1 = Module4
            Module4 = 0; Module4Timer = 0
            
        if Buffer4_2 == 0 and Buffer4_1:
            Buffer4_2 = Buffer4_1 
            Buffer4_1 = 0
            
        if (Module5 == 0) and Buffer4_2:
            Module5 = Buffer4_2
            Buffer4_2 = 0
            
        if (Buffer5_1 == 0) and Module5Finish:
            Buffer5_1 = Module5
            Module5 = 0; Module5Timer = 0
            
        if Buffer5_2 == 0 and Buffer5_1:
            Buffer5_2 = Buffer5_1 
            Buffer5_1 = 0
            
        if (Module6 == 0) and Buffer5_2:
            Module6 = Buffer5_2
            Buffer5_2 = 0
            
        if (Module6Finish):
            Module6 = 0; Module6Timer = 0
   
        if (jobWaitingLounge==[]) and (Module1+Buffer1_1+Buffer1_2+Module2+Buffer2_1+Buffer2_2+Module3+Buffer3_1+Buffer3_2+Module4+Buffer4_1+Buffer4_2+Module5+Buffer5_1+Buffer5_2+Module6==0):
            if time < quickestTime:
                quickestTime = time
                quickestId = jobId.copy()
                quickestId = [x+offsetLine for x in quickestId]
                print(quickestId)
                print(itemgetter(*jobId.copy())(pT1)); 
                print(itemgetter(*jobId.copy())(pT2)); 
                print(itemgetter(*jobId.copy())(pT3)); 
                print(itemgetter(*jobId.copy())(pT4)); 
                print(itemgetter(*jobId.copy())(pT5)); 
                print(itemgetter(*jobId.copy())(pT6)); 
                print(itemgetter(*jobId.copy())(pT7)); 
                print(quickestTime); print("Iteration:"); print(iteration)
            break          

print("final result:")        
print(quickestId)
print(quickestTime)
            