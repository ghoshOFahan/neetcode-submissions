class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach=0
        for index,jump in enumerate(nums):
            if index>maxreach:
                return False
            maxreach = max(maxreach,index+jump)
        return True