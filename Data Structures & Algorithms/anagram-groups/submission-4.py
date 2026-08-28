class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list=defaultdict(list)
        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-97]+=1
            key=tuple(count)
            anagram_list[key].append(word)
        s=[]
        for i in anagram_list:
            s.append(anagram_list[i])
        return s