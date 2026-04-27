class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult,zero = 1,0
        for num in nums:
            if num:
                mult*=num
            else:
                zero+=1
        if zero>1: return[0]*len(nums)
        res=[0]*len(nums)
        for i,c in enumerate(nums):
            if zero: res[i]=0 if c else mult
            else: res[i]=mult//c
        return res