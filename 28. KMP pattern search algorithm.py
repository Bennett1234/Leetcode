#brute force
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return -1
        lps = [0]*len(needle)
        prevLPS,i = 0,1
        while i < len(needle):
            if needle[i]==needle[prevLPS]:
                lps[i]=prevLPS+1
                prevLPS += 1
                i=i+1
            elif prevLPS == 0:
                lps[i]=0
                i=i+1
            else:
                prevLPS = lps[prevLPS-1]
        i=0
        j=0
        while i < len(haystack):
            if haystack[i]==needle[j]:
                i,j = i+1,j+1
            else:
                if j == 0:
                    i = i+1
                else:
                    j = lps[j-1]
            if j == len(needle):
                return i - len(needle)
        return -1
                    
                

