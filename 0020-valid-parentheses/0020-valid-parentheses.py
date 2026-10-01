class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dicts = {')':'(', ']':'[', '}':'{'}
        opens = ['(', '{', '[']
        check = []
        for i in range(len(s)):
            if s[i] in opens:
                check.append(s[i])
            else:
                if check == []:
                    return False
                else:
                    if check[-1] == dicts[s[i]]:
                        check.pop()
                    else:
                        return False
        return check == []
                    

        