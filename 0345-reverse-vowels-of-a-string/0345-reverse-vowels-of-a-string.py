class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = list(s)
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left = 0
        right = len(s) - 1
        while left < right:
            if arr[left] not in vowel:
                left +=1
            elif arr[right] not in vowel:
                    right -=1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left +=1
                right -=1
        
        s = "".join(arr)
        return s
        