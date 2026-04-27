class Solution {
     private boolean alph(char C)
        {
            return (C>='A'&&C<='Z'||C>='a'&&C<='z'||C>='0'&&C<='9');
        }
    public boolean isPalindrome(String s) {
        
        int l=0,r=s.length()-1;
        
        while(l<r)
        {
            while(l<r && !alph(s.charAt(l)) )
            {
                l++;
            }
            while(l<r && !alph(s.charAt(r)) )
            {
                r--;
            }
        
            if (Character.toLowerCase(s.charAt(l))!=Character.toLowerCase(s.charAt(r)))
            {
                return false;
            }
            l++;r--;
        }
        return true;
    }
    
}
