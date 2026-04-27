class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> num = new HashSet<>();
        for(int num1 : nums)
        {
            num.add(num1);
        }
        int longest = 0;
        for(int number : num)
        {
            if(!num.contains(number-1))
            {
                int length = 1;
                while(num.contains(number+length))
                {
                    length++;
                }
                longest = Math.max(longest,length);
            }
        }
        return longest;
    }
}
