#geeksforgeeks
#https://www.geeksforgeeks.org/problems/ceil-the-floor2802/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=ceil-the-floor


#i tried linear solution, it worked. and it is the optimal solution.
# time complexity is O(n)

#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        floor=-1
        ceiling=-1
        maxi=float('inf')
        mini=float('inf')
        for num in arr:
            if num < x:
                diff = x - num
                if diff < maxi:
                    floor = num
                    maxi = diff
            elif num > x:
                diff = num - x
                if diff < mini:
                    ceiling = num
                    mini = diff
            elif num == x:
                floor, ceiling = num, num
                break
        return [floor,ceiling]

#also tried an O(n logn) solution (myself)

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        def func(arr,x):
            arr.sort()
            n=len(arr)
            low=0
            high=n-1
            floor=-1
            ceil=-1
            floordiff=float('inf')
            ceildiff=float('inf')
            while low<=high:
                mid=(low+high)//2
                if arr[mid]==x:
                    floor=ceil=arr[mid]
                    return [floor,ceil]
                elif arr[mid]<=x:
                    fdiff=x-arr[mid]
                    if fdiff < floordiff:
                        floor=arr[mid]
                        floordiff=fdiff
                    low=mid+1
                else:
                    cdiff=arr[mid]-x
                    if cdiff < ceildiff:
                        ceil=arr[mid]
                        ceildiff=cdiff
                    high=mid-1
            
            return [floor,ceil]
        
        return func(arr,x)

#chatgpt solution

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()  # Sorting the array (O(N log N))
        n = len(arr)
        low, high = 0, n - 1
        floor, ceil = -1, -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == x:
                return [x, x]  # Exact match, return x as both floor and ceil
            
            elif arr[mid] < x:
                floor = arr[mid]  # Possible floor candidate
                low = mid + 1  # Move right to find a closer value
            
            else:
                ceil = arr[mid]  # Possible ceil candidate
                high = mid - 1  # Move left to find a closer value
        
        return [floor, ceil]


