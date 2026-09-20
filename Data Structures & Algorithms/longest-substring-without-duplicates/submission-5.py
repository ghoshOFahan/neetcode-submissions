class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        longest=0
        s1=set()
        for right in range(len(s)):
            while s[right] in s1 :
                s1.remove(s[left])
                left+=1
            longest=max(longest,right-left+1)
            s1.add(s[right])
        return longest
            
