class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character,Character> koto = new HashMap<>();
        koto.put(')','('); 
        koto.put('}','{'); 
        koto.put(']','['); 
        for(char c:s.toCharArray())
        {
            if( koto.containsKey(c))
            {
                if(!stack.isEmpty()&&stack.peek()==koto.get(c))
                {
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
