#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
def TwoSum (l, target):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i] + l[j] == target:
                return (i,j)
    return [-1,-1]


#O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            l = target-nums[i]
            if (l in d):
                return [i,d[l]]
            d[nums[i]] = i
