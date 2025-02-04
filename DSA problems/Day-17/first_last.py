#leetcode
#34. Find First and Last Position of Element in Sorted Array
#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        idx=[]
        while i <= j:
            if idx == []:
                if nums[i]==target:
                    idx.append(i)
                    continue
                i+=1
            else:
                if nums[j]==target:
                    idx.append(j)
                    break
                j-=1
        if idx ==[]:
            return [-1,-1]
        else:
            return idx


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]