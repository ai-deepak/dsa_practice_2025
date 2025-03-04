#leetcode
#kth missing
#https://leetcode.com/problems/kth-missing-positive-number/


#my solution - O(n^2)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = arr[-1]+k
        count=0
        for i in range(1,n+1):
            if i not in arr:
                count+=1
                if count==k:
                    return i
                

# after watching striver video - O(log n)
def kthmissing(arr,k):
    low=0
    high=len(arr)-1
    
    def missingCount(arr,idx):
        missing = arr[idx]-(idx+1)
        return missing
        
    while low <= high:
        mid=(low+high)//2
        missing_count = missingCount(arr,mid)
        if missing_count < k:
            low=mid+1
        else:
            high=mid-1
    
    return arr[high] + (k- missingCount(arr,high))

print(kthmissing(arr,k))


