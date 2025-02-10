#geeksforgeeks
#https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?track=DSASP-Searching&amp%253BbatchId=154&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=floor-in-a-sorted-array

# brute force is to do linear search
# below optimal solution (after watching striver notes)
# for more discussion with chatgpt - https://chatgpt.com/share/67a9e14a-5d0c-800d-9fbb-ea0f927959ed

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        #Your code here
        
        low, high = 0, len(arr) - 1
        ans = -1  # Initialize answer to -1 (default if no floor exists)

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= k:
                ans = mid  # Store the best candidate so far
                low = mid + 1  # Move to the right half to find a larger floor
            else:
                high = mid - 1  # Move to the left half

        return ans


