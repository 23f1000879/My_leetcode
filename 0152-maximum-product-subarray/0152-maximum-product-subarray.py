class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = nums[0]
        current_min = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            new_max = max(nums[i], current_max * nums[i], current_min * nums[i])
            new_min = min(nums[i], current_max * nums[i], current_min * nums[i])
            current_max, current_min = new_max, new_min
            best = max(best,current_max,current_min)
        return best