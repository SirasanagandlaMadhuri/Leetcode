Simplify path
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        words=path.split('/')
        for i in words:
            if i=="..":
                if stack:
                    stack.pop()
            elif i!="." and i!="":
                stack.append(i)
        res="/"+"/".join(stack)
        return res


        
            
