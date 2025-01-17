#leetcode
# 704. Binary Search
# https://leetcode.com/problems/binary-search/description/

# time and space complexity is O(n) and O(1) respectively

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
    
# optimized solution
# time and space complexity is O(logn) and O(1) respectively
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
    