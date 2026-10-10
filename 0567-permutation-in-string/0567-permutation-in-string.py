class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n,m=len(s1),len(s2)
        if n>m:
            return False
        def id_of_alphabets(ch):
            return ord(ch)-ord('a')
        need=[0]*26
        window=[0]*26
        for ch in s1:
            need[id_of_alphabets(ch)]+=1
        for right in range(m):
            window[id_of_alphabets(s2[right])]+=1
            if right>=n:
                left_Char=s2[right-n]
                window[id_of_alphabets(left_Char)]-=1
            if window==need:
                return True
        return False