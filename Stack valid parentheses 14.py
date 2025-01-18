class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')',
              '[':']',
              '{':'}'}
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(d[i])
            elif i in [')',']','}'] and len(stack) >0:
                if i == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
