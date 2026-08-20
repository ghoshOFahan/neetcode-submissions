class Solution:
    def climbStairs(self, n: int) -> int:
        s={}
        def dep(n,s) -> int:
            if n==1:return 1
            if n==0:return 1
            if n in s:
                return s[n]
            s[n]=dep(n-1,s)+dep(n-2,s)
            return s[n]
        return dep(n,s)