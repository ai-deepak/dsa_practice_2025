#leetcode
#540. Single Element in a Sorted Array
#https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        if len(nums) > 1:
            while i < len(nums):
                if i == len(nums)-1:
                    return nums[i]
                elif nums[i]!=nums[i+1]:
                    return nums[i]
                i+=2
        return nums[0]