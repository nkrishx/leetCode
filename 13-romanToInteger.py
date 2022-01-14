class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        for key, value in hashMap.items():
            s = s.replace(key, f'+{value}')
        
        print(s)
        split_str=s.split('+')
        print(split_str)
        split_str=[int(each) for each in split_str if each != '']
        print(split_str)
        return sum(split_str)
        