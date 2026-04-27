class MinStack {
    Stack<Integer> minstack1;
    int arr[] = new int[15];
    public MinStack() {
        minstack1= new Stack<>();
    
    }
    
    public void push(int val) {
        minstack1.push(val);
    }
    
    public void pop() {
        minstack1.pop();
    }
    
    public int top() {
        int val = minstack1.peek();
        return val;
    }
    
    public int getMin() {
        int compare = Integer.MAX_VALUE,count =0;
        while(!minstack1.isEmpty()){
            if(minstack1.peek()<compare)
            {
                compare = minstack1.peek();
            }
            arr[count]=minstack1.pop();
            count++;
        }
        for(int i = count-1;i>=0;i--)
        {
            minstack1.push(arr[i]);
            arr[i]=0;
        }
        return compare;
    }
}
