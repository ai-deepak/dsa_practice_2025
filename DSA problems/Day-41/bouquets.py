#leetcode
# #1482. Minimum Number of Days to Make m Bouquets
#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/


# brute force is to use for loop

# i tried binary solution - watched striver video for explanation. O(NlogD)

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def bloom(arr,m,k):
            n=len(arr)
            low=min(arr)
            high=max(arr)
            minDay=-1
            if m*k>n:
                return -1
                
            while low<=high:
                mid = (low+high)//2
                count=0
                minSum=0
                for i in arr:
                    if i <= mid:
                        count+=1
                    else:
                        minSum+=(count//k)
                        count=0
                if count !=0:
                    minSum+=(count//k)
                    count=0
                if minSum>=m:
                    minDay=mid
                    high=mid-1
                else:
                    low=mid+1
            
            return minDay

        return bloom(bloomDay,m,k)
        
#chatgpt slightly optimized , same logic and complexity

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMakeBouquets(day: int) -> bool:
            bouquets, count = 0, 0
            for bloom in bloomDay:
                if bloom <= day:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0  # Reset count for the next bouquet
                else:
                    count = 0  # Reset count if the streak breaks
                if bouquets >= m:
                    return True
            return False

        if m * k > len(bloomDay):
            return -1
        
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid + 1
        return low
