class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split()
        for i in range(len(word)):
            if i<(len(word)-1-i):
                word[i], word[len(word)-1-i] = word[len(word)-1-i], word[i]
        result = " ".join(word)
        return result
        