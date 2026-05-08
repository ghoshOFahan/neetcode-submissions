class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def f(i):
            if i>=n:
                return 0
            if dp[i]!=-1: return dp[i]
            current=nums[i]+f(i+2)
            next=f(i+1)
            dp[i]=max(current,next)
            return dp[i]
        return f(0)
