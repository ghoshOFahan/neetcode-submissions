class Solution:
    def climbStairs(self, n: int) -> int:
        s={}
        def dp(n,s):
            if n==0:
                return 1
            if n==1:
                return 1
            if n in s:
                return s[n]
            s[n]=dp(n-1,s)+dp(n-2,s)
            return s[n]
        return dp(n,s)