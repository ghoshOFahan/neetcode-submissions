class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]
        for current_index,current_temp in enumerate(temperatures):
            while stack and current_temp>temperatures[stack[-1]]:
                prev_temp_index=stack.pop()
                output[prev_temp_index]=current_index-prev_temp_index
            stack.append(current_index)
        return output

