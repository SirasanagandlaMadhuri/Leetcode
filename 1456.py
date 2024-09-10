Question: maximum number of vowel letters in any substring of s with length k.
Solution:
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        ans=0
        word=list(s[:k])
        c=sum(1 for i in word if i in vowels)
        ans=c
        for i in range(k,len(s)):
            if s[i] in vowels:
                c+=1
            if s[i-k] in vowels:
                c-=1
            ans=max(c,ans)
        return ans
