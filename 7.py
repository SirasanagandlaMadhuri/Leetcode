Reverse Integer:
class Solution:
    def reverse(self, x: int) -> int:
        k=x
        if k<0:
            k=abs(x) 
        ans=str(k)
        ans=int(ans[::-1])
        if ans not in range(-2**31,2**31):
            return 0
        elif x<0:
            return ans*-1
        else:
            return ans
