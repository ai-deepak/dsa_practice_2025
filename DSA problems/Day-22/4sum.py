#leetcode
#18. 4Sum
#https://leetcode.com/problems/4sum/description/

# based on 3sum problem, we can solve 4sum problem by fixing one element and then finding 3sum for remaining elements.
# i have coded myself without watching any videos
# time complexity is O(n^3) and space complexity is O(n)

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = set()
        for i in range(n):
            for y in range(i+1,n):
                j=y
                k=j+1
                l=n-1
                while k<l:
                    alsum = nums[i]+nums[j]+nums[k]+nums[l]
                    if alsum == target:
                        res.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif alsum < target:
                        k+=1
                    elif alsum > target:
                        l-=1

        return list(res)
    
#slightly optimized version, removing set

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates for nums[i]
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:  # Skip duplicates for nums[j]
                    continue
                k, l = j+1, n-1
                while k < l:
                    alsum = nums[i] + nums[j] + nums[k] + nums[l]
                    if alsum == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:  # Skip duplicates for nums[k]
                            k += 1
                        while k < l and nums[l] == nums[l+1]:  # Skip duplicates for nums[l]
                            l -= 1
                    elif alsum < target:
                        k += 1
                    else:
                        l -= 1
        
        return res

