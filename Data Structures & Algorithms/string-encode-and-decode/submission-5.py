class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for i in strs:
            string=string+str(len(i))+"#"+i
            # 5#hello4#word
        return string
    def decode(self, s: str) -> List[str]:
        string=[];i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            string.append(word)
            i=j+1+length
        return string
