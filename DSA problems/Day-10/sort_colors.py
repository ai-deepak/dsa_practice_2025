#leetcode
#75. Sort Colors
#https://leetcode.com/problems/sort-colors/submissions/1503715712/

#my solution, worked after 3 submission. I tried using hashmap. O(N+K) time complexity. O(U) space complexity. U -> unique number

nums = [1,1]
numdict={}

for i in nums:
    if i not in numdict:
        numdict[i]=1
    else:
        numdict[i]+=1
print(numdict)
y=0
i=0
while y < len(nums):
    if i in numdict:
        if numdict[i]:
            nums[y]=i
            y+=1
            numdict[i]-=1
        else:
            i+=1
    else:
        i+=1

print(nums)

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?
# after watching striver video, understood the concept and coded 3 pointer solution.
# time complexity O(N) and space comp O(1)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=len(nums)-1
        while mid <= high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        


