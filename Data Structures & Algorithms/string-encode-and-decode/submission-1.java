class Solution {

    public String encode(List<String> strs) {
        String result="";
        for(String s: strs)
        {
            result=result+s.length()+"#"+s;
        }
        return result;
    }

    public List<String> decode(String str) {
        List<String> arr = new ArrayList<>();int i =0;
        while(i<str.length())
        {
            int j = str.indexOf("#",i);
            int lengt = Integer.parseInt(str.substring(i,j));
            String cut = str.substring(j+1,j+1+lengt);
            arr.add(cut);
            i = j+1+lengt;
        }
        return arr;
    }
}
