class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store={}
        for index,value in enumerate(nums):
            if value in store:
                return True
            store[value]=index
        return False
