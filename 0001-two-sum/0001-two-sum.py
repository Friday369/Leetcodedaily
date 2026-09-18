class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in s:
               return[s[complement],i]
            s[nums[i]]=i
        return []