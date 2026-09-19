class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1=set(nums1)
        result=set()
        for i in nums2:
            if i in s1:
                result.add(i)
        return list(result)
        