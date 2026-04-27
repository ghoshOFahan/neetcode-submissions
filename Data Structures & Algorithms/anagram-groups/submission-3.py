class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for string in strs:
            ch=[0]*26
            for c in string:
                ch[ord(c)-ord('a')]+=1
            res[tuple(ch)].append(string)
        return list(res.values())


            