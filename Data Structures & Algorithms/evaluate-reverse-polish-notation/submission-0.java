class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> obj = new Stack<>();
        for(String s:tokens)
        {
            if(! (s.equals("+")||s.equals("-")||s.equals("*")||s.equals("/")))
            {
                obj.push(s);
            }
            else 
            {
                int right = Integer.parseInt(obj.pop());    
                int left = Integer.parseInt(obj.pop());        

                switch (s) {
                    case "+":
                        obj.push(Integer.toString(left + right));
                        break;
                    case "-":
                        obj.push(Integer.toString(left - right));
                        break;
                    case "*":
                        obj.push(Integer.toString(left * right));
                        break;
                    case "/":
                        obj.push(Integer.toString(left / right));
                        break;
                }
            }
        }
        return Integer.parseInt(obj.pop());
    }
}
