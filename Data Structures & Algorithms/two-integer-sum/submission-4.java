public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> obj = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int diff = target - nums[i];
            
            if(obj.containsKey(diff) && obj.get(diff)!=i)
            {
                return new int[]{obj.get(diff),i};
            }
            obj.put(nums[i],i);
        }
        return new int[]{};
    }
}