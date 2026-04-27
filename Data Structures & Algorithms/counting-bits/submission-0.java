class Solution {
    public int[] countBits(int n) {
        int[] arr = new int[n+1];
        for(int i=0;i<n+1;i++){
            arr[i] = count1(i);
        }
        return arr;
    }
    public int count1(int n){
        int res = 0;
        while(n!=0){
            n&=(n-1);
            res++;
        }
        return res;
    }
}
