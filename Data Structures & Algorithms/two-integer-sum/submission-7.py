class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for n in range(0,len(nums)):
            diff = target-nums[n]
            if diff in freq:
                if freq[diff]<n: return [freq[diff],n]
                return [n,freq[diff]]
            freq[nums[n]]=n
        return []
