class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        
        def rob1(i):
            if i>=n:return 0
            if dp[i]!=-1:return dp[i]

            current_robbery=nums[i]+rob1(i+2)
            skip_robbery=rob1(i+1)

            dp[i]=max(current_robbery,skip_robbery)
            return dp[i]
        return rob1(0)