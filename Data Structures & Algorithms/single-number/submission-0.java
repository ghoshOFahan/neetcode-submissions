class Solution {
    public int singleNumber(int[] nums) {
        int missing = nums[0];
        for(int i=1;i<nums.length;i++){
            missing = missing^nums[i];
        }
        return missing;
    }
}
