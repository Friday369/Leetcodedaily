class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n,m=len(p),len(s)
        result=[]
        if n>m:
            return result
        need=[0]*26
        window=[0]*26
        for i in p:
            need[ord(i)-ord('a')]+=1
        for right in range(m):
            window[ord(s[right])-97]+=1
            if right>=n:
                window[ord(s[right-n])-97]-=1
            if right>=n-1 and window==need:
                result.append(right-n+1)
        return result