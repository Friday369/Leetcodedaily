class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams={}
        for word in strs:
            counts=[0]*26
            for char in word:
                counts[ord(char)-ord('a')]+=1
            key=tuple(counts)
            if key not in anagrams:
                anagrams[key]=[word]
            else:
                anagrams[key].append(word)
        return list(anagrams.values())        