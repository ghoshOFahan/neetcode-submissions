class Solution {
    public int maxArea(int[] heights) {
        int l=0,r=heights.length-1;
        int res = 0,area=0;
        while(l<r)
        {
            area = (r-l) * Math.min(heights[r],heights[l]);
            res = Math.max(area,res);
            if(heights[l]<heights[r])
            {
                l++;
            }
            else
            {
                r--;
            }
        }
        return res;
    }
}
