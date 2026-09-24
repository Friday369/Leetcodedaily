class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        count=[0]*(len(nums)+1)
        for i in nums:
            count[i]+=1
        for i in nums:
            if count[i]==2:
                result.append(i)
                count[i]=0 #To prevent duplicate entry
        return result