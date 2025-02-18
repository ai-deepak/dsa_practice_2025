#leetcode
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# 153. Find Minimum in Rotated Sorted Array

# i did solve with help of chatgpt

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1

        while low < high:

            mid = (low+high)//2
            
            if nums[mid] > nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]
