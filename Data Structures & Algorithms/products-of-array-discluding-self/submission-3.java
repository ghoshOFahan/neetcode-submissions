class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] count =new int[nums.length];
        int mult = 1;int zero=0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]==0)
            {
                zero++;
            }
            else
            {
                mult = mult*nums[i];
            }
        }
        for(int i=0;i<count.length;i++)
        {
            if(zero==1 && nums[i]==0)
            {
                count[i]=mult;
            }
            else if(zero==1 && nums[i]!=0)
            {
                count[i]=0;
            }
            else if(zero>1)
            {
                count[i]=0;
            }
            else
            {
                count[i]=mult/nums[i];
            }
        }
        return count;
    }
}  
