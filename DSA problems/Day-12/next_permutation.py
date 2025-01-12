#leetcode
#31. Next Permutation
#https://leetcode.com/problems/next-permutation/description/


# i gaveup and watch the striver video for this problem. as i could not come up with optimal solution.

#brute force approach is the same approach what is given in the question
# first we take permutation of the array and sorting it.
# we do linear search and find the next permutation.
# if we need to code that, we need to do it recursively for permutation.
# but it will take a lot of time.
# time complexity is O(N! * N)
# hence we only tell the approach to the interviewer.


#below is the solution to the optimal approach
#1. Approach is to find the breakpoint by looping from last. number lessar than the previous number.
#2. After finding the breakpoint, we again loop from last and find the nearst greatest number.
#3. Swap that number with breakpoint number.
#4. now we need to reverse the array length (breakpoint+1 to len(nums)-1)
#5. once we do it, we can get the next permutation.

# any doubts, visit striver video for clear explanation.

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx=i
                break
        if idx ==-1:
            x=0
            y=len(nums)-1
            while x < y:
                nums[x],nums[y]=nums[y],nums[x]
                x+=1
                y-=1
            return nums
        for i in range(len(nums)-1,0,-1):
            if nums[idx]<nums[i]:
                nums[idx],nums[i]=nums[i],nums[idx]
                break

        x=idx+1
        y=len(nums)-1
        while x < y:
            nums[x],nums[y]=nums[y],nums[x]
            x+=1
            y-=1