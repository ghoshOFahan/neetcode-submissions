class Solution:
    def isValid(self, s: str) -> bool:
        freq={};stack=[]
        freq[')']='('
        freq['}']='{'
        freq[']']='['
        for ch in s:
            if ch in freq:
                if stack and freq[ch]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack