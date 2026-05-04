class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr={}
        for i in nums:
            if i in arr:
                return True
            arr[i]=arr.get(i,0)+1
        return False