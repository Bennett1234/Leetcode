class Solution:
    def romanToInt(self, s: str) -> int:
        sum_ = 0
        d = {'I':1
        ,'X':10
        ,'C':100
        ,'V':5
        ,'L':50
        ,'M':1000
        ,'D':500}
        prev = None
        for i in range(len(s)-1,-1,-1):
            if (prev in ['V','X'] and s[i] == 'I')\
            or(prev in ['L','C'] and s[i] == 'X')\
            or(prev in ['D','M'] and s[i] == 'C'):
                sum_ = sum_-d[s[i]]
            else:
                sum_ = sum_+d[s[i]]
            prev = s[i]

        return sum_
