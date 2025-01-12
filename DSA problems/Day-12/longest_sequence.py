#leetcode
#128. Longest Consecutive Sequence
#https://leetcode.com/problems/longest-consecutive-sequence/description/


# i Saw the striver video and crafter this solution, need to revisit this problem again.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def func(nums):
            if len(nums)>1:
                numset = set(nums)
                count=1
                maxi=1
                for i in numset:
                    currEle=i
                    prevEle=i-1
                    if prevEle not in numset:
                        nextEle=i+1
                        while nextEle in numset:
                            count+=1
                            maxi=max(maxi,count)
                            nextEle+=1
                    count=1
                return maxi
            elif nums==[]:
                return 0
            return 1
        return func(nums)