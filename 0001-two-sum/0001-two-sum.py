class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in seen:
                return (seen[remain], i)
            seen[nums[i]] = i