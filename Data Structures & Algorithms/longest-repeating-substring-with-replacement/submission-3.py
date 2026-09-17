class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        maxLen=0
        max1=float("-inf")
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max1=max(count[s[right]],max1)
            while(right-left+1-max1>k):
                count[s[left]]-=1
                left+=1
            maxLen=max(maxLen, right-left+1)
        return maxLen