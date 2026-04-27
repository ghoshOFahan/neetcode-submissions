class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower().replace(" ","")
        start=0;end=len(s1)-1
        while(start<end):
            while start<end and not s1[start].isalnum():
                start+=1
            while start<end and not s1[end].isalnum():
                end-=1
            if s1[start]!=s1[end]:
                return False
            start+=1
            end-=1
        return True
