#leetcode
# binary search - easy
# https://leetcode.com/problems/kth-missing-positive-number/

# solved it myself

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i=1
        j=0
        missing=0
        counter=0
        while counter<k:
            if j < len(arr) and i == arr[j]:
                j += 1
            else:
                missing = i
                counter += 1
            i += 1
        return missing


# #actual code
# class Solution(object):
#     def findKthPositive(self, arr, k):
#         """
#         :type arr: List[int]
#         :type k: int
#         :rtype: int
#         """
#         i=1
#         j=0
#         missing=0
#         counter=0
#         while counter<k:
#             if j < len(arr):
#                 if i==arr[j]:
#                     i+=1
#                     j+=1
#                 elif i!=arr[j]:
#                     missing=i
#                     i+=1
#                     counter+=1
#             else:
#                 missing=i
#                 i+=1
#                 counter+=1
#         return missing
