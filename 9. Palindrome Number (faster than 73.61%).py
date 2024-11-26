def isPalindrome(x):
    return str(x)==str(x)[::-1]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x %10 == 0:
            return False
        reverse = 0
        orig = x
        while x > 0:
            last = x % 10
            reverse = reverse*10+last
            x = x // 10
        return orig == reverse
        
