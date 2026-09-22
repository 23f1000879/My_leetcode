class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = list(nums)
        for i in range(len(nums)):
            ans.append(nums[i])
            
            
        return ans
        