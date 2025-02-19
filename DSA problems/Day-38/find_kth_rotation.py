#geeksforgeeks
#https://www.geeksforgeeks.org/problems/rotation4723/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=rotation
#Find Kth Rotation

#this problem similar to the leetcode find minimum in rotated sorted array problem, 
# instead of returning the minimum element we have to return the element index, which is actually kth rotation.

# complexity: O(logn)

class Solution:
    def findKRotation(self, arr):
        # code here
        n=len(arr)
        low=0
        high=n-1
        
        while low<high:
            
            mid = (low+high)//2
            
            if arr[mid] > arr[high]:
                low=mid+1
            else:
                high=mid
        
        return low
