class Solution:
    def intToRoman(self, num: int) -> str:
        
        modNum = num
        ret = ""
        behind = False
        sequence = [1,5,10,50,100,500,1000]
        seq = [1000,500,100,50,5,1]
        
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
            if (modNum+seq[seqPosition+1] >= seq[seqPosition]):
                return True
            else: return False
        
#         def thisLessThanNextFromSeqNumber():
#             # if  modNum >= seq[i] - seq[i+1]
            
        
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
        
        def roman (quotient: int, seqNumber: int, seqPosition: int, modNum: int, *args) -> str:
            
            if (modNum - seqNumber) < 0:
                return ''   
            
            ret = ''
            numeral = convert(seqNumber)
            
            if seqPosition == len(seq)-1:
                print("on 1s")
            elif seqPosition > 0: 
                if (numeralsShouldBeSwitched(modNum, seqPosition)):
                    return convert(seq[seqPosition+1])+convert(seq[seqPosition-1])
            else: # executes on 1000s only
                return numeral*int(quotient)
            
        
        
        i = 0
        for i in range(len(seq)-1):
            
            quotient = floor(modNum / seq[i])
            
            ret += str(roman(quotient, seq[i], i, modNum, seq))
            
            if digitsAreSameLength(i, seq) and modNum >= seq[i] - seq[i+1]:
                # i.e. modNum = 999. only 500 is subtracted instead of 900
                print("FOR if. modNum:" + str(modNum) + " seqNumber: " + str(seq[i]))
                i = i+1
                modNum %= seq[i]
                print("After ++i and modNum mod. modNum:" + str(modNum) + " seqNumber: " + str(seq[i]))
                print()
                
            else:
                modNum %= seq[i]
                print("FOR else. modNum: "+ str(modNum) + " seqNumber: " + str(seq[i]))
                print()
            if (modNum == 0):
                return ret
                
# #         handle 1000 separately
#         if ones == 1:
#             ret += "I"
#         elif ones == 2:
#             ret += "II"
#         elif ones == 3:
#             ret = ret + "III"
#         elif ones == 0:
#             ret += ""
#         elif ones == 4:
#             behind = True

        return(ret)
        
        # Ms = num / 1000
        # ret += Ms
        
        