class Solution:
    def isValid(self, s: str) -> bool:
        freq={}
        freq[")"]="("
        freq["]"]="["
        freq["}"]="{"
        stack=[]
        for i in s:
            if i in freq and stack:
                if stack[-1]==freq[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
