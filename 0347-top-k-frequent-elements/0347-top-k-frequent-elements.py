class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        sorted_Result=sorted(count,key=count.get,reverse=True)
        return sorted_Result[:k]

        