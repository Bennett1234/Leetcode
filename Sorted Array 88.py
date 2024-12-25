#brute force
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:]
        loc = 0
        while nums2:
            element = nums2.pop(0)
            for i in range(loc,m+1):
                if nums1[i] > element:
                    nums1[i+1:m+1] = nums1[i:m]
                    nums1[i] = element
                    m = m + 1
                    loc = i
                    break

#using pointers
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m+n-1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
                
            

        
