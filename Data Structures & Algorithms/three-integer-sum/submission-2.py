class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique=set()
        for i in range(0,len(nums)):
            target = -nums[i]
            s=set()
            for j in range(i+1,len(nums)):
                c = target-nums[j]
                if c in s:
                    triplet=tuple(sorted([nums[i],nums[j],c]))
                    unique.add(triplet)
                else:
                    s.add(nums[j])
        return [list(t) for t in unique]
