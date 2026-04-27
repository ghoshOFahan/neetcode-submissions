class Solution {
    public int search(int[] nums, int target) {
        int l=0,r=nums.length-1;
        if(nums.length==1 && nums[0]==target)
        {
            return 0;
        }
        while(l<=r)
        {
            int gen=(l+r)/2;
            if(nums[gen]<target)
            {
                l++;
            }
            else if(nums[gen]>target)
            {
                r--;
            }
           
            else{
                return gen;
            }
        }
        return -1;
    }
}
