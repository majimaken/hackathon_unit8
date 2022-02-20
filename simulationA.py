from modulefinder import Module
import random
emptyIndex = 0
pT1 = [emptyIndex,4887,2755,2348,3268,3787,3032,2551,3341,3556,2869,1224,1878,2266,2950,4787,3380,1224,3582,2666,2916,3157]
pT2 = [emptyIndex,4203,3273,4187,1224,3972,3700,4554,3352,4133,1224,4887,4280,2955,4139,4150,4315,3837,3400,3979,3747,3325]
pT3 = [emptyIndex,2551,2341,2804,2959,2159 ,612,2286,2540,1793,4091,2678,2538,2080,3209,2547,2361,2367,2895 ,612,2520,2397]

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

for iteration in range(1,100000):
    random.shuffle(jobId)
    jobWaitingLounge = jobId.copy()
    if jobWaitingLounge in triedCombinations:
        break
    triedCombinations.append(jobId.copy())
    time = 0
    while True:
        time += 1
        if Module1:
            Module1Timer += 1
        if Module2:
            Module2Timer += 1
        if Module3:
            Module3Timer += 1        
        
        Module1Finish = Module1Timer > pT1[Module1] #
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
            