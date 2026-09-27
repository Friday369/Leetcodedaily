class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first=None
        second=None
        third=None
        for i in nums:
            if i==first or i==second or i==third:
                continue
            if first is None or first<i:
                third=second
                second=first
                first=i
            elif second is None or second<i:
                third=second
                second=i
            elif third is None or third<i:
                third=i
        if third is not None:
            return third
        return first