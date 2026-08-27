class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s={}
        n=len(cost)
        def dp(i,s):
            if i >=n:
                return 0
            if i in s:
                return s[i]
            s[i]=cost[i]+min(dp(i+1,s),dp(i+2,s))
            return s[i]
        return min(dp(0,s),dp(1,s))
    