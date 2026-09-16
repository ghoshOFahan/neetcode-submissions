class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxLen=0
        for start in range(0,len(s)):
            while(s[start] in s[left:start]):
                left+=1
            maxLen=max(maxLen,(start-left)+1)
        return maxLen

