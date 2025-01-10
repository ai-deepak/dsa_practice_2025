#leetcode
#53. Maximum Subarray
# The below solution is what i coded. Which is using 2 for loops
# basic test case solved. But got time limit exceeded error for other cases
# time complexity O(N^3) and space complexity O(1)
# how? outer loop O(N) * inner loop O(N) * sum operation O(N) = O(N^3)

nums = [-2,1,-3,4,-1,2,1,-5,4]
finalMax=float('-inf')
if len(nums)<1:
    print(nums[0])
else:
    for i in range(len(nums)):
        for y in range(i+1,len(nums)+1):
            finalMax = max(sum(nums[i:y]),finalMax)
print(finalMax)

# i need to figure out solution for O(n).
#watched striver video, kadane's algorithm

class Solution(object):
    def maxSubArray(self, nums):
        asum=0
        finalMax=nums[0]
        for i in range(len(nums)):
            asum=asum+nums[i]
            finalMax = max(finalMax, asum)
            asum = max(asum, 0)
        return finalMax
    
#follow up: If you have figured out the O(n) solution, 
#try coding another solution using the divide and conquer approach, which is more subtle.

