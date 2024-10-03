FIND THE STUDENT THAT REPLACES CHALK
BEATS 91%

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if k%sum(chalk)==0:
            return 0
        else:
            while k>sum(chalk):
                k=k%sum(chalk)
            for i in range(len(chalk)):
                if chalk[i]>k:
                    return i
                else:
                    k-=chalk[i]

                
                

                
