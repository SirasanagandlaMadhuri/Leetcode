REMOVING STARS FROM A STRING 
class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for char in s:
            if char.isalpha():
               stack.append(char) 
            if char=='*':
                stack.pop()
        return "".join(stack)
