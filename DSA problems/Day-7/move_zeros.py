#leetcode
#283. Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,count=0,0
        while i < len(nums):
            if nums[i]==0:
                nums.pop(i)
                count+=1
                i-=1
            i+=1
        for i in range(count):
            nums.append(0)
        return nums
    
#time complexity is O(n^2)

#need to improve the code