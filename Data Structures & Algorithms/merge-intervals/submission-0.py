class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        for first,second in intervals[1:]:
            last_end=res[-1][1]
            if first<=last_end:
                res[-1][1]=max(last_end,second)
            else:
                res.append([first,second])
        return res

