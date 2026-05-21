class Solution {
    public boolean isPalindrome(String s) {
        String s1=s.toLowerCase();
        int start=0,end=s1.length()-1;
        while(start<=end){
            while(start<end && !Character.isLetterOrDigit(s1.charAt(start))){
                start++;
            }
            while(start<end && !Character.isLetterOrDigit(s1.charAt(end))){
                end--;
            }
            if (s1.charAt(start)!=s1.charAt(end)){
                return false;
            }
            start++;end--;
        }
        return true;
    }
}
