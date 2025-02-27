#leetcode
#1283. Find the Smallest Divisor Given a Threshold
#https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

#solved it myself using binary search

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def smallDiv(nums,t):
            low=1
            high=max(nums)
            
            while low<high:

                mid=(low+high)//2
                asum = 0
                for i in nums:
                    asum+=(i+mid-1)//mid
                if asum > threshold:
                    #move right
                    low=mid+1
                else:
                    high=mid
            
            return low

        return smallDiv(nums,threshold)