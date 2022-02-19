from modulefinder import Module
import random

pT1 = [0,10,1]
pT2 = [0,1,10]
pT3 = [0,5,5]

jobId = [1, 2]
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
    print(jobId)
    time = 0
    while True:
        if time > 1000:
            print("timeout reached!")
            exit()
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
            print(time)
            break          

print("final result:")        
print(quickestId)
print(quickestTime)
            