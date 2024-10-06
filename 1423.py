MAXIMUM POINTS FROM CARDS
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftsum=0
        rightsum=0
        maxsum=0
        for i in range(k):
            leftsum+=cardPoints[i]
        maxsum=leftsum
        rightindex=len(cardPoints)-1
        for j in range(k-1,-1,-1):
            leftsum-=cardPoints[j]
            rightsum+=cardPoints[rightindex]
            rightindex-=1
            maxsum=max(maxsum,leftsum+rightsum)
        return maxsum

