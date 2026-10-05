class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water=0
        right=len(height)-1
        left=0
        while left<right:
            width=right-left
            h=min(height[left],height[right])
            water=width*h
            max_water=max(max_water,water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_water
        