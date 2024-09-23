Longest subarray of 1's after deleting one element
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cur=0
        prev=0
        ans=0
        for i in nums:
            if i==1:
                cur+=1
            elif i==0:
                ans=max(ans,prev+cur)
                prev=cur
                cur=0              
        ans=max(ans,prev+cur)
        if ans==len(nums):
            return ans-1
        else:
            return ans
