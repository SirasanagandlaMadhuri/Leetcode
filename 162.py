Question: Find peak element(A peak element is an element that is strictly greater than its neighbors.)
Solution:
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums or len(nums)==1:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        if len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        return 0
