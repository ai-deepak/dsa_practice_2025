
# leetcode
# Problem: Merge Sorted Array

#brute force - solved it myself
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            idx = len(nums1)-i-1
            nums1[idx]=nums2[i]

        nums1.sort()
        # print(nums1)   



#optimal solution - got hint from chatgpt and solved it
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        p = m+n-1
        while p2 >= 0 and p1 >= 0:
            if nums1[p1]>nums2[p2]:
                nums1[p]=nums1[p1]
                p1-=1
            else:
                nums1[p]=nums2[p2]
                p2-=1
            p-=1
        while p2 >= 0:
            nums1[p]=nums2[p2]
            p2-=1
            p-=1