class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_product=nums[0]
        current_minproduct=nums[0]
        max_product=nums[0]
        for i in range(1,len(nums)):
            old_max=current_product
            old_min=current_minproduct
            current_product=max(nums[i],old_max*nums[i],old_min*nums[i])
            current_minproduct=min(nums[i],old_max* nums[i],old_min*nums[i])
            max_product=max(max_product,current_product)
        return max_product