class Solution:
    def intToRoman(self, num: int) -> str:
        
        localNum = num
        ret = ""
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']      
        
        for i in range(len(val)):
            
            while (val[i] <= localNum):
                ret += numerals[i]
                localNum -= val[i]

        return(ret)