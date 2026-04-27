class Solution {
    public boolean isPalindrome(String s) {
        String rev="",rev1="";
        String s1=s.toLowerCase();
        for(char c:s1.toCharArray())
        {
            if(Character.isLetter(c)||(Character.isDigit(c)))
            {
                rev=rev+c;
                rev1=c+rev1;
            }
        }
        if(rev.equals(rev1))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
