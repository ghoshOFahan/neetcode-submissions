class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dir={}
        for i in nums:
            if i in dir:
                dir[i]+=1
            else:
                dir[i]=1
        buckets=defaultdict(list)
        for num,freq in dir.items():
            buckets[freq].append(num)
        res=[]
        for i in range(len(nums),0,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res)==k:
                    return res
        return res
            
        