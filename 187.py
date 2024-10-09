Repeated DNA SEQUENCE BEATS 92% 
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        ans=set()
        for length in range(len(s)-10+1):
            substr=s[length:length+10]
            if substr in seen:
                ans.add(substr)
            seen.add(substr)
        return list(ans)
