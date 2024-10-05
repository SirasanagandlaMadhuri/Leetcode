Find all anagrams
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1=len(s)
        n2=len(p)
        ans=[]
        if n1<n2:
            return []
        s_count=[0]*26
        p_count=[0]*26
        for i in range(n2):
            s_count[ord(s[i])-97]+=1
            p_count[ord(p[i])-97]+=1
        if s_count==p_count:
            ans.append(0)
        for i in range(n2,n1):
            s_count[ord(s[i])-97]+=1
            s_count[ord(s[i-n2])-97]-=1
            if s_count==p_count:
                ans.append(i-n2+1)
        return ans
