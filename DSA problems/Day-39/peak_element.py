#leetcode
#https://leetcode.com/problems/find-peak-element/description/
# 162. Find Peak Element
# this problem has 4 solution - brute force linear approach, my binary search, striver solution, stunning chatgpt solution

#brute force approach - complexity O(n)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        peak=float('-inf')
        if n==1:
            return 0
        for i in range(n):
            if i==0:
                if nums[i]>nums[i+1]:
                    peak=i
                    return peak
            if i==n-1:
                if nums[i]>nums[i-1]:
                    peak=i
                    return peak
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                peak=i
                return peak
        return peak
    
#optimised approach binary search - complexity O(logn)
#after watching striver video
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        if n==1:
            return 0
        while low<=high:
            mid=(low+high)//2
            if mid==0 and nums[mid]>nums[mid+1]:
                return mid
            if mid==n-1 and nums[mid]>nums[mid-1]:
                return mid
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid]>nums[mid+1]:
                high=mid-1
            else:
                low=mid+1

        return -1

#striver solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        if n==1: return 0
        if nums[0]>nums[1]: return 0
        if nums[n-1]>nums[n-2]: return n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid]>nums[mid+1]:
                high=mid-1
            else:
                low=mid+1

        return -1
    
#stunning chatgpt solution
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:  
                high = mid
            else:
                low = mid + 1

        return low