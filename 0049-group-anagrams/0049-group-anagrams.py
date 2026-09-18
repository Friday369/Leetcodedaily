class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
    
        """
        anagrams={}
        for word in strs:
            sorted_words="".join(sorted(word))
            if sorted_words in anagrams:
                anagrams[sorted_words].append(word)
            else:
                anagrams[sorted_words]=[word]
        return list(anagrams.values())
