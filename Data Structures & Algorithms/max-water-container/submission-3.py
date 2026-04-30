class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights)==0: return 0
        start=0;end=len(heights)-1;maxArea=0
        while start<end:
            diff = end - start
            capacity_diff = min(heights[start],heights[end])
            maxArea = max(maxArea,capacity_diff*diff)
            
            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1
        return maxArea