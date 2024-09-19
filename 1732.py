Find highest altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[]
        a.append(0)
        for i in range(len(gain)):
            a.append(gain[i]+a[i])
        return max(a)
