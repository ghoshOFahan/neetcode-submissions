class Solution:
    def isValid(self, s: str) -> bool:
        freq={};arr=[]
        freq['}']='{'
        freq[')']='('
        freq[']']='['
        for i in s:
            if i in freq and  len(arr)>0 and arr[-1]==freq[i]:
                arr.pop()
            else:
                arr.append(i)
        if len(arr)==0:
            return True
        return False
