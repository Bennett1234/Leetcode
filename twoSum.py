#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(numbers,target):
    for i,a in enumerate(numbers):
        for j, b in enumerate(numbers[i+1:]):
            if a + b == target:
                return [i,j+i+1]
    return [-1,-1]
