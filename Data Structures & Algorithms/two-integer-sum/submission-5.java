class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> obj = new HashMap<>();

        for(int i=0;i<nums.length;i++)
        {
            int num = nums[i];
            int diff = target - num;
            
            if(obj.containsKey(diff))
            {
                return new int[]{obj.get(diff),i};
            }
            obj.put(num,i);
        }
        return new int[]{};
    }
}
