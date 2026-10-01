class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split()
        word = word[::-1]
        result = " ".join(word)
        return result
        
        