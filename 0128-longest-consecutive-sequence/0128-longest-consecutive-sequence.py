class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        for i in range(len(nums)):
            s.add(nums[i])
        longest=0
        for i in s:
            if i-1 not in s:
                x=i
                count=1
                while x+1 in s:
                    
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest
