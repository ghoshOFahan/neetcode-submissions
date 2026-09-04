class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s={}
        n=len(cost)
        def dp(i):
            if i==0:
                return 0
            if i==1:
                return 0
            if i in s:
                return s[i]
            s[i]=min((dp(i-1)+cost[i-1]),(dp(i-2)+cost[i-2]))
            return s[i]
        return dp(n)