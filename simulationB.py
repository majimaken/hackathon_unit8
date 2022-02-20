from modulefinder import Module
import random
from operator import itemgetter 
emptyIndex = 0
offsetLine = 21
pT1 = [emptyIndex,1674,1897,1974,1623,1937,2417,1777,2255,1841 ,796,2090,2020,1558,2321,2202,2329,3533,3434]
pT2 = [emptyIndex,3716,2584,2619,3016,3520,3136,3202,3108,2966,2172,4014,2439, 796,2917,3224,2847,4815, 796]
pT3 = [emptyIndex,2818 ,796,2540, 796,2698, 796,2064,2068,2362,1920,2051,1992,2575,2389,2533, 796,3690,4243]
pT4 = [emptyIndex,2562,2665,3494,5391,2420,2790,3090,3246,3226,2588,2351,2957,2330,3156,2341,3226,4078,4859]
pT5 = [emptyIndex,2862,3174,3472,2632,2415,3068,2880, 796,2391,3145, 796,2867,2790,2579,2593,3448,4417,4098]
pT6 = [emptyIndex,2195,2035,1561,1927,1522,1704,2133,2030,2146,1493, 398,1475,1960,1857,1453, 398,2762,2879] #1613

jobId = list(range(22-offsetLine,39+1-offsetLine))
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


for iteration in range(1,100000):
    random.shuffle(jobId)
    jobId.remove(31-offsetLine)
    jobId.remove(32-offsetLine) #or 44
    jobId.insert(0,31-offsetLine)
    jobId.insert(39,32-offsetLine) 

    jobWaitingLounge = jobId.copy()
    if jobWaitingLounge in triedCombinations:
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
                print(quickestId); 
                print(itemgetter(*jobId.copy())(pT1)); 
                print(itemgetter(*jobId.copy())(pT2)); 
                print(itemgetter(*jobId.copy())(pT3)); 
                print(itemgetter(*jobId.copy())(pT4)); 
                print(itemgetter(*jobId.copy())(pT5)); 
                print(itemgetter(*jobId.copy())(pT6)); 
                print(quickestTime); print("Iteration:"); print(iteration)
            break          

print("final result:")        
print(quickestId)
print(quickestTime)
            