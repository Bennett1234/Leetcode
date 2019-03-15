def maxSubArray(nums):
    maximum = running_sum = nums[0]
    if len(nums) == 1:
        return(nums[0])
    for n in nums[1:]:
        running_sum = max(running_sum+n,n)
        maximum = max(running_sum, maximum)
    return maximum
#Maintain a running_total of the array seen so far.
#If the current value is greater than the current running total, set the running total to the current value.
#Track the maximum total seen so far and return it.
