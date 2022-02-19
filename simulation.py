from modulefinder import Module
import random
emptyIndex = 0
pT1 = [emptyIndex,4275,2143,1736,2656,3175,2420,1939,2729,2944,2257,1569,3521,1654,3233,4175,2768,2596,3538,3703,3225,2788]
pT2 = [emptyIndex,3591,2661,3575, 612,3360,3088,3942,2740,3521, 612,4275,3668,2343,3527,3538,3703,3225,2788,3367,3135,2713]
pT3 = [emptyIndex,2551,2341,2804,3571,3743,5166,2286,2540,1793,4929,4892,3567,2080,3209,4927,3837,3400,4591,4359,6299,3644]

jobId = list(range(1,21+1))
jobWaitingLounge = []
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

quickestId = []
quickestTime = 9999999999

for iteration in range(1,10):
    random.shuffle(jobId)
    jobWaitingLounge = jobId.copy()
    if jobWaitingLounge in triedCombinations:
        break
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
        
        Module1Finish = Module1Timer > pT1[Module1]
        Module2Finish = Module2Timer > pT2[Module2]
        Module3Finish = Module3Timer > pT3[Module3]
 
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
            
        if (Module3Finish):
            Module3 = 0; Module3Timer = 0
               
        if (jobWaitingLounge==[]) and (Module1+Buffer1_1+Buffer1_2+Module2+Buffer2_1+Buffer2_2+Module3==0):
            if time < quickestTime:
                quickestTime = time
                quickestId = jobId.copy()
                print(quickestId); print(quickestTime)
            break          

print("final result:")        
print(quickestId)
print(quickestTime)
            