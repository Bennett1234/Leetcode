def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        else:
            for i in range(0,len(nums)-1):
                if nums[i] < target and nums[i+1] > target:
                    return i+1
