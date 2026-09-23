class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        arr = list(flowerbed)
        count = 0
        for i in range(len(flowerbed)):
            if arr[i]==0:
                if (i == 0) or (arr[i-1] == 0):
                    if (i == len(arr) - 1) or (arr[i+1] == 0):
                        arr[i] = 1
                        count = count+1
        if count >= n:
            return True
        else:
            return False
