class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        prefix_sum=0
        s={0:1}
        for i in nums:
            prefix_sum+=i
            if prefix_sum-k in s:
                count+=s[prefix_sum-k]
            if prefix_sum in s:
                s[prefix_sum]+=1
            else:
                s[prefix_sum]=1
        return count


        