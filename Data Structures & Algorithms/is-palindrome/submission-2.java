class Solution {
    public boolean isPalindrome(String s) {
        String s1 = s.toLowerCase();
        String rev="",rev1="";
        for(char c:s1.toCharArray())
        {
            if(Character.isLetter(c) || Character.isDigit(c))
            {
                rev = c + rev;
                rev1= rev1 + c;
            }
        }
        if(rev.equals(rev1))
        {
            return true;
        }
        return false;
    }
}
