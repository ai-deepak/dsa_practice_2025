#leetcode
#169. Majority Element
#https://leetcode.com/problems/majority-element/description/

# i coded this solution myself using hashmaps. But this is not optimal solution
# iterating over N elements - O(N)
# dictionary operation to insert - O(1)
# max opertaion (iteration over dictionary to search for max) - O(N)
# time complexity is O(2N) which is O(N). 
# space complexity is O(N) as we use hashmaps.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """
        a = {}
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        return max(a, key=a.get)
    
#Follow-up: Could you solve the problem in linear time and in O(1) space?
# Saw the striver video for optimal solution - using Moore's voting algorithm
# which follows 2 steps
# 1. find the element
# 2. validating the element is the right element or not
# i coded the below solution.

class Solution(object):
    def majorityElement(self, nums):
        count = 1
        i = 1
        ele = nums[0]
        while i < len(nums):
            if count != 0:
                if nums[i]==ele:
                    count+=1
                else:
                    count-=1
            else:
                ele=nums[i]
                count=1
            i+=1

        counter=0
        for y in range(len(nums)):
            if nums[y]==ele:
                counter+=1
        if counter > (len(nums)//2):
            return ele
        
#chatgpt gave me optimized code, without validation (if the majority is gauranteed)
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        ele = None
        for num in nums:
            if count == 0:
                ele = num
            count += 1 if num == ele else -1
        return ele
