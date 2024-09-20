Longest consecutive sequence 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        nums=set(nums)
        for num in nums:
            if num-1 not in nums:
                c=1
                while num+c in nums:
                    c+=1
                ans=max(ans,c)
        return ans
