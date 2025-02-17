#leetcode
#81. Search in Rotated Sorted Array II
#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

#same concept as before, but due to duplicated we might have to add new condition to shrink the search
            # if nums[low]==nums[mid]==nums[high]:
            #     low+=1
            #     high-=1
            #     continue


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        low=0
        high=n-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target: return True
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]:
                if target >=nums[low] and target <=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1	
            else: 
                #right array is sorted
                if target >= nums[mid] and target <=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

        return False
