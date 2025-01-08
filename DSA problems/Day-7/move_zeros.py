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


#after striver video - my improved solution

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=-1
        while i < len(nums):
            if nums[i] != 0:
                i+=1
            elif nums[i] == 0:
                j=i
                i=i+1
                break
        if j==-1:
            return nums
        while i < len(nums):
            if nums[i] != 0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                j+=1
            else:
                i+=1
        return nums
    
#time complexity is O(n)
#space complexity is O(1)


#python few lines of code (optimized with same complexity)

nums = [1,0,2,3,2,0,0,4,5,1]
non_zero = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[non_zero] = nums[non_zero], nums[i]
        non_zero += 1
        
print(nums)