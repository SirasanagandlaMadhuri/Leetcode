Question: Maximum average subarray

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg=-inf
        cur=0
        for i in range(k):
            cur+=nums[i]
        avg=cur/k
        for i in range(k,len(nums)):
            cur+=nums[i]
            cur-=nums[i-k]
            avg=max(avg,cur/k)
        return avg
