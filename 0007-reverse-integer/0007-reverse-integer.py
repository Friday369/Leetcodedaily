class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_x = int(str(x)[::-1])
        result = sign * reversed_x

        if result > INT_MAX or result < INT_MIN:
            return 0

        return result