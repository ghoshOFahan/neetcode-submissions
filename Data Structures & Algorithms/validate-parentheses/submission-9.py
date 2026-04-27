class Solution:
    def isValid(self, s: str) -> bool:
        freq={};arr=[]
        freq[')']='('
        freq['}']='{'
        freq[']']='['
        for ch in s:
            if ch in freq:
                if arr and arr[-1]==freq[ch]:
                    arr.pop()
                else:
                    return False
            else:
                arr.append(ch)
        return not arr