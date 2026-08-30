class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0;right=len(nums)-1;res=0
        while(left<=right):
            mid=int((left+right)/2)
            if nums[mid]<target:
                left+=1
            elif nums[mid]>target:
                right-=1
            elif nums[mid]==target:
                return mid
            
        return -1