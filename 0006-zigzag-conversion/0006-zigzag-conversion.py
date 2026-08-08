class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        row = 0
        going_down = False

        for c in s:
            rows[row] += c
            if row == 0 or row == numRows - 1:
                going_down = not going_down
            row += 1 if going_down else -1

        return ''.join(rows)