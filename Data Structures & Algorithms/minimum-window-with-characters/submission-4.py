class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        left=0
        count={}
        count1={}
        string=""
        for i in range(len(t)):
            count[t[i]]=count.get(t[i],0)+1

        have, need = 0, len(count)
        for right in range(len(s)):
            c = s[right]
            count1[c]=count1.get(c,0)+1
            if c in count and count1[c] == count[c]:
                have += 1

            while have == need:
                if string=="" or right-left+1<len(string):
                    string=s[left:right+1]
                count1[s[left]]-=1
                if s[left] in count and count1[s[left]] < count[s[left]]:
                    have -= 1
                left+=1
        return string