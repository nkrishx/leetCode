class Solution:
    def numberToWords(self, num: int) -> str:
        self.below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",  "Eighty", "Ninety"]
        
        self.thousand = ["", "Thousand", "Million", "Billion"]
        if num == 0:
            return "Zero"
        
        result = ""
        i = 0
        while num  > 0:
            if num%1000 != 0:
                result = self.helper(num%1000) + " " + self.thousand[i] + " " + result
            num = num // 1000
            i += 1
        return result.rstrip()  
    
    def helper(self, num):
        if num<20:
            return (self.below_20[num]).rstrip()       
        elif num <100:
            return (self.tens[num//10] + " " + self.helper(num%10)).rstrip()
        elif num < 1000:
            return (self.below_20[num//100] + " " + "Hundred" + " "  + self.helper(num%100)).rstrip()
        