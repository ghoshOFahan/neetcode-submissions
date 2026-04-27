class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if diff in freq:
                if freq[diff]<i: return [freq[diff],i]
                else: return [i,freq[diff]]
            freq[nums[i]]=i
        return []