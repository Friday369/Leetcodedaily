class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count={}
        for i in nums:
    
            if  i in count:
                count[i]+=1
            else:
                count[i]=1
        buckets=[[] for j in range(len(nums)+1)]
        
        for i,freq in count.items():
            buckets[freq].append(i)
        result=[]
        for freq in range(len(buckets)-1,0,-1):
            for i in buckets[freq]:
                result.append(i)
                if len(result)==k:
                    return result
        return result