class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        for i in heights:
            start=0;end=len(heights)-1
            while start<end:
                
                minHeight=min(heights[start],heights[end])
                area=max(area,minHeight*(end-start))

                if heights[start]<=heights[end]:
                    start+=1
                else:
                    end-=1
        return area
