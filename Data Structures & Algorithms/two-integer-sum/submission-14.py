class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}
        for index,value in enumerate(nums):
            diff=target-value
            if diff in store:
                return [store[diff],index]
            store[value]=index
        return []