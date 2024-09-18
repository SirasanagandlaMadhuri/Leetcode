Find the occurence of the first string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if haystack==needle:
            return 0        
        for i in range(len(haystack)-len(needle)+1):
            sub=haystack[i:i+len(needle)]
            if sub in needle:
                return i
        return -1
