Sentence similarity III
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1=sentence1.split()
        words2=sentence2.split()
        if not sentence1 or not sentence2:
            return True
        if not sentence1 and not sentence2:
            return True
        if len(words2)<len(words1):
            words1,words2=words2,words1
        l1,l2=0,0
        while l1<len(words1) and l2<len(words2) and words1[l1]==words2[l2]:
            l1+=1
            l2+=1
        r1=len(words1)-1
        r2=len(words2)-1
        while r1>=l1 and r2>=l2 and words1[r1]==words2[r2]:
            r1-=1
            r2-=1
        return l1>r1
            

        

            



            


        
