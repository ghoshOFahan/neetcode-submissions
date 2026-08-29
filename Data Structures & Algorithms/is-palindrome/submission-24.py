class Solution:
    def isPalindrome(self, s: str) -> bool:
        def valChar(s):
            if (ord(s)>=97 and ord(s)<=122) or (ord(s)>=48 and ord(s)<=57):
                return True
            return False
        s1=s.lower()
        left=0;right=len(s)-1
        while(left<right):
            while(left<right and not valChar(s1[left])):
                left+=1
            while(left<right and not valChar(s1[right])):
                right-=1
            if s1[left]!=s1[right]:
                return False
            else:
                left+=1
                right-=1
        return True


            