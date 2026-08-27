class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=[0]*26
        for i in s:
            s1[ord(i)-97]+=1
        for i in t:
            s1[ord(i)-97]-=1
        for i in s1:
            if i!=0:
                return False
        return True