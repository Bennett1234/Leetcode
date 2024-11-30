class Solution:
    def isValid(self, s: str) -> bool:
        bucket = []
        map_ = {'(':')',
        '[':']',
        '{':'}'}
        for i in s:
            if i in ['(','[','{']:
                bucket.append(i)
            elif len(bucket) > 0:
                last = bucket.pop()
                if map_[last] != i:
                    return False
            else:
                return False
        if len(bucket) >0:
            return False
        else:
            return True
