class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char=[0]*26
        for i in s:
            char[ord(i)-ord('a')]+=1
        for i in t:
            char[ord(i)-ord('a')]-=1
        for i in char:
            if i!=0:
                return False
        return True