class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        unique = set()
        for i in range(0,len(nums)):
            start = i+1;end=len(nums)-1
            while(start<end):
                if nums[i]+nums[start]+nums[end]<0:
                    start+=1
                elif nums[i]+nums[start]+nums[end]>0:
                    end-=1
                else:
                    unique.add(tuple(sorted([nums[i],nums[start],nums[end]])))
                    start+=1;end-=1
        return [list(i) for i in unique]
                