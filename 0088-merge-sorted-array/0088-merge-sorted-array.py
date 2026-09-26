class Solution(object):
    def merge(self, nums1, m, nums2, n):
        arr1 = nums1[:m]
        result = []

        i = 0
        j = 0

        while i < m and j < n:
            if arr1[i] <= nums2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        # Remaining elements from arr1
        while i < m:
            result.append(arr1[i])
            i += 1

        # Remaining elements from nums2
        while j < n:
            result.append(nums2[j])
            j += 1

        # Put result into nums1
        for i in range(m + n):
            nums1[i] = result[i]