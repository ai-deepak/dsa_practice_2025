#leetcode
# 152. Maximum Product Subarray


#solved it by watch striver video (for intuition watch the video)
#optimal solution

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = 1
        suffix = 1
        maxi=float('-inf')
        n=len(nums)
        for i in range(n):
            if prefix==0: prefix=1
            if suffix==0: suffix=1
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]
            maxi = max(maxi,max(prefix,suffix))
        return maxi