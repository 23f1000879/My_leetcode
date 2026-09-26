class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insertPos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insertPos], nums[i] = nums[i],nums[insertPos]
                insertPos+=1
        return nums

        