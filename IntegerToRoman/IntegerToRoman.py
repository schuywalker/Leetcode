from math import floor
from operator import mod


class Solution:
    def intToRoman(self, num: int) -> str:
        
        modNum = num
        ret = ""
        behind = False
        sequence = [1,5,10,50,100,500,1000]
        seq = [1000,500,100,50,10,5,1]
        
        def convert (val: int) -> str:
            if val == 1:
                return 'I'
            elif val == 5:
                return 'V'
            elif val == 10:
                return 'X'
            elif val == 50:
                return 'L'
            elif val == 100:
                return 'C'
            elif val == 500:
                return 'D'
            elif val == 1000:
                return 'M'
            
        def numeralsShouldBeSwitched(modNum:int, seqPosition:int) -> bool:
            if ((modNum != seq[seqPosition]) and (modNum+seq[seqPosition+1] >= seq[seqPosition])):
                return True
            else: return False
        
        
        def digitsAreSameLength(i:int, *seq) -> bool:
           
            # print(seq)
            seq = seq[0]
            # print (seq)

            if (i >= len(seq)-2):
                print("digitsAreSameLength if ")
                return False
            
            elif (len(str(seq[i])) == len(str(seq[i+1]))):
                print ("digitsAreSameLength elif: "+str(len(str(seq[i]))) +" "+ str(len(str(seq[i+1]))))
                return True
            else:
                print ("digitsAreSameLength else: "+str(len(str(seq[i]))) +" "+ str(len(str(seq[i+1]))))
                return False
             
        def findNextPrecursor(i:int, seq) -> int:
            ret = 0
            print(seq[i])
            if seq[i] == 1:
                return 0
            else :
                for x in range(i,len(seq)-1):
                    ret = ret + 1
                    if seq[x] % 10 == 0 or seq[x] == 1:
                        return ret
            return 0
        
        i = 0
        for i in range(len(seq)):
            
            quotient = floor(modNum / seq[i]) 
            
            numeral = convert(seq[i])

            if modNum < seq[i] and not numeralsShouldBeSwitched(modNum, i):
                print('on:', seq[i],'do nothing. modNum', modNum)
            if i == 0:
                ret += numeral*int(quotient)
                modNum %= 1000
            elif modNum >= 50 and modNum < 90:
                ret += 'L'
                modNum %= 50
            elif modNum >= 500 and modNum < 900:
                ret += 'D'
                modNum %= 500
            # elif i == len(seq)-1:
            #     print("on 1s")
            else: 
                if (i < len(seq) and numeralsShouldBeSwitched(modNum, i)):
                    
                    amount = findNextPrecursor(i, seq)
                    
                    ret += convert(seq[i+amount])+convert(seq[i])
                    print("FOR if. modNum:",modNum," on: ",seq[i],)
                    modNum %= seq[i+1]
                    print(quotient)
                    # i = i+1
                    print("After ++i and modNum mod. on:",modNum," seqNumber: ",seq[i])
                else:
                    ret += numeral*int(quotient)
                    print("FOR else. modNum:", modNum, " on: ", seq[i])
                    modNum %= seq[i]
                    print("After ++i and modNum mod modNum:", modNum, " seqNumber: ", seq[i])
            
            print(ret)
            
            # if digitsAreSameLength(i, seq) and modNum >= seq[i] - seq[i+1]:
            #     # i.e. modNum = 999. only 500 is subtracted instead of 900
            #     print("FOR if. modNum:" + str(modNum) + " seqNumber: " + str(seq[i]))
            #     i = i+1
            #     modNum %= seq[i]
            #     print("After ++i and modNum mod. modNum:" + str(modNum) + " seqNumber: " + str(seq[i]))
            #     print()
                
            # else:
            #     modNum %= seq[i]
            #     print("FOR else. modNum: "+ str(modNum) + " seqNumber: " + str(seq[i]))
            #     print()
            # if (modNum == 0):
            #     return ret

        return(ret)
        
        