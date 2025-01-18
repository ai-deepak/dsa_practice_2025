#leetcode
#35. Search insert position
#https://leetcode.com/problems/search-insert-position/description/

#time and space complexity is O(n) and O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target > nums[i]:
                continue
            elif target <= nums[i]:
                return i
        if target > nums[-1]:
            return len(nums)