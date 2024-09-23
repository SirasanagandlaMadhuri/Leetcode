Candies Distribution
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        if not candyType:
            return 0
        eat=len(candyType)//2
        candy=len(set(candyType)) 
        return min(eat,candy)
