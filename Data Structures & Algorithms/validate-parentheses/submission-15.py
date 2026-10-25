class Solution:
    def isValid(self, s: str) -> bool:
        freq={};arr=[]
        freq["]"]="["
        freq["}"]="{"
        freq[")"]="("
        for i in s:
            if i in freq:
                if len(arr)!=0 and freq[i]==arr[-1]:
                    arr.pop()
                else:
                    return False
            else:
                arr.append(i)
        return len(arr)==0
        