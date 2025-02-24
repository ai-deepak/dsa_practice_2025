    #geeksforgeeks
    #https://www.geeksforgeeks.org/problems/square-root/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=square-root

    #my solution

    class Solution:
        def floorSqrt(self, n): 
            return int(n**(1/2))
        
    #using binary search

    #Complete this function
    class Solution:
        def floorSqrt(self, n): 
        #Your code here
            # return int(n**(1/2))
            
            low=0
            high=n
            
            while low<=high:
                mid=(low+high)//2
                
                if mid*mid==n:
                    return mid
                elif mid*mid>n:
                    high=mid-1
                else:
                    low=mid+1
                    
            return high


#chatgpt newton method (aka babylonian method)
# for more explanation watch this chat: https://chatgpt.com/share/67b85715-8c04-800d-83fa-a5ba1eb52e19
# complexity is O(log logn) which is better than O(logn) of binary search


class Solution:
    def floorSqrt(self, n):
        if n == 0 or n == 1:
            return n
        x = n
        while x * x > n:
            x = (x + n // x) // 2  # Integer division to keep floor value
            
        return x
    

