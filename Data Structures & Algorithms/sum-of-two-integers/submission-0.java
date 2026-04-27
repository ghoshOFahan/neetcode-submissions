class Solution {
    int carry =0;
    public int getSum(int a, int b) {
        while(b!=0){
            carry =(a&b)<<1;
            a = a^b;
            b = carry;
        }
        return a;
    }
}
