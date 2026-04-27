class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> obj = new HashSet<>();
        for(int i:nums)
        {
            if(obj.contains(i))
            {
                return true;
            }
            else{
                obj.add(i);
            }
        }
        return false;
    }
}
