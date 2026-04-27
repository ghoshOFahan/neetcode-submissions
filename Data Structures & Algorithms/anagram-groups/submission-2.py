class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for string in strs:
            sortedS=''.join(sorted(string))
            res[sortedS].append(string)
        final=[]
        for i in res:
            final.append(res[i])
        return final

            